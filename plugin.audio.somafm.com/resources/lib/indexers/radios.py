# -*- coding: utf-8 -*-

"""
    SomaFM Add-on
    Author: Twilight0

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from tulip import directory, client, cache, control
from ..modules import syshandle, sysaddon
from urlparse import urljoin
import json


class Indexer:

    def __init__(self):

        self.list = [] ; self.data = [] ; self.groups = [] ; self.qofs = []
        self.main = 'http://somafm.com'
        self.index = urljoin(self.main, '/listen/genre.html')

        if control.setting('group') == 'Name':
            self.translated = control.lang(30003)
        elif control.setting('group') == 'Popularity':
            self.translated = control.lang(30004)
        elif control.setting('group') == 'Genre':
            self.translated = control.lang(30005)

        self.switch = {'title': control.lang(30006).format(self.translated),
                       'icon': control.join(control.addonPath, 'resources', 'media', 'selector.png'), 'action': 'switcher'}

    def switcher(self):

        def seq(choose):

            control.setSetting('group', choose)
            control.idle()
            # if control.condVisibility('MusicPlayer.HasNext'):
            #     control.execute('Playlist.Clear')
            control.sleep(50)
            control.refresh()

        self.groups = [control.lang(30003), control.lang(30004), control.lang(30005)]

        choice = control.selectDialog(heading=control.lang(30006), list=self.groups)

        if choice == 0:
            seq('Name')
        elif choice == 1:
            seq('Popularity')
        elif choice == 2:
            seq('Genre')
        else:
            control.execute('Dialog.Close(all)')

    def get_stations(self, url):

        import datetime
        year = datetime.datetime.now().year

        html = client.request(url)
        main = client.parseDOM(html, 'div', attrs={'id': 'midstations'})[0]
        items = client.parseDOM(main, 'li')

        for item in items:

            name = client.parseDOM(item, 'h3')[0]
            image = client.parseDOM(item, 'img', ret='src')[0]
            image = urljoin(self.main, image)
            urls = client.parseDOM(item, 'a', ret='href')[3:-1]
            links = [urljoin(self.main, link) for link in urls]
            streams = json.dumps(links)
            listeners = client.parseDOM(item, 'dd')[-2]
            n = client.parseDOM(item, 'span', attrs={'class': 'playing'})[0]
            now = client.parseDOM(n, 'a')[0]
            history = client.parseDOM(n, 'a', ret='href')[0]
            history = urljoin(self.main, history)
            genre = html.split(item)[0]
            genre = client.parseDOM(genre, 'h1', attrs={'class': 'GenreHeader'})[-1]
            description = client.parseDOM(item, 'p', attrs={'class': 'descr'})[0]

            if control.setting('caching') == 'false' and control.setting('station') == 'true':
                title = name + ' ~ ' + now
            elif control.setting('caching') == 'false' and control.setting('station') == 'false':
                title = now.partition(' - ')[2]
            else:
                title = name

            data = {'title': title, 'image': image, 'url': streams,
                    'listeners': int(listeners), 'history': history, 'genre': genre, 'artist': now.partition(' - ')[0],
                    'album': name, 'year': year, 'comment': description, 'mediatype': 'music'}

            self.list.append(data)

        return self.list

    def stations(self):

        import itertools
        from operator import itemgetter

        self.list = cache.get(self.get_stations, 0 if control.setting('caching') == 'false' else int(control.setting('period')), self.index)

        if self.list is None:
            return

        for item in self.list:
            item.update({'action': 'play', 'isFolder': 'False'})

        for item in self.list:
            refresh = {'title': 30015, 'query': {'action': 'refresh'}}
            cache_clear = {'title': 30002, 'query': {'action': 'cache_clear'}}
            # station_info = {'title': 30016, 'query': {'action': 'description', 'text': item['comment']}}
            history = {'title': 30017, 'query': {'action': 'history', 'url': item['history']}}
            item.update({'cm': [refresh, cache_clear, history]})

        if control.setting('switcher') == 'true':
            if control.setting('group') == 'Name':
                self.list = sorted(self.list, key=lambda k: k['album'].lower())
                self.list = itertools.groupby(self.list, key=itemgetter('album'))
                self.list = [next(item[1]) for item in self.list]
            elif control.setting('group') == 'Popularity':
                self.list = sorted(self.list, key=lambda k: str(k['listeners']))
                self.list = itertools.groupby(self.list, key=itemgetter('album'))
                self.list = [next(item[1]) for item in self.list]
            elif control.setting('group') == 'Genre':
                self.list = sorted(self.list, key=lambda k: k['genre'].lower())
                self.list = itertools.groupby(self.list, key=itemgetter('album'))
                self.list = [next(item[1]) for item in self.list]
            else:
                self.list = self.list
        elif control.setting('switcher') == 'false' and control.setting('index_method') == '0':
            self.list = sorted(self.list, key=lambda k: k['album'].lower())
            self.list = itertools.groupby(self.list, key=itemgetter('album'))
            self.list = [next(item[1]) for item in self.list]
        elif control.setting('switcher') == 'false' and control.setting('index_method') == '1':
            self.list = sorted(self.list, key=lambda k: str(k['listeners']))
            self.list = itertools.groupby(self.list, key=itemgetter('album'))
            self.list = [next(item[1]) for item in self.list]
        elif control.setting('switcher') == 'false' and control.setting('index_method') == '2':
            self.list = sorted(self.list, key=lambda k: k['genre'].lower())
            self.list = itertools.groupby(self.list, key=itemgetter('album'))
            self.list = [next(item[1]) for item in self.list]
        else:
            self.list = self.list

        count = 1

        for item in self.list:
            item.setdefault('tracknumber', count)
            count +=1

        if control.setting('switcher') == 'true':
            li = control.item(label=self.switch['title'], iconImage=self.switch['icon'])
            li.setArt({'fanart': control.addonInfo('fanart')})
            li.setProperty('IsPlayable', 'false')
            url = '{0}?action={1}'.format(sysaddon, self.switch['action'])
            control.addItem(syshandle, url, li, isFolder=False)
        else:
            pass

        directory.add(self.list, infotype='music')
