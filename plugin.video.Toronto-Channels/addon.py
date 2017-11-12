# -*- coding: utf-8 -*-

"""
    Toronto-Channels Add-on
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

import os, sys, urlparse
import xbmcaddon, xbmcgui, xbmcplugin, xbmc, xbmcvfs
from resources.lib.url_opener import open_url

# Addon variables:
join = os.path.join
addon = xbmcaddon.Addon()
language = addon.getLocalizedString
addonname = addon.getAddonInfo("name")
addonid = addon.getAddonInfo("id")
addonpath = addon.getAddonInfo("path")
addonfanart = addon.getAddonInfo("fanart")
addItem = xbmcplugin.addDirectoryItem
endDir = xbmcplugin.endOfDirectory
transpath = xbmc.translatePath
datapath = transpath(addon.getAddonInfo("profile")).decode("utf-8")
dialog = xbmcgui.Dialog()
infoLabel = xbmc.getInfoLabel
fp = infoLabel('Container.FolderPath')
player = xbmc.Player().play

# Misc variables:
addonicon = join(addonpath, 'icon.png')
addonart = join(addonpath, 'resources/media')
NETVToronto_img = join(addonart, 'NETV_Toronto.png')
NETVToronto_2_img = join(addonart, 'NETV_Toronto_2.png')
Cannali_img = join(addonart, 'CANNALI_WEB_MUSIC.png')
Melodia_img = join(addonart, 'RADIO_MELODIA_TORONTO.png')
Life_img = join(addonart, 'LIFEHD.png')
Eugo24_img = join(addonart, 'EUGO24.png')
Settings_img = join(addonart, 'settings.png')
Voice_img = join(addonart, 'mag_thumb.jpg')


# Links:
if addon.getSetting('hls') == 'false':

    NETVToronto_url = 'rtmp://live.netvtoronto.com/NetvToronto/NetvToronto'
    NETV_Toronto_2_url = 'rtmp://162.219.176.210/live/eugo242017p1a'
    Eugo24_url = 'rtmp://162.219.176.210:18935/live/eugo242017p1a'
    Cannali_url = 'rtmp://live.streams.ovh/cannali/cannali'
    Life_url = 'rtmp://live.streams.ovh:1935/LIFEHD/LIFEHD'

else:

    NETVToronto_url = 'http://live.netvtoronto.com:1935/NetvToronto/NetvToronto/playlist.m3u8'
    NETV_Toronto_2_url = 'http://162.219.176.210/live/eugo242017p1a/playlist.m3u8'
    Eugo24_url = 'http://162.219.176.210:18935/live/eugo242017p1a/playlist.m3u8'
    Cannali_url = 'http://live.streams.ovh:1935/cannali/cannali/playlist.m3u8'
    Life_url = 'http://live.streams.ovh:1935/LIFEHD/LIFEHD/playlist.m3u8'

Melodia_url = 'http://149.202.208.214:9086/live'
YT_Channel = 'UCKXFDK9dRGcnwr7mWmzoY2w'
YT_Doc_playlist = 'http://alivegr.net/raw/docs.m3u'
base_url = 'http://alivegr.net/bci_mags/'
index_url = urlparse.urljoin(base_url, 'index.txt')

# Handlers:
sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])
params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
action = params.get('action', None)
url = params.get('url')


def play_item(path):

    li = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(syshandle, True, listitem=li)


def play_docs():

    from random import randint
    integer = randint(0, 1054)

    xbmc.executebuiltin('PlayMedia({0},playoffset={1})'.format(YT_Doc_playlist, integer))


def mags_index():

    xbmcplugin.setContent(syshandle, 'images')

    index_txt = open_url(index_url)

    splitted = index_txt.splitlines()

    magazines = []

    for line in splitted:

        title = line.replace('Volume', language(30025))

        image = line.partition(' - ')[0].replace('Volume ', 'vol')
        image = urlparse.urljoin(base_url, image + '/thumbs' + '/page-01.jpg')

        url = '{0}?action=mag_index&url={1}'.format(sysaddon, image.partition('/thumbs')[0])

        data = {'title': title, 'image': image, 'url': url}

        magazines.append(data)

    for mag in magazines:

        li = xbmcgui.ListItem(label=mag['title'], iconImage=mag['image'])
        li.setArt({'poster': mag['image'], 'thumb': mag['image'], 'fanart': addonfanart})
        li.setInfo('image', {'title': mag['title'], 'picturepath': mag['url']})
        url = mag['url']
        isFolder = True

        xbmcplugin.addDirectoryItem(syshandle, url, li, isFolder)

    xbmcplugin.endOfDirectory(syshandle)


def mag_index(url):

    number = int(open_url(url + '/pages'))

    pages = []

    for page in range(1, number + 1):

        string = str(page)

        title = language(30026) + ' ' + string

        if len(string) == 2:
            image = url + '/thumbs' + '/page-' + string + '.jpg'
            link = url + '/' + string + '.jpg'
        else:
            image = url + '/thumbs' + '/page-' + '0' + string + '.jpg'
            link = url + '/' + '0' + string + '.jpg'

        data = {'title': title, 'image': image, 'url': link}
        pages.append(data)

    for selida in pages:

        li = xbmcgui.ListItem(label=selida['title'], iconImage=selida['image'])
        li.setArt({'poster': selida['image'], 'thumb': selida['image'], 'fanart': addonfanart})
        li.setInfo('image', {'title': selida['title'], 'picturepath': selida['url']})
        path = selida['url']
        isFolder = False

        xbmcplugin.addDirectoryItem(syshandle, path, li, isFolder)

    xbmcplugin.endOfDirectory(syshandle)


def main_menu():

    xbmcplugin.setContent(syshandle, 'movies')

    # NETV Toronto
    if addon.getSetting('netv') == 'true':
        url1 = '{0}?action=play&url={1}'.format(sysaddon, NETVToronto_url)
        li1 = xbmcgui.ListItem(label='NETV Toronto', iconImage=NETVToronto_img)
        li1.setArt({'poster': NETVToronto_img, 'thumb': NETVToronto_img, 'fanart': addonfanart})
        li1.setInfo('video', {'title': 'NETV Toronto', 'plot': language(30006), 'genre': 'Live'})
        li1.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url1, listitem=li1, isFolder=False)
    elif addon.getSetting('netv') == 'false':
        pass

    # NETV Toronto 2
    if addon.getSetting('netv2') == 'true':
        # url2 = '{0}?action=play&url={1}'.format(sysaddon, NETV_Toronto_2_url)
        url2 = '{0}?action=play_docs'.format(sysaddon)
        li2 = xbmcgui.ListItem(label='NETV Toronto 2', iconImage=NETVToronto_2_img)
        li2.setArt({'poster': NETVToronto_2_img, 'thumb': NETVToronto_2_img, 'fanart': addonfanart})
        li2.setInfo('video', {'title': 'NETV Toronto 2', 'plot': language(30019), 'genre': 'Live'})
        li2.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url2, listitem=li2, isFolder=False)
    elif addon.getSetting('netv2') == 'false':
        pass

    # Eugo24
    if addon.getSetting('eugo24') == 'true':
        url3 = '{0}?action=play&url={1}'.format(sysaddon, Eugo24_url)
        li3 = xbmcgui.ListItem(label='Eugo24', iconImage=Eugo24_img)
        li3.setArt({'poster': Eugo24_img, 'thumb': Eugo24_img, 'fanart': addonfanart})
        li3.setInfo('video', {'title': 'Eugo24', 'plot': language(30021), 'genre': 'Live'})
        li3.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url3, listitem=li3, isFolder=False)
    elif addon.getSetting('eugo24') == 'false':
        pass

    # Life HD
    if addon.getSetting('life') == 'true':
        url4 = '{0}?action=play&url={1}'.format(sysaddon, Life_url)
        li4 = xbmcgui.ListItem(label='Life HD', iconImage=Life_img)
        li4.setArt({'poster': Life_img, 'thumb': Life_img, 'fanart': addonfanart})
        li4.setInfo('video', {'title': 'Life HD', 'plot': language(30008), 'genre': 'Live'})
        li4.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url4, listitem=li4, isFolder=False)
    elif addon.getSetting('life') == 'false':
        pass

    # Cannali Music
    if addon.getSetting('cannali') == 'true':
        url5 = '{0}?action=play&url={1}'.format(sysaddon, Cannali_url)
        li5 = xbmcgui.ListItem(label='CANNALI Music', iconImage=Cannali_img)
        li5.setArt({'poster': Cannali_img, 'thumb': Cannali_img, 'fanart': addonfanart})
        li5.setInfo('video', {'title': 'CANNALI Music', 'plot': language(30007), 'genre': 'Live'})
        li5.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url5, listitem=li5, isFolder=False)
    elif addon.getSetting('cannali') == 'false':
        pass

    # Youtube Channel
    if addon.getSetting('youtube') == 'true':
        url5 = 'plugin://plugin.video.youtube/channel/{0}/'.format(YT_Channel)
        li5 = xbmcgui.ListItem(label='Youtube Channel', iconImage=addonicon)
        li5.setArt({'poster': addonicon, 'thumb': addonicon, 'fanart': addonfanart})
        addItem(handle=syshandle, url=url5, listitem=li5, isFolder=True)
    elif addon.getSetting('youtube') == 'false':
        pass

    # Radio Melodia Toronto
    if addon.getSetting('melodia') == 'true':
        url6 = '{0}?action=play&url={1}'.format(sysaddon, Melodia_url)
        li6 = xbmcgui.ListItem(label='Radio Melodia Toronto', iconImage=Melodia_img)
        li6.setArt({'poster': Melodia_img, 'thumb': Melodia_img, 'fanart': addonfanart})
        li6.setInfo('music', {'title': 'Radio Melodia Toronto', 'comment': language(30009), 'genre': 'Live'})
        li6.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url6, listitem=li6, isFolder=False)
    elif addon.getSetting('melodia') == 'false':
        pass

    # Voice Life & Style
    if addon.getSetting('voice') == 'true':
        url7 = '{0}?action={1}'.format(sysaddon, 'mags_addon')
        li7 = xbmcgui.ListItem(label='Voice Life & Style Mag', iconImage=Voice_img)
        li7.setArt({'poster': Voice_img, 'thumb': Voice_img, 'fanart': addonfanart})
        li7.setInfo('image', {'title': 'Voice Life & Style', 'picturepath': Voice_img})
        addItem(handle=syshandle, url=url7, listitem=li7, isFolder=False)
    elif addon.getSetting('voice') == 'false':
        pass

    # Settings
    settings_url = '{0}?action=settings'.format(sysaddon)
    settings_li = xbmcgui.ListItem(label=language(30001), iconImage=Settings_img)
    settings_li.setArt({'thumb': Settings_img, 'fanart': addonfanart})
    addItem(handle=syshandle, url=settings_url, listitem=settings_li, isFolder=True)

    endDir(syshandle)


def setup_iptv():

    if not xbmcvfs.exists(datapath):

        xbmcvfs.mkdirs(datapath)

    iptv_folder = transpath('special://profile/addon_data/pvr.iptvsimple')

    def seq():

        xbmcvfs.copy(join(addonpath, 'resources', 'iptv', 'iptv_settings.xml'), join(iptv_folder, 'settings.xml'))
        # xbmcvfs.copy(join(addonpath, 'resources', 'iptv', 'simple-client.m3u'), join(datapath, 'simple-client.m3u'))
        iscon = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
        liveon = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
        xbmc.executeJSONRPC(iscon)
        xbmc.executeJSONRPC(liveon)
        dialog.notification(addonname, language(30015), sound=False)

    if not xbmcvfs.exists(join(iptv_folder, 'settings.xml')):

        xbmcvfs.mkdirs(iptv_folder)

        if dialog.yesno(addonname, language(30013), language(30014)):
            seq()
        else:
            dialog.notification(addonname, language(30016), sound=False)

    elif xbmcvfs.exists(join(iptv_folder, 'settings.xml')):

        if dialog.yesno(addonname, language(30013), language(30017)):
            seq()
        else:
            dialog.notification(addonname, language(30016), sound=False)


def melodia_player():

    listitem = xbmcgui.ListItem(thumbnailImage=Melodia_img)
    listitem.setInfo('music', {'title': 'Radio Melodia Toronto', 'genre': 'Greek Music'})
    player(item=Melodia_url, listitem=listitem)


def mags_addon():

    xbmc.executebuiltin('ActivateWindow(pictures,"plugin://plugin.video.Toronto-Channels/?content_type=image",return)')


def keymap_edit():

    location = transpath(join('special://profile', 'keymaps', 'tc.xml'))

    def seq():

        string_start = '<keymap><slideshow><mouse>'
        string_end = '</mouse></slideshow></keymap>'
        string_for_left = '<leftclick>NextPicture</leftclick>'
        string_for_right = '<rightclick>PreviousPicture</rightclick>'
        string_for_middle = '<middleclick>Rotate</middleclick>'
        string_for_up = '<wheelup>ZoomIn</wheelup>'
        string_for_down = '<wheeldown>ZoomOut</wheeldown>'

        strings = [string_for_left, string_for_right, string_for_middle, string_for_up, string_for_down]

        map_left = language(30031)
        map_right = language(30032)
        map_middle = language(30033)
        map_up = language(30034)
        map_down = language(30035)

        keys = [map_left, map_right, map_middle, map_up, map_down]

        dialog.ok(addonname, language(30030))

        indices = dialog.multiselect(addonname, keys)

        if not indices:

            dialog.notification(addonname, language(30036), time=3, sound=False)

        else:

            finalized = []

            for i in indices:
                finalized.append(strings[i])

            joined = ''.join(finalized)

            to_write = string_start + joined + string_end

            with open(location, 'w') as f:
                f.write(to_write)

            xbmc.executebuiltin('Action(reloadkeymaps)')

            dialog.notification(addonname, language(30015), sound=False)

    yes = dialog.yesno(addonname, language(30028), language(30014))

    if yes:

        if xbmcvfs.exists(location):

            choices = [language(30038), language(30039)]

            choice = dialog.select(language(30037), choices)

            if choice == 0:

                seq()

            elif choice == 1:

                xbmcvfs.delete(location)
                xbmc.executebuiltin('Action(reloadkeymaps)')

            else:

                dialog.notification(addonname, language(30016))

        else:

            seq()

    else:

        dialog.notification(addonname, language(30016))


if action is None:

    if 'audio' in fp:
        melodia_player()
    elif 'image' in fp:
        checkpoint()
        mags_index()
    else:
        main_menu()

elif action == 'play':

    play_item(url)

elif action == 'play_docs':

    play_docs()

elif action == 'mags_index':

    mags_index()

elif action == 'mags_addon':

    mags_addon()

elif action == 'mag_index':

    mag_index(url)

elif action == 'settings':

    addon.openSettings()

elif action == 'setup_iptv':

    setup_iptv()

elif action == 'keymap_edit':

    keymap_edit()
