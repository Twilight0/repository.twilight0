# -*- coding: utf-8 -*-

"""
    Greek TV Add-on
    Author: Thgiliwt

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

import urlparse, random
import xbmcaddon, xbmcgui, xbmcplugin, xbmc
import client
from __init__ import sysaddon, syshandle, params

addon = xbmcaddon.Addon()
localisedstr = addon.getLocalizedString
addonname = addon.getAddonInfo("name")
addonpath = addon.getAddonInfo("path").decode('utf-8')
addonfanart = addon.getAddonInfo("fanart")
addonicon = addon.getAddonInfo("icon")
addonid = addon.getAddonInfo("id")

dialog = xbmcgui.Dialog()

addDirItems = xbmcplugin.addDirectoryItems
addDirItem = xbmcplugin.addDirectoryItem
endDir = xbmcplugin.endOfDirectory

execute = xbmc.executebuiltin

action = params.get('action', None)
url = params.get('url')

##########################################################
main_url = 'http://www.fittube.tv/fittube/user_video/'   #
##########################################################

item_list = []


def root():

    extracted = []

    source = client.request(main_url)

    links = client.parseDOM(source, 'a', ret='href')

    urls = [link for link in links if link not in ['/fittube/', 'video_image/']]

    for url in urls:
        extracted.append(urlparse.urljoin(main_url, url))

    if addon.getSetting('order') == '0':
        return sorted(extracted)
    else:
        return sorted(extracted, key=lambda x: random.random())


def items_list(list_):

    for index, item in enumerate(list_):

        if addon.getSetting('filenames') == 'true':
            li = xbmcgui.ListItem(label=item.partition('_video/')[2], iconImage=addonicon)
        else:
            li = xbmcgui.ListItem(label='Random fitness video #' + str(1 + index), iconImage=addonicon)

        li.setInfo('video', {'title': item.partition('_video/')[2]})
        li.setArt({'thumb': addonicon, 'fanart': addonfanart})
        li.setProperty('IsPlayable', 'true')
        _url_ = '{0}?action=play&url={1}'.format(sysaddon, item)
        isFolder = False
        item_list.append((_url_, li, isFolder))

    addDirItems(handle=syshandle, items=item_list)
    endDir(syshandle, cacheToDisc=True)


def main():

    choices = ['List All videos', 'Pick a random video', 'Compile a playlist with "n" number of random videos', 'Addon Settings']

    choice = dialog.select('Please make a choice', choices)

    if choice == 0:

        items_list(root())

    elif choice == 1:

        execute('PlayMedia("{0}")'.format(random.choice(root())))

    elif choice == 2:

        def picker(seq):

            from functools import partial
            return partial(random.choice, seq)

        number = dialog.numeric(0, heading='How many random videos do you wanted to get picked?')

        list_ = [picker(root())() for item in range(int(number))]

        items_list(list_)

    elif choice == 3:

        addon.openSettings()

    else:

        execute('Dialog.Close(all)')


def play_item(path):

    li = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(syshandle, True, listitem=li)


if action is None:

    main()

elif action == 'play':

    play_item(url)
