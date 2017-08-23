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