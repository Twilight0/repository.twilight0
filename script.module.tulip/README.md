## Script.module.tulip is a Kodi addon in the form of a module with many commonly used routines and functions that can be used to ease addon development.

It is assumed that all your artwork will be saved in resources/media folder and this argument below will be used for plugin calls:

    params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

To use it first you have to insert this line in your addon.xml, "requires" section:

    <import addon="script.module.tulip" version="1.0.1" />

Then insert these in your **default.py** (or addon.py, or whatever name of the root module is in your addon.xml):

    from tulip import "name of the module"

### Available modules:

**Bookmarks**

It provides bookmarking function within the addon. bookmarks are saved in addon's userdata folder in pysqlite database file.

_Example:_
>Root menu item:

    {'title': 'Bookmarks', 'action': 'bookmarks', 'icon': 'bookmarks.png'}

>Context menu statement to add a bookmark (obviously within other menus):

    for item in self.list:
        bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
        bookmark['bookmark'] = item['url']
        item.update({'cm': [{'title': 'Add to bookmarks', 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}]})

>Context menu statement to remove bookmark (within bookmarks menu):

    for item in self.list:
        bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
        bookmark['delbookmark'] = item['url']
        item.update({'cm': [{'title': 'Remove from bookmarks', 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

**Cache**

This provides caching functionality. Timeout in hours. creates cache.db file in addon's userdata folder

_Example:_

    _list_ = cache.get(list_to_be_cached, timeout)

**Client**

This one provides extensive urllib2 request functionality, xml parser (parseDOM), javascript parser, cookie handling, random user agent function, urllib retriever, replaceHTMLcodes

_Example:_

    result = client.request(url)

For parseDOM please have a look over here:
[http://kodi.wiki/view/Add-on:Parsedom_for_xbmc_plugins](http://kodi.wiki/view/Add-on:Parsedom_for_xbmc_plugins#parseDOM.28self.2C_html.2C_name_.3D_.22.22.2C_attrs_.3D_.7B.7D.2C_ret_.3D_False.29)

Retriever simply downloads and saves a file:
    client.retriever('source', 'destination'))

**Control**

This one contains important many xbmc* modules equivalents for an addon to properly work.

_Example:_
Get addon id:

    control.addonInfo('id')

**Directory**

This is responsible for creating directories and passing arguments to these creators. Also includes a primitive resolver functionality

_Example:_

    _list_ = []
    directory.add(_list_)

_for setting a resolved url:_

    directory.resolve(params['url'])

**Clean Title** _not tested yet_

Cleans up title strings from "unnecessary" characters such as html codes.

_Example:_

title = 'Some Title &quot;' 

{'title': cleantitle.get(title)}

You will get 'Some Title'

**Workers**

This is for multi process (threading)

**Youtube**

Youtube wrapper

For the purpose of showing an example addon which uses lamlib (in which tulip was based on), I recommend studying an existing one for Euronews:
[https://github.com/lambda81/plugin.video.euronews.com](https://github.com/lambda81/plugin.video.euronews.com)
