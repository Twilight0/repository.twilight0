# -*- coding: utf-8 -*-

'''
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
'''

import json, re

from tulip import bookmarks, directory, client, cache, workers, youtube, control
from urlparse import urljoin


class Indexer:

    def __init__(self):
        self.list = []; self.data = []
        self.base_link = 'http://www.star.gr/'
        self.news_link = urljoin(self.base_link, '_layouts/handlers/tv/feeds.program.ashx?catTitle=News&artId=9')
        self.news_image = urljoin(self.base_link, 'tv/PublishingImages/2015/04/080415181740_0653.jpg')
        self.tvshows_link = urljoin(self.base_link, '_layouts/handlers/tv/feeds.program.ashx?catTitle=hosts')
        self.episodes_link = urljoin(self.base_link, '_layouts/handlers/tv/feeds.program.ashx?catTitle=%s&artId=%s')
        self.cartoon_link = urljoin(self.base_link, 'tv/el/Pages/StarlandIndex.aspx')
        self.web_tv_link = urljoin(self.base_link, 'webtv/')
        self.play_link = 'http://cdnapi.kaltura.com/p/21154092/sp/2115409200/playManifest/entryId/%s/flavorId/%s/format/url/protocol/http/a.mp4'
        self.live_link = 'http://klive-a.akamaihd.net/dc-1/live/hls/p/713821/e/1_fp7fyi3j/sd/10000/t/ZA8fcNZ-c0boV5jwPLnSfg/index-s32.m3u8'
        self.youtube_key = 'AIzaSyBOS4uSyd27OU0XV2KSdN3vT2UG_v0g9sI'
        self.youtube_link = 'UCwUNbp_4Y2Ry-asyerw2jew'

    def root(self):

        self.list = [
            {
                'title': 32009,
                'action': 'live',
                'isFolder': 'False',
                'icon': 'live.png'
            }
            ,
            {
                'title': 32001,
                'action': 'tvshows',
                'icon': 'tvshows.png'
            }
            ,
            {
                'title': 32007,
                'action': 'web_tv',
                'icon': 'www.png'
            }
            ,
            {
                'title': 32002,
                'action': 'archive',
                'icon': 'archive.png'
            }
            ,
            {
                'title': 32003,
                'action': 'cartoon',
                'icon': 'cartoon.png'
            }
            ,
            {
                'title': 32004,
                'action': 'popular',
                'icon': 'popular.png'
            }
            ,
            {
                'title': 32005,
                'action': 'news',
                'icon': 'news.png'
            }
            ,
            {
                'title': 32006,
                'action': 'bookmarks',
                'icon': 'bookmarks.png'
            }
        ]

        for item in self.list:
            cache_clear = {'title': 30403, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear]})

        directory.add(self.list)

    def bookmarks(self):

        self.list = bookmarks.get()

        if self.list is None:
            return

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['delbookmark'] = i['url']
            i.update({'cm': [{'title': 32502, 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    def tvshows(self):

        self.list = cache.get(self._tv_shows, 24, self.tvshows_link)

        if self.list is None:
            return

        for i in self.list: i.update({'action': 'episodes'})

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    def cartoon(self):

        self.list = cache.get(self._cartoons, 24, self.cartoon_link)

        if self.list is None:
            return

        for i in self.list: i.update({'action': 'episodes'})

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    def episodes(self, url, image):

        self.list = cache.get(self._episodes, 1, url, image)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'play', 'isFolder': 'False'})

        directory.add(self.list)

    def archive(self):

        self.list = cache.get(youtube.youtube(key=self.youtube_key).playlists, 24, self.youtube_link)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'youtube'})

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    def youtube(self, url):
    
        self.list = cache.get(youtube.youtube(key=self.youtube_key).playlist, 1, url)

        if self.list is None:
            return

        self.list = [i for i in self.list if int(i['duration']) > 120]

        for i in self.list: i.update({'action': 'play', 'isFolder': 'False'})

        directory.add(self.list)

    def popular(self):

        self.list = cache.get(youtube.youtube(key=self.youtube_key).videos, 1, self.youtube_link)

        if self.list is None:
            return

        self.list = [i for i in self.list if int(i['duration']) > 120]

        for i in self.list:
            i.update({'action': 'play', 'isFolder': 'False'})

        directory.add(self.list)

    def web_tv(self):

        self.list = cache.get(self._webtv, 24)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'web_episodes'})

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    def web_episodes(self, url):

        self.list = cache.get(self._webepisodes, 24, url)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'play', 'isFolder': 'False'})

        directory.add(self.list, content='episodes')

    def news(self):

        self.episodes(self.news_link, self.news_image)

    def play(self, title, image, url):

        if len(url) == 11:

            from youtube_resolver import resolve as yt_resolve
            link = yt_resolve(url)
            stream = link[1]['url']
            directory.resolve(stream, meta={'title': title}, icon=image)

        else:

            directory.resolve(url)

    def live(self):

        directory.resolve(self.live_link, meta={'title': 'STAR HD'}, icon=control.addonInfo('icon'))

    def _webtv(self):

        html = client.request(urljoin(self.web_tv_link, 'index.php'))

        divclass = client.parseDOM(html, 'div', attrs={'class': 'category-posts-grid-row large-post-row clearfix'})

        bare_links = client.parseDOM(divclass, 'a', ret='href')
        links = [urljoin(self.web_tv_link, i) for i in bare_links]

        result = client.parseDOM(divclass, 'a')

        items = zip(result, links)

        for item, url in items:

            title = client.parseDOM(item, 'h2')[0]
            image = client.parseDOM(item, 'img', ret='src')[0]
            image = urljoin('http://www.star.gr/webtv/', image)

            data = dict(title=title, image=image, url=url)

            self.list.append(data)

        return self.list

    def _tv_shows(self, url):

        try:
            result = client.request(url, mobile=True)
            result = json.loads(result)
            items = result['hosts']
        except:
            return

        for item in items:

            try:

                title = item['Title'].strip()
                title = client.replaceHTMLCodes(title)
                title = title.encode('utf-8')

                id = item['ProgramId']
                cat = item['ProgramCat'].strip()
                url = self.episodes_link % (cat, id)
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                image = item['Image'].strip()
                image = urljoin(self.base_link, image)
                image = client.replaceHTMLCodes(image)
                image = image.encode('utf-8')

                self.list.append({'title': title, 'url': url, 'image': image})

            except:
                pass

        return self.list

    def _episodes(self, url, image):

        try:

            result = client.request(url, mobile=True)
            result = json.loads(result)
            items = result['videosprogram']

        except:
            return

        for item in items:

            try:
                title = item['Title'].strip()
                title = client.replaceHTMLCodes(title)
                title = title.encode('utf-8')

                url = item['VideoID'].strip()
                url = self.play_link % (url, url)
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                self.list.append({'title': title, 'url': url, 'image': image})

            except:
                pass

        return self.list

    def _webepisodes(self, url):

        html = client.request(url)

        table = client.parseDOM(html, 'table', attrs={'class': 'table-fill'})[0]

        info = re.findall('text-left\">(.+?)<', table, re.U | re.S)
        self.data = [i.strip() for i in info]
        show = self.data[0]
        name = self.data[1]
        presentation = self.data[2]
        people = self.data[3]
        description = self.data[4]
        plot = self.data[5]

        episodes = client.parseDOM(html, 'a', attrs={'id': 'show_video_id'})

        for count, episode in list(enumerate(episodes[::-1], start=1)):

            datestr = client.parseDOM(episode, 'time')[0].partition('</span>')[2]
            date = datestr.split('/')[::-1]
            fixed = []
            for i in date:
                if len(i) == 1:
                    fixed.append('0' + i)
                else:
                    fixed.append(i)
            aired = '-'.join(fixed)
            title = name + ' - ' + control.lang(32008) + ' - ' + datestr
            link = client.parseDOM(episode, 'article', ret='onclick')[0]
            link = re.findall("'(.+?)'", link)[0]
            # link = urljoin('http://https://www.youtube.com/embed/', link)
            image = client.parseDOM(episode, 'img', ret='src')[0]

            data = dict(
                title=title, image=image, url=link, aired=aired, genre=show, year=date[0], episode=count,
                plot=presentation + ': ' + people + '\n' + description + ': ' + plot
            )

            self.list.append(data)

        return self.list

    def _cartoons(self, url):

        try:
            result = client.request(url)

            result = client.parseDOM(result, 'a', ret='href')
            result = [i for i in result if 'starland' in i.lower()]
            result = [re.findall('artId=(\d*)', i) for i in result]
            result = [i[0] for i in result if len(i) > 0]
            result = [x for y, x in enumerate(result) if x not in result[:y]]
            result = [self.episodes_link % ('Starland', i) for i in result]

            threads = []
            for i in range(0, len(result)):
                threads.append(workers.Thread(self.thread, result[i], i))
                self.data.append('')
            [i.start() for i in threads]
            [i.join() for i in threads]

            items = self.data

        except:
            return

        for item in items:

            try:

                item = json.loads(item)

                # videos = item['videosprogram'][0]['VideoID']

                title = item['programme']['Title'].strip()
                title = client.replaceHTMLCodes(title)
                title = title.encode('utf-8')

                id = item['programme']['ProgramId']
                cat = item['programme']['ProgramCat'].strip()
                url = self.episodes_link % (cat, id)
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                image = item['programme']['Image'].strip()
                image = urljoin(self.base_link, image)
                image = client.replaceHTMLCodes(image)
                image = image.encode('utf-8')

                self.list.append({'title': title, 'url': url, 'image': image})

            except:

                pass

        return self.list

    def thread(self, url, i):

        try:
            result = client.request(url)
            self.data[i] = result
        except:
            return
