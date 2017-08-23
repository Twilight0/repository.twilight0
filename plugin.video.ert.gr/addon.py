# -*- coding: utf-8 -*-

'''
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
'''


from resources.lib import ert, action, url


if action is None:
    ert.indexer().root()

elif action == 'addBookmark':
    from tulip import bookmarks
    bookmarks.add(url)

elif action == 'deleteBookmark':
    from tulip import bookmarks
    bookmarks.delete(url)

elif action == 'channels':
    ert.indexer().channels()

elif action == 'bookmarks':
    ert.indexer().bookmarks()

elif action == 'categories':
    ert.indexer().categories()

elif action == 'episodes':
    ert.indexer().episodes(url)

elif action == 'popular':
    ert.indexer().popular()

elif action == 'live':
    ert.indexer().live(url)

elif action == 'radios':
    ert.indexer().radios()

elif action == 'radio':
    ert.indexer().radio(url)

elif action == 'district':
    ert.indexer().district()

elif action == 'play':
    ert.indexer().play(url)

elif action == 'cache_clear':
    from tulip import cache
    cache.clear(withyes=False)
