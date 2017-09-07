# -*- coding: utf-8 -*-

'''
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

import control, client
import re


def local(path):

    with open(path) as f:
        file_ = f.read()

    f.close()

    if not file_:

        return

    if path.endswith('.txt') or file_.startswith('true'):
        keys = file_.splitlines()[1:]
    elif path.endswith('.xml') or file_.startswith('<?xml'):
        keys = [
            client.parseDOM(file_, 'id')[0], client.parseDOM(file_, 'api_key')[0], client.parseDOM(file_, 'secret')[0]
        ]
    else:
        keys = None

    return keys


def remote(address):

    if 'pastebin' in address and not 'raw' in address:
        url = re.sub(r'(^.+?\.com/)(\w+)', r'\1raw/\2', address)
    elif 'debian' in address and not 'plain' in address:
        url = re.sub(r'(^.+?\.net/)(\w+)', r'\1plain/\2',address)
    else:
        url = address

    text = client.request(url)

    if not text:
        return

    if text.startswith('true'):
        keys = text.splitlines()[1:]
    elif text.startswith('<?xml'):
        keys = [client.parseDOM(text, 'id')[0], client.parseDOM(text, 'api_key')[0], client.parseDOM(text, 'secret')[0]]
    else:
        keys = None

    return keys


def setup(list_):

    control.addon('plugin.video.youtube').setSetting('youtube.api.enable', 'true')
    control.addon('plugin.video.youtube').setSetting('youtube.api.id', list_[0])
    control.addon('plugin.video.youtube').setSetting('youtube.api.key', list_[1])
    control.addon('plugin.video.youtube').setSetting('youtube.api.secret', list_[2])

    control.infoDialog(message=control.lang(30015), time=3000)


def wizard():

    control.addon('plugin.video.youtube').setSetting('kodion.setup_wizard', 'true')
    control.execute('RunPlugin(plugin://plugin.video.youtube/sign/out/)')


def seq():

    conditions = [
        control.addon('plugin.video.youtube').getSetting('youtube.api.enable') == 'true',
        bool(control.addon('plugin.video.youtube').getSetting('youtube.api.id')),
        bool(control.addon('plugin.video.youtube').getSetting('youtube.api.key')),
        bool(control.addon('plugin.video.youtube').getSetting('youtube.api.secret'))
    ]

    if any(conditions) and bool(control.setting('local')) or bool(control.setting('remote')):
        control.okDialog(control.addonInfo('name'), control.lang(30017))

    if not bool(control.setting('local')) and not bool(control.setting('remote')):

        result = None

    elif control.setting('local_or_remote') == '0':

        result = local(control.setting('local'))

    else:

        result = remote(control.setting('remote'))

    if not result:

        control.okDialog(control.lang(30010), control.lang(30011))

    else:

        if control.yesnoDialog(
                line1=control.lang(30012), line2='', line3='',
                yeslabel=control.lang(30013), nolabel=control.lang(30014)
        ):

            setup(result)
            if control.setting('wizard') == 'true':
                wizard()
            else:
                pass

        else:

            control.infoDialog(control.lang(30014))


def init():

    if not bool(control.setting('local')) and not bool(control.setting('remote')):

        if control.yesnoDialog(heading=control.lang(30008), line1=control.lang(30009)):
            control.openSettings()
        else:
            control.infoDialog(control.lang(30014))

    else:

        choices = [control.lang(30020), control.lang(30016), control.lang(30019)]

        selection = control.selectDialog(choices)

        if selection == 0:

            seq()

        elif selection == 1:

            control.openSettings()

        elif selection == 2:

            control.openSettings(id='plugin.video.youtube')

        else:

            pass

if __name__ == '__main__':

    init()

else:

    control.okDialog(heading=control.addonInfo('name'), line1=control.lang(30001))
