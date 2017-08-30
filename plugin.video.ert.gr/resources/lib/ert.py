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

import urlparse, json, re
# noinspection PyUnresolvedReferences
from tulip import bookmarks, directory, client, cache, control


class indexer:

    def __init__(self):

        self.list = []
        self.base_link = 'http://webtv.ert.gr'
        self.categories_link = 'http://webtv.ert.gr/programma/'
        self.episodes_link = 'http://webtv.ert.gr/?cat=%s'
        self.sports_link = 'http://webtv.ert.gr/category/athlitika/'
        self.news_link = 'http://webtv.ert.gr/category/eidiseis/'
        self.info_link = 'http://webtv.ert.gr/category/ert-enimerosi/'
        self.weather_link = 'http://webtv.ert.gr/category/kairos/'
        self.documentary_link = 'http://webtv.ert.gr/tag/ntokimanter/'
        self.culture_link = 'http://webtv.ert.gr/tag/politismos/'
        self.cartoons_link = 'http://webtv.ert.gr/category/paidika/'
        self.entertainment_link = 'http://webtv.ert.gr/tag/psichagogia/'
        self.popular_link = 'http://webtv.ert.gr/feed/'
        self.ert1_link = 'http://webtv.ert.gr/ert1-live/'
        self.ert2_link = 'http://webtv.ert.gr/ert2-live/'
        self.ert3_link = 'http://webtv.ert.gr/ert3-live/'
        self.ertw_link = 'http://webtv.ert.gr/ertworld-live/'
        self.ertp_link = 'http://webtv.ert.gr/ert-play-live/'
        self.radio_link = 'http://webradio.ert.gr/'
        self.district_link = 'http://webradio.ert.gr/liveradio/list.html'

    def root(self):

        self.list = [
            {
                'title': 32001,
                'action': 'channels',
                'icon': 'channels.png'
            }
            ,
            {
                'title': 32002,
                'action': 'popular',
                'icon': 'popular.png'
            }
            ,
            {
                'title': 32004,
                'action': 'episodes',
                'url': self.news_link,
                'icon': 'news.png'
            }
            ,
            {
                'title': 32005,
                'action': 'episodes',
                'url': self.info_link,
                'icon': 'info.png'
            }
            ,
            {
                'title': 32003,
                'action': 'episodes',
                'url': self.sports_link,
                'icon': 'sports.png'
            }
            ,
            {
                'title': 32006,
                'action': 'episodes',
                'url': self.weather_link,
                'icon': 'weather.png'
            }
            ,
            {
                'title': 32007,
                'action': 'episodes',
                'url': self.documentary_link,
                'icon': 'documentary.png'
            }
            ,
            {
                'title': 32008,
                'action': 'episodes',
                'url': self.culture_link,
                'icon': 'culture.png'
            }
            ,
            {
                'title': 32009,
                'action': 'episodes',
                'url': self.cartoons_link,
                'icon': 'cartoons.png'
            }
            ,
            {
                'title': 32010,
                'action': 'episodes',
                'url': self.entertainment_link,
                'icon': 'entertainment.png'
            }
            ,
            {
                'title': 32011,
                'action': 'categories',
                'icon': 'categories.png'
            }
            ,
            {
                'title': 32026,
                'action': 'radios',
                'icon': 'radio.png'
            }
            ,
            {
                'title': 32012,
                'action': 'bookmarks',
                'icon': 'bookmarks.png'
            }
        ]

        for item in self.list:
            cache_clear = {'title': 32036, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear]})

        directory.add(self.list, content='videos')

    def channels(self):

        self.list = [
            {
                'title': 32021,
                'action': 'live',
                'url': 'ert1',
                'isFolder': 'False',
                'icon': 'ert1.png'
            },

            {
                'title': 32022,
                'action': 'live',
                'url': 'ert2',
                'isFolder': 'False',
                'icon': 'ert2.png'
            },

            {
                'title': 32023,
                'action': 'live',
                'url': 'ert3',
                'isFolder': 'False',
                'icon': 'ert3.png'
            },

            {
                'title': 32024,
                'action': 'live',
                'url': 'ertw',
                'isFolder': 'False',
                'icon': 'ertw.png'
            }
            ,
            {
                'title': 32025,
                'action': 'live',
                'url': 'ertp',
                'isFolder': 'False',
                'icon': 'ertp.png'
            }
        ]

        for i in self.list:

            i.update({'fanart': control.addonmedia('webtv_fanart.jpg')})

        directory.add(self.list, content='videos')

    def bookmarks(self):

        self.list = bookmarks.get()

        if self.list is None:
            return

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['delbookmark'] = i['url']
            i.update({'cm': [{'title': 32502, 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: str(k['title']).lower())

        directory.add(self.list, content='videos')

    def categories(self):

        self.list = cache.get(self.categories_list, 24)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'episodes'})

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list, content='videos')

    def episodes(self, url):

        self.list = cache.get(self.episodes_list, 1, url)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'play', 'isFolder': 'False'})

        for i in self.list:
            i.update({'nextlabel': 32500, 'nextaction': 'episodes'})

        directory.add(self.list, content='videos')

    def popular(self):

        self.list = cache.get(self.popular_list, 1, self.popular_link)

        if self.list is None:
            return

        for i in self.list: i.update({'action': 'play', 'isFolder': 'False'})

        directory.add(self.list, content='videos')

    def play(self, url):
        directory.resolve(self.resolve(url))

    def live(self, url):

        if url == 'ert1':
            title = 'EPT 1'
            # icon = 'ert1.png'
        elif url == 'ert2':
            title = 'EPT 2'
            # icon = 'ert2.png'
        elif url == 'ert3':
            title = 'EPT 3'
            # icon = 'ert3.png'
        elif url == 'ertw':
            title = 'EPT World'
            # icon = 'ertw.png'
        elif url == 'ertp':
            title = 'EPT Play'
            # icon = 'ertp.png'

        # logo = control.addonmedia(icon)

        directory.resolve(self.resolve_live(url), meta={'title': title})

    def radio(self, url):
        directory.resolve(self.resolve_radio(url))

    def categories_list(self):

        try:
            result = client.request(self.categories_link)

            items = re.findall('(<option\s.+?</option>)', result)
        except:
            return

        for item in items:
            try:
                title = client.parseDOM(item, 'option', attrs={'class': 'level-[1-9]'})[0]
                title = client.replaceHTMLCodes(title)
                title = title.strip().upper()
                title = title.encode('utf-8')

                url = client.parseDOM(item, 'option', ret='value', attrs={'class': 'level-[1-9]'})[0]
                url = self.episodes_link % url
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                self.list.append({'title': title, 'url': url})
            except:
                pass

        return self.list

    def episodes_list(self, url):

        try:
            result = client.request(url)

            items = client.parseDOM(result, 'div', attrs={'class': 'blog-listing-con.+?'})[0]
            items = client.parseDOM(items, 'div', attrs={'class': 'item-thumbnail'})
        except:
            return

        try:
            next = client.parseDOM(result, 'a', ret='href', attrs={'rel': 'next'})[0]
            next = urlparse.urljoin(self.base_link, next)
            next = client.replaceHTMLCodes(next)
            next = next.encode('utf-8')
        except:
            next = ''

        for item in items:
            try:
                title = client.parseDOM(item, 'a', ret='title')[0]
                title = client.replaceHTMLCodes(title)
                title = title.encode('utf-8')

                url = client.parseDOM(item, 'a', ret='href')[0]
                url = urlparse.urljoin(self.base_link, url)
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                image = client.parseDOM(item, 'img', ret='src')[0]
                image = urlparse.urljoin(self.base_link, image)
                image = client.replaceHTMLCodes(image)
                image = image.encode('utf-8')

                self.list.append({'title': title, 'url': url, 'image': image, 'next': next})
            except:
                pass

        return self.list

    def popular_list(self, url):
        try:
            result = client.request(url)

            items = client.parseDOM(result, 'item')
        except:
            return

        for item in items:
            try:
                title = client.parseDOM(item, 'title')[0]
                title = client.replaceHTMLCodes(title)
                title = title.encode('utf-8')

                url = client.parseDOM(item, 'link')[0]
                url = urlparse.urljoin(self.base_link, url)
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                image = client.parseDOM(item, 'img', ret='src')[0]
                image = urlparse.urljoin(self.base_link, image)
                image = client.replaceHTMLCodes(image)
                image = image.encode('utf-8')

                self.list.append({'title': title, 'url': url, 'image': image})
            except:
                pass

        return self.list

    def radio_list(self):

        try:

            result = client.request(self.radio_link)
            stations = client.parseDOM(result, 'figure', attrs={'class': 'wpb_wrapper vc_figure'})[:-1]
            names = [control.lang(32028), control.lang(32029), control.lang(32030), control.lang(32031),
                     control.lang(32032), control.lang(32033), control.lang(32034), control.lang(32035)]
            radios = map(lambda foo, bar: (foo, bar), names, stations)

        except:

            return

        for title, data in radios:

            link = client.parseDOM(data, 'a', ret='href')[0]
            image = client.parseDOM(data, 'img', ret='src')[0]

            self.list.append({'title': title, 'url': link, 'image': image, 'action': 'radio', 'isFolder': 'False'})

        district = [{'title': control.lang(32027), 'url': 'http://webradio.ert.gr/liveradio/list.html',
                     'icon': 'district.png', 'action': 'district'}]

        self.list.extend(district)

        return self.list

    def radios(self):

        self.list = cache.get(self.radio_list, 24)

        if self.list is None:
            return

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        directory.add(self.list)

    def district_list(self):

        try:

            result = client.request(self.district_link).decode('windows-1253')
            radios = client.parseDOM(result, 'td')
            radios = [foo for foo in radios if foo]

        except:

            return

        for radio in radios:
            title = client.parseDOM(radio, 'a')[0]
            href = client.parseDOM(radio, 'a', ret='href')[0]
            html = client.request(href)
            link = client.parseDOM(html, 'iframe', ret='src')[0]
            image = client.parseDOM(html, 'img', ret='src')[0]

            self.list.append({'title': title, 'image': image, 'url': link})

        return self.list

    def district(self):

        self.list = cache.get(self.district_list, 24)

        if self.list is None:
            return

        for i in self.list:
            i.update({'action': 'radio', 'isFolder': 'False'})

        for i in self.list:
            bookmark = dict((k, v) for k, v in i.iteritems() if not k == 'next')
            bookmark['bookmark'] = i['url']
            i.update({'cm': [{'title': 32501, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

        directory.add(self.list)

    @staticmethod
    def resolve(url):

        try:
            referer = url

            result = client.request(url)

            url = client.parseDOM(result, 'div', attrs={'class': 'play.+?'})[0]
            url = client.parseDOM(url, 'iframe', ret='src')[0]

            try:
                url = re.findall('(?:youtube.com|youtu.be)/(?:embed/|.+?\?v=|.+?\&v=|v/)([\w-]+)', url)[0]
                url = 'plugin://plugin.video.youtube/play/?video_id=%s' % url
                return url
            except:
                pass

            try:
                if not 'ert-archives.gr' in url:
                    raise Exception()
                url = urlparse.parse_qs(urlparse.urlparse(url).query)['tid'][0]
                url = 'http://www.ert-archives.gr/V3/media.hFLV?tid=%s' % url
                return url
            except:
                pass

            try:
                url = url.replace(' ', '%20')

                url = client.request(url, referer=referer)

                url = re.findall('(?:\"|\')(http.+?)(?:\"|\')', url)
                url = [i for i in url if '.m3u8' in i]
                url = [i.replace(' ', '%20') for i in url]

                u = client.request(url[0], output='geturl')
                if u is None and len(url) > 1:
                    u = client.request(url[1], output='geturl')

                return u
            except:
                pass

        except:
            pass

    def resolve_live(self, url):

        if url == 'ert1':
            link = self.ert1_link
        elif url == 'ert2':
            link = self.ert2_link
        elif url == 'ert3':
            link = self.ert3_link
        elif url == 'ertw':
            link = self.ertw_link
        elif url == 'ertp':
            link = self.ertp_link

        html = client.request('http://www.whatismyip.com/my-ip-information/')

        if 'gr.png' in html:
            GR = True
        else:
            GR = False

        result = client.request(link)

        result = client.parseDOM(result, 'iframe', ret='src')[0]

        video = client.request(result)

        if GR:

            yt_link = client.parseDOM(video, 'iframe', ret='src')[-1]
        else:

            yt_link = client.parseDOM(video, 'iframe', ret='src')[0]

        regxpr = re.compile('(?:youtube.com|youtu.be)/(?:embed/|.+?\?v=|.+?\&v=|v/)([\w-]+)')

        vid = regxpr.findall(yt_link)[0]

        from youtube_resolver import resolve as yt_resolve

        link = yt_resolve(vid)

        stream = link[0]['url']

        return stream

    @staticmethod
    def resolve_radio(url):

        result = client.request(url)

        try:
            stream = re.compile('file: ?.(.*?).,').findall(result)[0]
        except IndexError:
            stream = re.compile('"(.+?radiostreaming.+?)"').findall(result)[0]

        return stream
