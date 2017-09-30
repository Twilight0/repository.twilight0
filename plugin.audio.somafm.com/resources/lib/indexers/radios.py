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
from urlparse import urljoin
import json, re
import datetime


class Indexer:

    def __init__(self):

        self.list = [] ; self.data = []
        self.main = 'http://somafm.com/'
        self.index = urljoin(self.main, 'channels.xml')

    def get_stations(self):

        year = datetime.datetime.now().year

        xml = client.request(self.index)
        stations = client.parseDOM(xml, 'channel')
        ids = client.parseDOM(xml, 'channel', ret='id')

        items = zip(ids, stations)

        for sid, item in items:

            station = client.parseDOM(item, 'title')[0].partition('A[')[2][:-3]
            image = client.parseDOM(item, 'image')[0]
            urls = re.findall('<.+?pls.+?>(.+?)</.+?pls>', item)
            streams = json.dumps(urls)
            listeners = client.parseDOM(item, 'listeners')[0]
            now = client.parseDOM(item, 'lastPlaying')[0].partition('A[')[2][:-3]
            song = now.partition(' - ')[2]
            artist = now.partition(' - ')[0]
            history = urljoin(self.main, sid + '/songhistory.html')
            genre = client.parseDOM(item, 'genre')[0]
            description = client.parseDOM(item, 'description')[0].partition('A[')[2][:-3]

            if control.setting('caching') == 'false':
                title = song
            else:
                title = station

            data = {
                'title': title, 'image': image, 'url': streams, 'listeners': int(listeners), 'history': history,
                'genre': genre, 'artist': artist, 'album': station, 'year': year, 'comment': description,
                'mediatype': 'music'
            }

            self.list.append(data)

        return self.list

    def stations(self):

        self.list = cache.get(
            self.get_stations, 0 if control.setting('caching') == 'false' else int(control.setting('period'))
        )

        if self.list is None:
            return

        for item in self.list:

            refresh = {'title': 30015, 'query': {'action': 'refresh'}}
            cache_clear = {'title': 30002, 'query': {'action': 'cache_clear'}}
            station_info = {'title': 30016, 'query': {'action': 'description', 'text': item['comment']}}
            history = {'title': 30017, 'query': {'action': 'history', 'url': item['history']}}

            if control.infoLabel('System.AddonVersion(xbmc.python)') == '2.24.0':
                item.update({'cm': [refresh, cache_clear, history], 'action': 'play', 'isFolder': 'False'})
            else:
                item.update({'cm': [refresh, cache_clear, history, station_info], 'action': 'play', 'isFolder': 'False'})

        for count, item in list(enumerate(self.list, start=1)):
            item.setdefault('tracknumber', count)

        control.sortmethods('album')
        control.sortmethods('genre')
        control.sortmethods('listeners')
        directory.add(self.list, infotype='music')
