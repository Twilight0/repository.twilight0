# -*- coding: utf-8 -*-

"""
    SomaFM Add-on
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

from tulip import directory, control, client
import json, re


ttz = 'MP3 320k'
tfs = 'MP3 256k'
ont = 'MP3 192k'
ote = 'MP3 128k'

aac1 = 'AAC 128k'
aac2 = 'AAC 64k'
aac3 = 'AAC 32k'


def selector(qofs, lofs, quality=ote):

    idx = qofs.index(quality)
    stream = lofs.pop(idx)

    return stream


def player(url):

    qofs = []

    lofs = json.loads(url)

    for item in lofs:

        if '320' in item:
            item = ttz
        elif '256' in item:
            item = tfs
        elif '192' in item:
            item = ont
        elif '130' in item:
            item = aac1
        elif '64' in item:
            item = aac2
        elif '32' in item:
            item = aac3
        else:
            item = ote

        qofs.append(item)

    if control.setting('quality_selector') == '0':

        choice = control.selectDialog(heading='Select quality', list=qofs)

        if choice <= len(lofs) and not choice == -1:

            link = lofs.pop(choice)

            stream = client.request(link)
            stream = re.findall('File1=([\w:\./-]*)', stream)[0]

            directory.resolve(stream)

        else:

            control.execute('Playlist.Clear')
            control.sleep(50)
            control.execute('Dialog.Close(all)')

    elif control.setting('quality_selector') == '1':

        stream = client.request(selector(qofs, lofs))
        stream = re.findall('File1=([\w:\./-]*)', stream)[0]
        directory.resolve(stream)

    elif control.setting('quality_selector') == '2':

        if 'MP3 320k' in qofs:
            stream = client.request(selector(qofs, lofs, ttz))
        elif 'MP3 256k' in qofs:
            stream = client.request(selector(qofs, lofs, tfs))
        elif 'MP3 192k' in qofs:
            stream = client.request(selector(qofs, lofs, ont))
        else:
            stream = client.request(selector(qofs, lofs))

        stream = re.findall('File1=([\w:\./-]*)', stream)[0]
        directory.resolve(stream)

    elif control.setting('quality_selector') == '3':

        stream = client.request(selector(qofs, lofs))
        stream = re.findall('File1=([\w:\./-]*)', stream)[0]
        directory.resolve(stream)

    elif control.setting('quality_selector') == '4':

        if 'AAC 128k' in qofs:
            stream = client.request(selector(qofs, lofs, aac1))
        elif 'AAC 64k' in qofs:
            stream = client.request(selector(qofs, lofs, aac2))
        elif 'AAC 32k' in qofs:
            stream = client.request(selector(qofs, lofs, aac3))
        else:
            stream = selector(qofs, lofs)

        stream = re.findall('File1=([\w:\./-]*)', stream)[0]
        directory.resolve(stream)

    elif control.setting('quality_selector') == '5':

        if 'AAC 128k' in qofs:
            stream = client.request(selector(qofs, lofs, aac3))
        elif 'AAC 64k' in qofs:
            stream = client.request(selector(qofs, lofs, aac2))
        elif 'AAC 32k' in qofs:
            stream = client.request(selector(qofs, lofs, aac1))
        else:
            stream = selector(qofs, lofs)

        stream = re.findall('File1=([\w:\./-]*)', stream)[0]
        directory.resolve(stream)

    else:

        selector(qofs, lofs)