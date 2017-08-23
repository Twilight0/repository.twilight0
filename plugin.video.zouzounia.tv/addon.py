# -*- coding: utf-8 -*-

'''
    Zouzounia TV Addon
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

main_id = 'UCzsQf6eiWz4gIHgx0oYadXA'
key = b64decode('QUl6YVN5QThrMU95TEdmMDNIQk5sMGJ5RDUxMWpyOWNGV28yR1I0')  # please do not copy this key


def item_list():
    return youtube.youtube(key=key).videos(main_id)


def _playlists():
    return youtube.youtube(key=key).playlists(main_id)


def third_party():

    menu = []

    channels = [
        {
         'title': 'Πειραχτίρια TV',
         'icon': 'https://yt3.ggpht.com/-tS9HnznNzaE/AAAAAAAAAAI/AAAAAAAAAAA/NaBbviI2fOk/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCnIEDKNRPQAsxU8gu0QqkaQ/'
        }
        ,
        {
         'title': 'Παιδικό Κανάλι',
         'icon': 'https://yt3.ggpht.com/-1El1TLf3hlg/AAAAAAAAAAI/AAAAAAAAAAA/hUoR927dsaE/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCp_UGBizEZEoHJlS71ninSA/'
        }
        ,
        {
         'title': 'Kids Channel Network',
         'icon': 'https://yt3.ggpht.com/-dR8D36X4sVM/AAAAAAAAAAI/AAAAAAAAAAA/TUV7N3Dg0CM/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCStBCJIgxvUXaggTo2C8ZQg/'
        }
        ,
        {
         'title': 'Παιδικά τραγούδια με στίχους',
         'icon': 'https://yt3.ggpht.com/-Jdrq5I2r5Tc/AAAAAAAAAAI/AAAAAAAAAAA/z7IPqFS7jqA/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCyENiZwRYzfXzbwP-Mxk9oA/'
        }
        ,
        {
         'title': 'Disney Greece',
         'icon': 'https://yt3.ggpht.com/-ONfYC2gl1wI/AAAAAAAAAAI/AAAAAAAAAAA/wURaWHLOI3k/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCy84vrlfPcEniv1wuyTr3fw/'
        }
    ]

    for channel in channels:
        li = control.item(label=channel['title'], iconImage=channel['icon'])
        li.setArt({'fanart': control.addonInfo('fanart')})
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

    # for i in video_list:
    #     i.update({'nextlabel': 30017, 'nextaction': 'videos'})

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

    na = [{'title': 30012, 'action': None, 'icon': 'not-found.jpg'}]

    if not bm:
        directory.add(na)
        return na

    for item in bm:
        bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
        bookmark['delbookmark'] = item['url']
        item.update({'cm': [{'title': 30007, 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

    _list = sorted(bm, key=lambda k: k['title'].lower())

    directory.add(_list)


def main():

    menu = [
        {
            'title': 30001,
            'action': 'videos',
            'icon': 'videos.jpg'
        }
        ,
        {
            'title': 30002,
            'action': 'playlists',
            'icon': 'playlists.jpg'
        }
        ,
        {
            'title': 30003,
            'action': 'bookmarks',
            'icon': 'heart.jpg'
        }
        ,
        {
            'title': 30013,
            'action': 'third_party',
            'icon': '3rd_party.jpg'
        }
        ,
        {
            'title': 30004,
            'action': 'settings',
            'icon': 'settings.jpg'
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
