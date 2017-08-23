# -*- coding: utf-8 -*-
'''
    Author    : Huseyin BIYIK <husenbiyik at hotmail>
    Year      : 2016
    License   : GPL

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
import sublib.utils
import sublib.sub
import sublib.item

import json
import urllib
import os
import sys
import urlparse
import shutil

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs


class service(object):
    '''Base class to inherit for subtitle service.

    Example:
        import sublib
        import os

        class mysubtitlesite(sublib.service):

            def search(self):
                print self.item
                sub = self.sub("Test Subtitle", "en")
                sub.download("http://a.com/b/c.srt")
                self.addsub(sub)

            def download(self, link)
                fname = os.path.join(self.path, "test.srt")
                with open(fname, "w") as f:
                    f.write(self.download(link))
                self.addfile(fname)
    Params:
        ua: User-Agent string to be used for http queries

    Attributes:

        sub: factory class for found subtitles, see sublib.sub.model()

        item: object holding information that is found from Kodi,
            see sublib.item.model()

        path: temp directory to save the downloaded subtitle file,
            you can use your own directory if you want

    '''

    sub = sublib.sub.model

    def __init__(self, ua=None):
        if not ua:
            self._ua = sublib.utils.useragent
        else:
            self._ua = ua
        self._subs = []
        self._paths = []
        addon = xbmcaddon.Addon()
        self._sid = xbmcaddon.Addon().getAddonInfo('id')
        profile = addon.getAddonInfo('profile')
        self._profile = xbmc.translatePath(profile).decode("utf-8")
        temp = os.path.join(profile, 'temp')
        self.path = xbmc.translatePath(temp).decode("utf-8")
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
        xbmcvfs.mkdirs(self.path)
        params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
        params = sublib.utils.dformat(params, json.loads)
        action = params.get("action", None)
        preflang = params.get('preferredlanguage', "")
        langs = params.get('languages', [])
        self.item = sublib.item.model(preflang, langs)
        self.item.title, self.item.show, self.item.season, self.item.episode =\
            sublib.utils.infofromstr(
                                     self.item.fname,
                                     self.item.title,
                                     self.item.show,
                                     self.item.season,
                                     self.item.episode
                                     )
        if action:
            method = getattr(self, "_action_%s" % action.lower())
            self._params = params
            method()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

    def _action_search(self):
        self.search()
        sorter = sublib.sub.sorter(self.item.languages[0])
        self._subs.sort(key=sorter.method, reverse=True)
        for sub in self._subs:
            if sub.iso not in self.item.languages and len(sub.iso) == 2:
                continue
            listitem = xbmcgui.ListItem(
                        label=xbmc.convertLanguage(sub.iso, xbmc.ENGLISH_NAME),
                        label2=sub.label,
                        iconImage=str(sub.rating),
                        thumbnailImage=sub.iso
                        )
            listitem.setProperty("sync", '{0}'.format(sub.sync).lower())
            listitem.setProperty("hearing_imp", '{0}'.format(sub.cc).lower())
            args = {
                    "action": "download",
                    "args": sub.args,
                    "kwargs": sub.kwargs,
                    "languages": self._params['languages'],
                    "prefferedlanguage": self._params['preferredlanguage']
                    }
            url = urllib.urlencode(sublib.utils.dformat(args, json.dumps))
            url = "plugin://%s/?%s" % (self._sid, url)

            xbmcplugin.addDirectoryItem(
                                        handle=int(sys.argv[1]),
                                        url=url,
                                        listitem=listitem,
                                        isFolder=False
                                        )

    def _action_manualsearch(self):
        self.item.title = None
        self.item.title, self.item.show, season, episode =\
            sublib.utils.infofromstr(
                                     self._params["searchstring"],
                                     self.item.title,
                                     self.item.show,
                                     )
        if season >= 0:
            self.item.season = season
        if episode >= 0:
            self.item.episode = episode
        self.item.imdb = None
        self.item.tvdb = None
        self.item.tmdb = None
        self.item.trakt = None
        self.item.slug = None
        if self.item.show:
            self.item.year = None
        self._action_search()

    def _action_download(self):
        self.download(*self._params["args"], **self._params["kwargs"])
        for fname in self._paths:
            sub = sublib.utils.getsub(
                                    fname,
                                    self.item.show,
                                    self.item.season,
                                    self.item.episode
                                    )
            if not sub:
                return
            listitem = xbmcgui.ListItem(label=sub)
            xbmcplugin.addDirectoryItem(
                                        handle=int(sys.argv[1]),
                                        url=sub,
                                        listitem=listitem,
                                        isFolder=False
                                        )

    def search(self):
        '''This is the method that service has to override. Service supposed to
        find the correct subtitle using self.item obeject, and create a
        self.sub instance , and then the found instance must be added with
        self.addsub(subins) method.

        Example:
            def search(self):
                print self.item
                sub = self.sub("Test Subtitle", "en")
                sub.download("http://a.com/b/c.srt")
                self.addsub(sub)

            def download(self, link)
                fname = os.path.join(self.path, "test.srt")
                with open(fname, "w") as f:
                    f.write(self.download(link))
                self.addfile(fname)

        Params:
            None

        Returns:
            None
        '''
        sub = self.sub("Test Subtitle", "en")
        self.addsub(sub)

    def download(self, *args, **kwargs):
        '''This is the method that service has to override. Service supposed to
        download the found subtitle to a path, and add this path with
        self.addfile("/path/to/file"). *args, **kwargs of the of method is
        dynamically created with sub.download(*arg, **kwargs) method. You can
        use self.temp folder to save to for ease of access
        but this is not mendatory

        Example:
            def download(self, link, id, isstuff)
                fname = os.path.join(self.path, "test.srt")
                with open(fname, "w") as f:
                    f.write(self.download(link))
                self.addfile(fname)

        Params:
            *args: created dynamically from sub.download(*args, *kwargs) method
            **kwargs: created dynamically from sub.download(*args, *kwargs)
                method

        Returns:
            None
        '''
        self.addfile("/path/to/file")

    def num(self, issub=True):
        '''Returns the number of found instances. if issub is True, found
        subtitles are counted else downlaoded files are counted.

        Params:
            issub: if issub is True, found subtitles are counted else
                downlaoded files are counted.

        Returns:
            int:numberofitems
        '''
        if issub:
            return len(self._subs)
        else:
            return len(self._paths)

    def request(self, url, query=None, data=None, referer=None, binary=False):
        ''' Helper method to make an http query. This is method is good enough
        for vast majority of your needs, includding cookie handlers, with/get
        post requests, if you need more advanced queries you can also use
        requests or your own implementation

        Params:
            u: url of the request
            query: dict carrying the url request arguments
            data: dict carrying the values to be posted
            referer: referer for request header
            binary: bool flag that determines if the return data should be
                encoded text if set False, or urllib2.response object
                if set True

        Returns:
            str/urllib2.reponse:response
        '''
        return sublib.utils.download(url,
                                     query,
                                     data,
                                     referer,
                                     binary,
                                     ua=self._ua
                                     )

    def addsub(self, sub):
        ''' Method to use if a subtitle is found when in self.search method

        Params:
            sub: subtitle instance of self.sub factory class

        Returns:
            None
        '''

        if not isinstance(sub, sublib.sub.model):
            raise TypeError(sub)
        self._subs.append(sub)

    def addfile(self, path):
        ''' Method to use if a subtitle is downloaded when in self.download method

        Params:
            path: /path/to/subtitle/file.srt

        Returns:
            None
        '''
        self._paths.append(path)
