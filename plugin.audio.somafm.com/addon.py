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

from resources.lib.modules import action, url, text

########################################################################################################################

if action is None:

    from resources.lib.indexers import radios

    radios.Indexer().stations()

########################################################################################################################

elif action == 'play':

    from resources.lib.modules.player import player

    player(url)

elif action == 'switcher':

    from resources.lib.indexers import radios

    radios.Indexer().switcher()

# elif action == 'description':
#
#     from resources.lib.modules import text_viewer
#
#     text_viewer.description(text)

elif action == 'history':

    from resources.lib.modules import text_viewer

    text_viewer.history(url)

elif action == 'cache_clear':

    from tulip import cache

    cache.clear(withyes=False)

elif action == 'refresh':

    from tulip import control

    control.refresh()
