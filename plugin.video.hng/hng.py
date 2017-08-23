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

main_id = 'UCdiTNAd8yrUcRaOEotk6oww'
ost = 'PLZF-_NNdxpb4FKRLZ7Z_VTe4ii_ObKyoC'
key = b64decode('QUl6YVN5QThrMU95TEdmMDNIQk5sMGJ5RDUxMWpyOWNGV28yR1I0')  # please do not copy this key


def item_list(id=main_id):
    return youtube.youtube(key=key).videos(id)


def _playlists(id=main_id):
    return youtube.youtube(key=key).playlists(id)


def third_party():

    menu = []

    channels = [
        {
         'title': 'Kotton Gamer',
         'icon': 'https://yt3.ggpht.com/-INHVBEYrqPs/AAAAAAAAAAI/AAAAAAAAAAA/KIxzHZaoLAE/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCuVsAtrhly8r38slgKYihqw/'
        },
        {
         'title': 'Atway',
         'icon': 'https://yt3.ggpht.com/-ndqPynNZhng/AAAAAAAAAAI/AAAAAAAAAAA/_1t_ZtmICKs/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UC80K82TkjjQ-mauzncjTxeQ/'
        },
        {
         'title': 'Luftangreifer',
         'icon': 'https://yt3.ggpht.com/-2cqx9aLhEaE/AAAAAAAAAAI/AAAAAAAAAAA/DNMsGKqVzek/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCaX0s3rQjI4fZYli4G0YwNA/playlist/PLZhVK1RzI0ZIx6fF7szLnfC62ZgazoTYK/'
        },
        {
         'title': 'Schilli',
         'icon': 'https://yt3.ggpht.com/-6ZZ8Y18Vow4/AAAAAAAAAAI/AAAAAAAAAAA/GKc2Q-Hij5w/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UC4AAJlFH9Pl0vj0hlF5M9bQ/'
        },
        {
         'title': 'Ignitation',
         'icon': 'https://yt3.ggpht.com/-bjbqCx0kGvY/AAAAAAAAAAI/AAAAAAAAAAA/bJfBTiVyPOQ/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UC9xyLaJGLBOZ81r4bvp7VfQ/'
        },
        {
         'title': 'Nemesis 073',
         'icon': 'https://yt3.ggpht.com/-D_kVdH4dBdI/AAAAAAAAAAI/AAAAAAAAAAA/nagGMSVcYOY/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/channel/UCWWu23gFvqP6_gGz8ZTJkeg/'
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

    na = [{'title': 30012, 'action': None, 'icon': 'camouflage.jpg'}]

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
            'icon': 'pointerquickfire.jpg'
        }
        ,
        {
            'title': 30002,
            'action': 'playlists',
            'icon': 'tightgrip.jpg'
        }
        ,
        {
            'title': 30016,
            'action': 'youtube',
            'url': ost,
            'icon': 'ghillie.jpg'
        }
        ,
        {
            'title': 30003,
            'action': 'bookmarks',
            'icon': 'marathonman.jpg'
        }
        ,
        {
            'title': 30013,
            'action': 'third_party',
            'icon': 'scavenger.jpg'
        }
        ,
        {
            'title': 30004,
            'action': 'settings',
            'icon': 'mechanic.jpg'
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
