# -*- coding: utf-8 -*-

'''
    Tulip routine libraries, based on lambda's lamlib
    Author Twilight0

        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re, json, urllib, urlparse
import client, workers, control


class youtube(object):

    def __init__(self, key=''):

        self.list = [] ; self.data = []
        self.base_link = 'http://www.youtube.com'
        self.key_link = '&key={0}'.format(control.setting('yt_api_key') or key)
        self.playlists_link = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&maxResults=50&channelId=%s'
        self.playlist_link = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=%s'
        self.videos_link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&maxResults=50&channelId=%s'
        self.content_link = 'https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=%s'
        self.search_link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=5&q=%s'
        self.youtube_search = 'https://www.googleapis.com/youtube/v3/search?q='
        self.youtube_watch = 'http://www.youtube.com/watch?v=%s'

        if control.condVisibility('System.HasAddon(script.module.urlresolver)') and control.setting('yt_resolve') == 'true':
            self.play_link = 'https://www.youtube.com/embed/%s'
        else:
            self.play_link = 'plugin://plugin.video.youtube/play/?video_id=%s'

    def playlists(self, url):
        url = self.playlists_link % url + self.key_link
        return self.play_list(url)

    def playlist(self, url, pagination=False):
        cid = url.split('&')[0]
        url = self.playlist_link % url + self.key_link
        return self.video_list(cid, url, pagination)

    def videos(self, url, pagination=False):
        cid = url.split('&')[0]
        url = self.videos_link % url + self.key_link
        return self.video_list(cid, url, pagination)

    def play_list(self, url):
        try:
            result = client.request(url)
            result = json.loads(result)
            items = result['items']
        except:
            pass

        for i in range(1, 5):
            try:
                if not 'nextPageToken' in result: raise Exception()
                next = url + '&pageToken=' + result['nextPageToken']
                result = client.request(next)
                result = json.loads(result)
                items += result['items']
            except:
                pass

        for item in items:
            try:
                title = item['snippet']['title']
                title = title.encode('utf-8')

                url = item['id']
                url = url.encode('utf-8')

                image = item['snippet']['thumbnails']['high']['url']
                if '/default.jpg' in image: raise Exception()
                image = image.encode('utf-8')

                self.list.append({'title': title, 'url': url, 'image': image})
            except:
                pass

        return self.list

    def video_list(self, cid, url, pagination):
        try:
            result = client.request(url)
            result = json.loads(result)
            items = result['items']
        except:
            pass

        for i in range(1, 5):
            try:
                if pagination == True: raise Exception()
                if not 'nextPageToken' in result: raise Exception()
                page = url + '&pageToken=' + result['nextPageToken']
                result = client.request(page)
                result = json.loads(result)
                items += result['items']
            except:
                pass

        try:
            if pagination == False: raise Exception()
            next = cid + '&pageToken=' + result['nextPageToken']
        except:
            next = ''

        for item in items: 
            try:
                title = item['snippet']['title']
                title = title.encode('utf-8')

                try: url = item['snippet']['resourceId']['videoId']
                except: url = item['id']['videoId']
                url = url.encode('utf-8')

                image = item['snippet']['thumbnails']['high']['url']
                if '/default.jpg' in image: raise Exception()
                image = image.encode('utf-8')

                append = {'title': title, 'url': url, 'image': image}
                if not next == '': append['next'] = next
                self.list.append(append)
            except:
                pass

        try:
            u = [range(0, len(self.list))[i:i+50] for i in range(len(range(0, len(self.list))))[::50]]
            u = [','.join([self.list[x]['url'] for x in i]) for i in u]
            u = [self.content_link % i + self.key_link for i in u]

            threads = []
            for i in range(0, len(u)):
                threads.append(workers.Thread(self.thread, u[i], i))
                self.data.append('')
            [i.start() for i in threads]
            [i.join() for i in threads]

            items = []
            for i in self.data: items += json.loads(i)['items']
        except:
            pass

        for item in range(0, len(self.list)):
            try:
                vid = self.list[item]['url']

                self.list[item]['url'] = self.play_link % vid

                d = [(i['id'], i['contentDetails']) for i in items]
                d = [i for i in d if i[0] == vid]
                d = d[0][1]['duration']

                duration = 0
                try:
                    duration += 60 * 60 * int(re.findall('(\d*)H', d)[0])
                except:
                    pass
                try:
                    duration += 60 * int(re.findall('(\d*)M', d)[0])
                except:
                    pass
                try:
                    duration += int(re.findall('(\d*)S', d)[0])
                except:
                    pass
                duration = str(duration)

                self.list[item]['duration'] = duration
            except:
                pass

        return self.list

    def thread(self, url, i):
        try:
            result = client.request(url)
            self.data[i] = result
        except:
            return

    def play(self, name, url=None):

        try:
            url = self.worker(name, url)
            if url is None:
                return

            title = control.infoLabel('listitem.title')
            if title == '':
                title = control.infoLabel('listitem.label')
            icon = control.infoLabel('listitem.icon')

            item = control.item(path=url, iconImage=icon, thumbnailImage=icon)
            try:
                item.setArt({'icon': icon})
            except:
                pass
            item.setInfo(type='Video', infoLabels={'title': title})
            control.player.play(url, item)
        except:
            pass

    def worker(self, name, url):

        try:
            if url.startswith(self.base_link):
                url = self.resolve(url)
                if url is None:
                    raise Exception()
                return url
            elif not url.startswith('http://'):
                url = self.youtube_watch % url
                url = self.resolve(url)
                if url == None:
                    raise Exception()
                return url
            else:
                raise Exception()
        except:
            query = name + ' trailer'
            query = self.youtube_search + query
            url = self.search(query)
            if url is None:
                return
            return url

    def search(self, url):

        try:
            query = urlparse.parse_qs(urlparse.urlparse(url).query)['q'][0]

            url = self.search_link % urllib.quote_plus(query) + self.key_link

            result = client.request(url)

            items = json.loads(result)['items']
            items = [(i['id']['videoId']) for i in items]

            for url in items:
                url = self.resolve(url)
                if url is not None:
                    return url
        except:
            return

    def resolve(self, url):
        try:
            id = url.split('?v=')[-1].split('/')[-1].split('?')[0].split('&')[0]
            result = client.request('http://www.youtube.com/watch?v=%s' % id)

            message = client.parseDOM(result, 'div', attrs={'id': 'unavailable-submessage'})
            message = ''.join(message)

            alert = client.parseDOM(result, 'div', attrs={'id': 'watch7-notification-area'})

            if len(alert) > 0:
                raise Exception()
            if re.search('[a-zA-Z]', message):
                raise Exception()

            url = 'plugin://plugin.video.youtube/play/?video_id=%s' % id
            return url
        except:
            return
