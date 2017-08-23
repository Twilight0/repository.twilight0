Table of Contents
=================

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Quickstart](#quickstart)
- [Sublib Module](#sublib-module)
	- [sublib.service](#class-sublibservice)
		- [service.addfile](#def-serviceaddfilepath)
		- [service.addsub](#def-serviceaddsubsub)
		- [service.download](#def-servicedownload)
		- [service.num](#def-servicenumissubtrue)
		- [service.request](#def-servicerequestu-querynone-datanone-referernone-binaryfalse)
		- [service.search](#def-servicesearch)
- [Sublib.Sub Module](#sublibsub-module)
	- [sublib.sub.model](#class-sublibsubmodel)
		- [model.download](#def-modeldownload)
- [Sublib.Item Module](#sublibitem-module)
	- [sublib.item.model](#class-sublibitemmodel)
 
 
Introduction
============
Sublib is a KODI / XBMC library that significantly reduces the effort on developing subtitle addons, it has built in features for

- Automatic parsing of media information
- Automatic parsing of filename information
- Automatic navigation for kodi call
- Ability to use subtitles in archives (zip/rar)
- Automatically match media with the packed subtitles using regexes
- It has an internal archive browser if no match is possible, and lets the user select the file inside the archive. (This is different than dialog.browse().)
- Automatically priotrize the subtitles according to users language settings.
- Allows the service also to priotrize its own matching
- Automatic integration for, listitem language icons, cc, and sync infolabels

It is written in OOP fashion an expects sublib.service to be inherited.  

[Return to TOC](#table-of-contents)
Quickstart
==========
To use it in your subtitle addon first you have make it depend on script.module.sublib. 
Then you have to write your own service in total composed from 2 methods as show in below simple example.

```python
    import sublib
    import os

    class mysubtitlesite(sublib.service):

        def search(self):
            print self.item
            sub = self.sub("Test Subtitle", "en")
            sub.download("http://a.com/b/c.srt")
            self.addsub(sub)

        def download(self, link)
            fname = os.path.join(self.path, "test.srt")
            with open(fname, "w") as f:
                f.write(self.download(link))
            self.addfile(fname)
```

to see it in action simply initialize your class in the module that your "lib" attribute points in your addon.xml

```python
	import myservice
	
	myservice.mysubtitlesite()
```  

Thats all.

[Return to TOC](#table-of-contents)
sublib Module
=============

### class `sublib.service()`
Base class to inherit for subtitle service.

**Example:**
```python
    import sublib
    import os

    class mysubtitlesite(sublib.service):

        def search(self):
            print self.item
            sub = self.sub("Test Subtitle", "en")
            sub.download("http://a.com/b/c.srt")
            self.addsub(sub)

        def download(self, link)
            fname = os.path.join(self.path, "test.srt")
            with open(fname, "w") as f:
                f.write(self.download(link))
            self.addfile(fname)
```
**Params:**

|param| description|
|---|---|
|ua|User-Agent string to be used for http queries|

**Attributes:**

    sub: factory class for found subtitles, see sublib.sub.model()

    item: object holding information that is found from Kodi,
        see sublib.item.model()

    path: temp directory to save the downloaded subtitle file,
        you can use your own directory if you want

[Return to TOC](#table-of-contents) 
----------

Methods:
#### def `service.addfile(path)`
Method to use if a subtitle is downloaded when in self.download method
**Params:**

|param| description|
|---|---|
|path|/path/to/subtitle/file.srt|

**Returns:**
    None

[Return to TOC](#table-of-contents) 

----------
#### def `service.addsub(sub)`
Method to use if a subtitle is found when in self.search method
**Params:**

|param| description|
|---|---|
|sub|subtitle instance of self.sub factory class|

**Returns:**
    None

[Return to TOC](#table-of-contents) 

----------
#### def `service.download()`
This is the method that service has to override. Service supposed to
download the found subtitle to a path, and add this path with
self.addfile("/path/to/file"). *args, **kwargs of the of method is
dynamically created with sub.download(*arg, **kwargs) method. You can
use self.temp folder to save to for ease of access
but this is not mendatory

**Example:**
```python
    def download(self, link, id, isstuff)
        fname = os.path.join(self.path, "test.srt")
        with open(fname, "w") as f:
            f.write(self.download(link))
        self.addfile(fname)

```
**Params:**

|param| description|
|---|---|
|*args|created dynamically from sub.download(*args, *kwargs) method|
|**kwargs|created dynamically from sub.download(*args, *kwargs)|

**Returns:**
    None

[Return to TOC](#table-of-contents) 

----------
#### def `service.num(issub=True)`
Returns the number of found instances. if issub is True, found
subtitles are counted else downlaoded files are counted.
**Params:**

|param| description|
|---|---|
|issub|if issub is True, found subtitles are counted else|

**Returns:**
    int:numberofitems

[Return to TOC](#table-of-contents) 

----------
#### def `service.request(u, query=None, data=None, referer=None, binary=False)`
Helper method to make an http query. This is method is good enough
for vast majority of your needs, includding cookie handlers, with/get
post requests, if you need more advanced queries you can also use
requests or your own implementation
**Params:**

|param| description|
|---|---|
|u|url of the request|
|query|dict carrying the url request arguments|
|data|dict carrying the values to be posted|
|referer|referer for request header|
|binary|bool flag that determines if the return data should be|

**Returns:**
    str/urllib2.reponse:response

[Return to TOC](#table-of-contents) 

----------
#### def `service.search()`
This is the method that service has to override. Service supposed to
find the correct subtitle using self.item obeject, and create a
self.sub instance , and then the found instance must be added with
self.addsub(subins) method.

**Example:**
```python
    def search(self):
        print self.item
        sub = self.sub("Test Subtitle", "en")
        sub.download("http://a.com/b/c.srt")
        self.addsub(sub)

    def download(self, link)
        fname = os.path.join(self.path, "test.srt")
        with open(fname, "w") as f:
            f.write(self.download(link))
        self.addfile(fname)

```
**Params:**

|param| description|
|---|---|

**Returns:**
    None

[Return to TOC](#table-of-contents) 

----------
sublib.sub Module
=================

### class `sublib.sub.model()`
Factory class that defines a found subtitle.
**Params:**

|param| description|
|---|---|
|label  |(required,string) Label to be shown on found subtitles|
|iso    |(required, 2 letter iso639-1 country code) localization of|
|rating |(optional[0], 0 <= integer <=4 ) rating of the subtitle|
|sync   |(optional[False], Bool) bool flag that determines if it is the|
|cc     |(optional[False],Bool) bool flag that determines if it is a closed|
|priorty|(optional[0],int) higher the value is, topper the result is|

**Attributes:**

    label  : (string): Label to be shown on found subtitles
    iso    : (2 letter iso639-1 country code) localization of the subtitle
    rating : (0 <= integer <=4 ) rating of the subtitle
    sync   : (Bool) bool flag that determines if it is the exact match
    cc     : (Bool) bool flag that determines if it is a closed caption
    priorty: (int) higher the value is, topper the result is shown in gui,
        note that preffered language sorting is done automatically and not
        to be considered as a part of this value.
    args   : (list) list of arguments to be passed to download function
    kwargs : (dict) list of keyword arguments to be passed to download function

**Returns:**
    subtitle instance

[Return to TOC](#table-of-contents) 
----------

Methods:
#### def `model.download()`
The arguments sent to this method will be pushed to self.download
method of the service

**Params:**
    *args: arguments to be passed
    **kwargs: keyword arguments to be passed

[Return to TOC](#table-of-contents) 

----------
sublib.item Module
==================

### class `sublib.item.model()`
This is the class that finds all possible information from Kodi and
serves them in their attributes.

**Attributes:**

    title: Title of the media. None if not found

    show: bool flag if the media is a tvshow (includes animes)

    season: integer showing the season, if not known -1, if special:0

    episode: integer showing the season, if not known -1, if special:0

    year: integer showing the year of the media, None if not known

    languages: list of 2 letter iso639 code that the subtitles should be
        found with. First item is always the prferred. You don't have to
        process this information, as long as sub.iso is provided filtering
        and priotrization is done automatically.

    imdb: imdb id string starting with tt

    tvdb: tvdb id string

    tmdb: tmdb id string

    trakt: trakt id string

    slug: slug id string
**Returns:**
    model instance

[Return to TOC](#table-of-contents) 
----------

Methods:
