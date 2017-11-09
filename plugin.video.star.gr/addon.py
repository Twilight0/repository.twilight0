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


import urlparse,sys
from resources.lib import star

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')
url = params.get('url')
image = params.get('image')
title = params.get('title')


if action is None:
    star.Indexer().root()

elif action == 'addBookmark':
    from tulip import bookmarks
    bookmarks.add(url)

elif action == 'deleteBookmark':
    from tulip import bookmarks
    bookmarks.delete(url)

elif action == 'bookmarks':
    star.Indexer().bookmarks()

elif action == 'tvshows':
    star.Indexer().tvshows()

elif action == 'web_tv':
    star.Indexer().web_tv()

elif action == 'cartoon':
    star.Indexer().cartoon()

elif action == 'archive':
    star.Indexer().archive()

elif action == 'episodes':
    star.Indexer().episodes(url, image)

elif action == 'web_episodes':
    star.Indexer().web_episodes(url)

elif action == 'youtube':
    star.Indexer().youtube(url)

elif action == 'popular':
    star.Indexer().popular()

elif action == 'news':
    star.Indexer().news()

elif action == 'play':
    star.Indexer().play(title, image, url)

elif action == 'live':
    star.Indexer().live()

elif action == 'cache_clear':
    from tulip import cache
    cache.clear(withyes=False)
