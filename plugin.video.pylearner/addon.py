# -*- coding: utf-8 -*-

"""
    PyLearner Add-on
    Author: Twilight0

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
"""

import os, sys, urlparse, urllib2
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
# noinspection PyUnresolvedReferences
import CommonFunctions as common
# import YDStreamExtractor

# Commands:
join = os.path.join
addon = xbmcaddon.Addon
language = addon().getLocalizedString
addonname = addon().getAddonInfo("name")
addonid = addon().getAddonInfo("id")
addonpath = addon().getAddonInfo("path")
addonfanart = addon().getAddonInfo("fanart")
addonicon = join(addonpath, 'icon.png')
addonmedia = join(addonpath, 'resources', 'media')

addDirItem = xbmcplugin.addDirectoryItem
addDirItems = xbmcplugin.addDirectoryItems
endDir = xbmcplugin.endOfDirectory
execute = xbmc.executebuiltin
dialog = xbmcgui.Dialog()
condVisibility = xbmc.getCondVisibility

# Handlers:
_url_ = sys.argv[0]
_handle_ = int(sys.argv[1])

params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
action = params.get('action', None)


def opener(url):

    requester = urllib2.Request(url)
    requester.add_header('User-Agent', 'Mozilla/5.0 (msie 11.0; windows nt 6.2 ; Trident/7.0; rv:11.0) like Gecko')
    response = urllib2.urlopen(requester)
    result = response.read()
    response.close()

    return result


def txt_box(heading, announce):

    window_id = 10147
    control_id1 = 1
    control_id2 = 5
    gui_window = xbmcgui.Window(window_id)

    execute('ActivateWindow(%d)' % window_id)
    xbmc.sleep(500)

    gui_window.getControl(control_id1).setLabel(heading)

    try:
        txt = open(announce)
        text = txt.read()

    except:
        text = announce

    gui_window.getControl(control_id2).setText(str(text))

    return


def cheat_sheet(cs_link):

    raw = opener(cs_link)

    txt_box('Python Cheat Sheet', raw)


def constructor():

    main = []

    if addon().getSetting('language') == '1':
        _xml_ = opener('http://alivegr.net/raw/pylearner-el.xml')
    else:
        _xml_ = opener('http://alivegr.net/raw/pylearner.xml')

    result = common.parseDOM(_xml_, 'item')

    for item in result:
        title = common.parseDOM(item, 'title')
        icon = common.parseDOM(item, 'icon')
        url = common.parseDOM(item, 'url')
        tp = common.parseDOM(item, 'type')

        item_data = ({'title': '[COLOR white]' + title[0] + '[/COLOR]'.replace('&amp;', '&'), 'icon': addonicon if icon[0] == '' else icon[0], 'url': url[0].
                     replace('https://www.youtube.com/channel', 'plugin://plugin.video.youtube/channel').
                     replace('https://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/play/?video_id='),
                     'type': str(tp).strip('[]\'u')})

        main.append(item_data)

    return main


# Build Root Menu:
def main_menu():

    execute('Container.SetViewMode(50)')

    item_list = []

    items = constructor()

    settings_url = '{0}?action=settings'.format(_url_)
    li = xbmcgui.ListItem(label='[COLOR orange]' + language(30014) + '[/COLOR]', iconImage='http://www.icon2s.com/img256/256x256-aptana-orange-settings.png')
    li.setInfo('video', {'title': '[COLOR orange]' + language(30014) + '[/COLOR]'})
    li.setArt({'fanart': addonfanart})
    addDirItem(handle=_handle_, url=settings_url, listitem=li, isFolder=True)

    for item in items:

        list_item = xbmcgui.ListItem(label=item['title'], iconImage=item['icon'])
        list_item.setInfo('video', {'title': item['title']})
        list_item.setArt({'thumb': item['icon'], 'fanart': addonfanart})

        if item['type'] == 'sep':
            url = _url_
            isFolder = False

        elif item['type'] == 'video':
            # url = item['url']
            url = '{0}?action=play&url={1}'.format(_url_, item['url'])
            isFolder = False

        elif item['type'] == 'index':
            url = item['url']
            isFolder = True

        elif item['type'] == 'pycheat':
            url = '{0}?action=pycheat&url={1}'.format(_url_, item['url'])
            isFolder = False

        else:
            url = _url_
            isFolder = False

        item_list.append((url, list_item, isFolder))

    addDirItems(_handle_, item_list)
    endDir(_handle_, cacheToDisc=False)


def youtube():

    # Please do not copy these keys, instead create your own with this tutorial:
    # http://forum.kodi.tv/showthread.php?tid=267160&pid=2299960#pid2299960

    api_keys = {
        'enablement': 'true',
        'id': '498788153161-pe356urhr0uu2m98od6f72k0vvcdsij0.apps.googleusercontent.com',
        'api_key': 'AIzaSyA8k1OyLGf03HBNl0byD511jr9cFWo2GR4',
        'secret': 'e6RBIFCVh1Fm-IX87PVJjgUu'
    }

    if addon('plugin.video.youtube').getSetting('youtube.api.enable') == 'true':
        if dialog.yesno(heading=addonname, line1=language(30007), line2=language(30008)):
            addon('plugin.video.youtube').setSetting('youtube.api.enable', api_keys['enablement'])
            addon('plugin.video.youtube').setSetting('youtube.api.id', api_keys['id'])
            addon('plugin.video.youtube').setSetting('youtube.api.key', api_keys['api_key'])
            addon('plugin.video.youtube').setSetting('youtube.api.secret', api_keys['secret'])
            dialog.notification(heading=addonname, message=language(30009), time=3000, sound=False)
        else:
            dialog.notification(heading=addonname, message=language(30010), time=3000, sound=False)
    else:
        if dialog.yesno(heading=addonname, line1=language(30013), line2=language(30008)):
            addon('plugin.video.youtube').setSetting('youtube.api.enable', api_keys['enablement'])
            addon('plugin.video.youtube').setSetting('youtube.api.id', api_keys['id'])
            addon('plugin.video.youtube').setSetting('youtube.api.key', api_keys['api_key'])
            addon('plugin.video.youtube').setSetting('youtube.api.secret', api_keys['secret'])
            dialog.notification(heading=addonname, message=language(30009), time=3000, sound=False)
        else:
            dialog.notification(heading=addonname, message=language(30010), time=3000, sound=False)



# def play_item(path, name, icon):
#
#     plot = """Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.
#     Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.
#     The language provides constructs intended to enable writing clear programs on both a small and large scale.
#     Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles.
#     It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.
#     Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems.
#     Using third-party tools, such as Py2exe or Pyinstaller, Python code can be packaged into stand-alone executable programs for some of the most popular operating systems, so Python-based software can be distributed to, and used on, those environments with no need to install a Python interpreter.
#     Above description was taken from wikipedia: https://en.wikipedia.org/wiki/Python_(programming_language)"""
#
#     list_item = xbmcgui.ListItem(path=path)
#     list_item.setInfo('video', {'title': name, 'plot': plot})
#     list_item.setArt({'thumb': icon})
#     xbmcplugin.setResolvedUrl(_handle_, True, listitem=list_item)

if action is None:

    main_menu()

elif action == 'play':

    execute('PlayMedia("{0}")'.format(params['url']))

#     stream = YDStreamExtractor.getVideoInfo(params['url'])
#     url = stream.streamURL()
#     title = stream.selectedStream()['title']
#     thumb = stream.selectedStream()['thumbnail']
#     #plot = stream.selectedStream()['description']
#     play_item(url, title, thumb)

elif action == 'pycheat':

    cheat_sheet(params['url'])

elif action == 'youtube':

    youtube()

elif action == 'settings':

    addon().openSettings()
