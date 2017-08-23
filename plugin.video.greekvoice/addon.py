# -*- coding: utf-8 -*-

"""
    Greek Voice Add-on
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

from tulip import control, directory, client
from resources.lib import action, sysaddon, syshandle, url


lc = [
    {
        'title': 'Greek Voice',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV1_icon.png'),
        'url': 'http://wpso.com:1936/hls/wzra.m3u8',
        'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV_TV1_fanart.jpg'),
        'plot': 'Greek Voice 1'.decode('utf-8')
    }
    ,
    # {
    #     'title': 'Greek Voice 2',
    #     'icon': join(addonmedia, 'GV2_icon.png'),
    #     'url': 'http://stream.ssh101.com:1935/live/greekvoice/playlist.m3u8',
    #     'fanart': join(addonmedia, 'GV_TV2_fanart.jpg'),
    #     'plot': 'Greek Voice 2'.decode('utf-8')
    # }
    # ,
    {
        'title': 'TILEMOUSIKI 1 SD',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='TILEMOUSIKI1SD.png'),
        'url': 'mmsh://wpso.com:200/music',
        'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='TILEMOUSIKI_fanart.jpg'),
        'plot': 'Εκπέμπει Παλαιά Τραγούδια και κονσέρτα σε ποιότητα SD'.decode('utf-8')
    }
    ,
    {
        'title': 'TILEMOUSIKI 2 HD',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='TILEMOUSIKI2HD.png'),
        'url': 'http://wpso.com:1936/hls/music.m3u8',
        'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='TILEMOUSIKI_fanart.jpg'),
        'plot': 'Μουσικό κανάλι εκπέμπει 24/7 σε σύστημα HD'.decode('utf-8')
    }
    ,
    {
        'title': 'WZRA KIDS 1',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='WZRA_KIDS_icon.png'),
        'url': 'mmsh://wpso.com:200/kids',
        'fanart': control.addonInfo('fanart'),
        'plot': 'Παιδικό Κανάλι 24/7'.decode('utf-8')
    }
    ,
    {
        'title': 'WZRA KIDS 2',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='WZRA_KIDS_icon.png'),
        'url': 'http://wpso.com:1936/hls/kidshd.m3u8',
        'fanart': control.addonInfo('fanart'),
        'plot': 'Παιδικό Κανάλι 24/7'.decode('utf-8')
    }
    ]


rc = [
    {
        'title': 'WPSO Greek Voice Radio',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='wpso_icon.png'),
        'url': 'http://wpso.com:8000/',
        'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV_Radio_fanart.jpg'),
        'plot': 'Ραδιοφωνικός σταθμός Φωνή Των Ελλήνων, παγκοσμία κάλυψη'.decode('utf-8')
    }
    ,
    {
        'title': 'WXYB Radio GR IT ES',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='wxyb_icon.png'),
        'url': 'http://wpso.com:7071/',
        'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV_Radio_fanart.jpg'),
        'plot': 'Radio WXYB 1520Khz Greek Italian & Spanish'
    }
    ,
    {
        'title': 'XAMOS Youth Radio',
        'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='xamos_icon.png'),
        'url': 'http://xamosam.com:9050',
        'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='xamos_fanart.jpg'),
        'plot': 'XAMOS Youth Radio 1500 KHz AM'
    }
]

##########################################
                                         #
channel_id = 'UC0HzJJlSxjhhN4OAXHHQIOg'  #
                                         #
##########################################


# Build Root Menu:
def main_menu():

    menu = []

    menu_items = [
            {
                'title': control.lang(30001),
                'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='television.png'),
                'url': '{0}?action={1}'.format(sysaddon, 'live'),
                'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV_TV2_fanart.jpg')
            }
            ,
            {
                'title': control.lang(30002),
                'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='radio.png'),
                'url': '{0}?action={1}'.format(sysaddon, 'radio'),
                'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='TILEMOUSIKI_fanart.jpg')
            }
            ,
            {
                'title': control.lang(30014),
                'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV_YT_icon.png'),
                'url': 'plugin://plugin.video.youtube/channel/{0}/'.format(channel_id),
                'fanart': control.addonmedia(addonid='script.greekvoice.artwork', icon='GV_TV2_fanart.jpg')
            }
            ,
            {
                'title': control.lang(30004),
                'icon': control.addonmedia(addonid='script.greekvoice.artwork', icon='settings.png'),
                'url': '{0}?action={1}'.format(sysaddon, 'settings'),
                'fanart': control.addonInfo('fanart')
            }
    ]

    for item in menu_items:
        li = control.item(label=item['title'], iconImage=item['icon'], thumbnailImage=item['icon'])
        li.setInfo('video', {'title': item['title']})
        li.setArt({'fanart': item['fanart']})
        _url = item['url']
        if item['url'].endswith('settings'):
            _isFolder = False
        else:
            _isFolder = True
        menu.append((_url, li, _isFolder))

    control.addItems(syshandle, menu)
    control.directory(syshandle)


def constructor(channels):

    menu = []

    for item in channels:

        li = control.item(label=item['title'], iconImage=item['icon'], thumbnailImage=item['icon'])
        li.setInfo('video', {'title': item['title'], 'plot': item['plot']})
        li.setArt({'fanart': item['fanart']})
        li.setProperty('IsPlayable', 'true')
        _url = '{0}?action=play&url={1}'.format(sysaddon, item['url'])
        _isFolder = False
        menu.append((_url, li, _isFolder))

    control.addItems(syshandle, menu)
    control.directory(syshandle)


def txt_box(heading, announce):

    window_id = 10147
    control_id1 = 1
    control_id2 = 5
    gui_window = control.window(window_id)

    control.execute('ActivateWindow(%d)' % window_id)
    control.sleep(200)

    gui_window.getControl(control_id1).setLabel(heading)

    gui_window.getControl(control_id2).setText(announce)


def guide():

    raw = client.request('http://pastebin.com/raw/8euL4fNM')

    txt_box('Greek Voice TV Guide', raw)


def youtube():

    # Please do not copy these keys, instead create your own with this tutorial:
    # http://forum.kodi.tv/showthread.php?tid=267160&pid=2299960#pid2299960

    api_keys = {
        'enablement': 'true',
        'id': '498788153161-pe356urhr0uu2m98od6f72k0vvcdsij0.apps.googleusercontent.com',
        'api_key': 'AIzaSyA8k1OyLGf03HBNl0byD511jr9cFWo2GR4',
        'secret': 'e6RBIFCVh1Fm-IX87PVJjgUu'
    }

    def seq():
        control.addon('plugin.video.youtube').setSetting('youtube.api.enable', api_keys['enablement'])
        control.addon('plugin.video.youtube').setSetting('youtube.api.id', api_keys['id'])
        control.addon('plugin.video.youtube').setSetting('youtube.api.key', api_keys['api_key'])
        control.addon('plugin.video.youtube').setSetting('youtube.api.secret', api_keys['secret'])
        control.dialog.notification(heading=control.addonInfo('name'), message=control.lang(30009), time=3000, sound=False)

    def cancelled():
        return control.dialog.notification(heading=control.addonInfo('name'), message=control.lang(30010), time=3000, sound=False)

    if control.addon('plugin.video.youtube').getSetting('youtube.api.enable') == 'true':
        if control.dialog.yesno(heading=control.addonInfo('name'), line1=control.lang(30007), line2=control.lang(30008)):
            seq()
        else:
            cancelled()
    else:
        if control.dialog.yesno(heading=control.addonInfo('name'), line1=control.lang(30011), line2=control.lang(30008)):
            seq()
        else:
            cancelled()


if action is None:

    main_menu()

elif action == 'live':

    constructor(lc)

elif action == 'radio':

    constructor(rc)

elif action == 'play':

    directory.resolve(url)

elif action == 'guide':

    guide()

elif action == 'settings':

    control.Settings()

elif action == 'youtube':

    youtube()
