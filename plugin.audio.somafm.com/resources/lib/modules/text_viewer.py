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

from tulip import control, client
import html2text


def description(text):

    return control.dialog.textviewer('SomaFM', text)


def history(url):

    html = client.request(url)
    mid = client.parseDOM(html, 'div', attrs={'id': 'midcontent'})[0]

    h2t = html2text.HTML2Text()
    h2t.ignore_links = True
    h2t.ignore_images = True
    h2t.ignore_emphasis = True
    h2t.body_width = 300

    text = h2t.handle(mid)

    return control.dialog.textviewer('SomaFM', text)
