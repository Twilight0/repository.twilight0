# -*- coding: utf-8 -*-

'''
    Heroes & Generals Addon
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

import json
from base64 import b64decode
from resources.lib import directory, url, action, youtube, cache, control, bookmarks, syshandle, sysaddon

main_id = 'UCU3aCwA_gLkw5pXA0sDwi1Q'
key = b64decode('QUl6YVN5QThrMU95TEdmMDNIQk5sMGJ5RDUxMWpyOWNGV28yR1I0')  # please do not copy this key


def item_list(id=main_id):
    return youtube.youtube(key=key).videos(id)


def _playlists(id=main_id):
    return youtube.youtube(key=key).playlists(id)


def third_party():

    menu = []

    channels = [
        {
            'title': 'Shapings',
            'icon': 'https://yt3.ggpht.com/-el5a1_jrQoY/AAAAAAAAAAI/AAAAAAAAAAA/4vfzhLOFwTU/s2256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCTyrENfBc1kF_WjJpJ69xwg/',
            'fanart': 'https://yt3.ggpht.com/mw8ST59D0EC8mic371fag7juR_98fayzCNQOlZLe4_0LWA4qWdtC0VuaZEHfpVcM-tU21J3uUQ=w1280'
        }
        ,
        {
            'title': 'My Fashion for legs',
            'icon': 'https://yt3.ggpht.com/-8KB9QMHgpfU/AAAAAAAAAAI/AAAAAAAAAAA/FnYtRAmeyfI/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCxDGBROh_raLb2hmGpnpwSw/',
            'fanart': 'https://yt3.ggpht.com/NrNpodrc7HOyHazqoR325oG3nAIvZ1w2Xm892bMjId5pvZvz-ALJ_r7TNi9SliCUIfgY_Hqv7Q=w1280'
        }
        ,
        {
            'title': 'My Pantyhose Girl',
            'icon': 'https://yt3.ggpht.com/-xcSz2kynP9Y/AAAAAAAAAAI/AAAAAAAAAAA/Yb0p_NoTlHo/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCjD1IY6M5HXXfwDIsunPnNw/',
            'fanart': 'https://yt3.ggpht.com/Bx9a_Wd9utXjH5bIYs7J7IY6V1nwb3658biejUYcAE3b6O2PtKuWVdxuil-1oOPSC5YRO4aP=w1280'
        }
        ,
        {
            'title': 'Jenny Smith',
            'icon': 'https://yt3.ggpht.com/-hXeRc4Fw_xw/AAAAAAAAAAI/AAAAAAAAAAA/tPbQ_JwDx5w/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCHYnTMm5xqESRSyiJhkfvng/',
            'fanart': 'https://yt3.ggpht.com/f8xlLtJzh80mmhkBN4Ebt1X9ATH1jBBwJe9hI2LHdAD2afKdI5cCfPD6KFGR17NriKhBIORN=w1280'
        }
        ,
        {
            'title': 'Maria Corazon',
            'icon': 'https://yt3.ggpht.com/-qGZ5TI9nePw/AAAAAAAAAAI/AAAAAAAAAAA/wBI3QIwC0TU/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCxtdrcrbK86XEX8gK-WiTFg/',
            'fanart': 'https://yt3.ggpht.com/S6FscqGLRYCnjsCswI47Ig-rOija_zdwNhcxuuf3OVZ3jvwG9V8Z4A8ERvZHou5zV0snfWy5KA=w1280'
        }
        ,
        {
            'title': 'LegsLavish',
            'icon': 'https://yt3.ggpht.com/-t1iVVloYB2A/AAAAAAAAAAI/AAAAAAAAAAA/Hvrp17BGKMU/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCihUp32JZKiT3FTrH1FrstQ/',
            'fanart': 'https://yt3.ggpht.com/bYD1ziF96PGYaD5BHOpSSSJ36MdZ0SiiPKMk2yTYtTXPblChC6VvRvWqFI7cUoQDNwgDZMpf7g=w1280'
        }
        ,
        {
            'title': 'LegsLavish Too',
            'icon': 'https://yt3.ggpht.com/-p8VrCRWVkSs/AAAAAAAAAAI/AAAAAAAAAAA/07W32axYdIQ/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCPbarqIiSsjtnf3lth1Andg/',
            'fanart': 'https://yt3.ggpht.com/-ZljPy8V-kErXgBeomkNw3cn8P4tcmiaGQbgjRZgaiAnXX4mWtQegU-LGR2Iq_5LQRqqi-dXNjU=w1280'
        }
        ,
        {
            'title': 'Model Zisan',
            'icon': 'https://yt3.ggpht.com/-z953IQPTa4Q/AAAAAAAAAAI/AAAAAAAAAAA/DTjIqPrhHPs/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCbVTkIhviMBkm6bTBBssOUw/',
            'fanart': control.addonInfo('fanart')
        }
        ,
        {
            'title': 'Pantyhose4all',
            'icon': 'https://yt3.ggpht.com/-uWG3G4mhiGE/AAAAAAAAAAI/AAAAAAAAAAA/sRz5E3Lgalc/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
            'url': 'plugin://plugin.video.youtube/channel/UCFprvvanH9ThTv9zO-pjOpA/',
            'fanart': 'https://yt3.ggpht.com/b-1oT1vhkzDuCYJVvY1OS6fGgXPX9FA9PwbHCS8UNb3_OMzha6E-4o1ezA0V0nJ-AUzf_RAF4w=w1280'
        }
    ]

    for channel in channels:
        li = control.item(label=channel['title'], iconImage=channel['icon'])
        li.setArt({'fanart': channel['fanart']})
        li.addContextMenuItems([(control.lang(30006), 'RunPlugin({0}?action=addBookmark)'.format(sysaddon))])
        url = channel['url']
        isFolder = True
        menu.append((url, li, isFolder))

    control.addItems(syshandle, menu)
    control.directory(syshandle)


def playlists():

    _list = cache.get(_playlists, 24)

    for p in _list:
        p.update({'action': 'youtube'})

    for p in _list:
        bookmark = dict((k, v) for k, v in p.iteritems() if not k == 'next')
        bookmark['bookmark'] = p['url']
        bm_cm = {'title': 30006, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
        refresh = {'title': 30008, 'query': {'action': 'refresh'}}
        cache_clear = {'title': 30005, 'query': {'action': 'cache_clear'}}
        p.update({'cm': [refresh, cache_clear, bm_cm]})

    directory.add(_list)


def _youtube(plink):

    _list = cache.get(youtube.youtube(key=key).playlist, 12, plink)

    if _list is None:
        return

    for i in _list:
        i.update({'action': 'play', 'isFolder': 'False'})

    for item in _list:
        bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
        bookmark['bookmark'] = item['url']
        bm_cm = {'title': 30006, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
        refresh = {'title': 30008, 'query': {'action': 'refresh'}}
        cache_clear = {'title': 30005, 'query': {'action': 'cache_clear'}}
        item.update({'cm': [refresh, cache_clear, bm_cm]})

    directory.add(_list)


def videos():

    video_list = cache.get(item_list, 12)

    for v in video_list:
        v.update({'action': 'play', 'isFolder': 'False'})

    for item in video_list:
        bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
        bookmark['bookmark'] = item['url']
        bm_cm = {'title': 30006, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
        refresh = {'title': 30008, 'query': {'action': 'refresh'}}
        cache_clear = {'title': 30005, 'query': {'action': 'cache_clear'}}
        item.update({'cm': [refresh, cache_clear, bm_cm]})

    directory.add(video_list)


def bm_list():

    bm = bookmarks.get()

    na = [{'title': 30012, 'action': None, 'icon': 'empty.png'}]

    if not bm:
        directory.add(na)
        return na

    for item in bm:
        bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
        bookmark['delbookmark'] = item['url']
        item.update({'cm': [{'title': 30007, 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

    il = sorted(bm, key=lambda k: k['title'].lower())

    directory.add(il)


def main():

    menu = [
        {
            'title': 30001,
            'action': 'videos',
            'icon': control.addonInfo('icon')
        }
        ,
        {
            'title': 30002,
            'action': 'playlists',
            'icon': 'playlists.png'
        }
        ,
        {
            'title': 30003,
            'action': 'bookmarks',
            'icon': 'bookmarks.png'
        }
        ,
        {
            'title': 30013,
            'action': 'third_party',
            'icon': 'channels.png'
        }
        ,
        {
            'title': 30004,
            'action': 'settings',
            'icon': 'settings.png'
        }
    ]

    if control.setting('third_party') == 'false':
        del menu[-2]

    cc = {'title': 30005, 'query': {'action': 'cache_clear'}}

    for item in menu:
        item.update({'cm': [cc]})

    directory.add(menu)

########################################################################################################################

if action is None:

    if control.setting('warning') == 'true':
        if control.yesnoDialog(
                heading=control.lang(30016), line1=control.lang(30017), line2='', line3='',
                yeslabel=control.lang(30018), nolabel=control.lang(30019)
        ):
            if control.setting('first_time') == 'true':
                control.setSetting('warning', 'false')
            else:
                control.setSetting('warning', 'true')
            main()
        else:
            import sys
            sys.exit()
    else:
        main()

elif action == 'videos':

    videos()

elif action == 'play':

    directory.resolve(url)

elif action == 'refresh':

    control.refresh()

elif action == 'playlists':

    playlists()

elif action == 'youtube':

    _youtube(url)

elif action == 'third_party':

    third_party()

elif action == 'bookmarks':

    bm_list()

elif action == 'addBookmark':

    bookmarks.add(url)

elif action == 'deleteBookmark':

    bookmarks.delete(url)

elif action == 'settings':

    control.openSettings()

elif action == 'cache_clear':

    if control.yesnoDialog(line1=control.lang(30009), line2='', line3=''):

        control.deleteFile(control.cacheFile)
        control.infoDialog(control.lang(30010))

    else:

        control.infoDialog(control.lang(30011))
