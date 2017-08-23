# -*- coding: utf-8 -*-
'''
    Author    : Huseyin BIYIK <husenbiyik at hotmail>
    Year      : 2016
    License   : GPL

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

import xbmcvfs
import xbmcgui
import xbmc

import re
import urllib
import urllib2
import cookielib
import unicodedata
import os

_cj = cookielib.CookieJar()
_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(_cj))

useragent = "KODI / XBMC Sublib Library"

prefixes = [
            ["e", "s"],
            ["episode", "seasons"],
            ["", ""],
            ]

seperators = ["", "x", "-", "_"]

regs = []

trims = ["360p", "480p", "576p", "720p", "1080p", "x264", "h264", "bluray"]

for epre, spre in prefixes:
    # build regexes for season and episodes
    for sep in seperators:
        if epre == spre == sep == "":
            continue
        regs.append("%s([0-9]+)%s%s([0-9]+)" % (spre, sep, epre))

for epre, spre in prefixes:
    # build regexes for episode only (animes)
    if epre == "" or epre == "x":
        continue
    regs.append("%s([0-9]+)" % epre)


def html_decode(s):
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'),
            (' ', '&nbsp;'),
            ("'", "&apos;")
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s


def normstr(s):
    s = unicodedata.normalize('NFKD', unicode(unicode(s, 'utf-8')))
    return s.encode('ascii', 'ignore')


def dformat(d, m):
    r = {}
    for k, v in d.iteritems():
        try:
            r[k] = m(v)
        except Exception:
            r[k] = v
    return r


def download(u, query=None, data=None, referer=None, binary=False, ua=None,
             encoding="utf-8"):
    if not ua:
        ua = useragent
    if query:
        q = urllib.urlencode(query)
        u += "?" + q
    if data:
        data = urllib.urlencode(data)
    header = {"User-Agent": ua}
    if referer:
        header["Referer"] = referer
    # print u
    req = urllib2.Request(u, data, header)
    res = _opener.open(req)
    if not binary:
        res = res.read()
        res = res.decode(encoding)
        res = html_decode(res)
    return res


def checkarchive(fname):
    with open(fname) as f:
        sign = f.read(4)
    if sign == "Rar!":
        return "rar"
    elif sign == "\x50\x4B\x03\x04":
        return "zip"


def selectfile(files, prefix="/"):
    if not len(files):
        return
    optlist = []
    dirindex = []
    optindex = -1
    if not prefix == "/":
        optlist.append("..")
        optindex += 1
    for f in files:
        if f.endswith("/"):
            fpath, fname = os.path.split(f[:-1])
            fname = None
        else:
            fpath, fname = os.path.split(f)
        if not fpath == "/":
            fpath += "/"
        if fpath == prefix:
            if fname:
                optlist.append(fname)
                optindex += 1
            else:
                optlist.append("[%s]" % f.split("/")[-2])
                optindex += 1
                dirindex.append(optindex)
    dialog = xbmcgui.Dialog()
    index = dialog.select(xbmc.getLocalizedString(13250), optlist)
    if index < 0:
        # canceled
        return
    if index == 0 and not prefix == "/":
        # parent directory
        prefix = "/".join(prefix.split("/")[:-2]) + "/"
        return selectfile(files, prefix)
    if index in dirindex:
        # sub-folder
        prefix += optlist[index][1:-1] + "/"
        ret = selectfile(files, prefix)
        if ret < 0:
            nprefix = os.path.split(prefix[:-1])[0] + "/"
            nprefix = nprefix.replace("//", "/")
            return selectfile(files, nprefix)
        else:
            return ret
    else:
        # single file
        return prefix + optlist[index]


def getlof(ar, fname, path="", lof=None):
    if not lof:
        lof = []
    ds, fs = xbmcvfs.listdir("%s://%s%s" % (ar, urllib.quote_plus(fname),
                                            path))
    for d in ds:
        dpath = path + "/" + d
        lof.append(dpath + "/")
        getlof(ar, fname, dpath, lof)
    for f in fs:
        lof.append(path + "/" + f)
    return lof


def findshow(season, episode, fname):
    matchstr = os.path.split(fname)[1]
    matchstr = matchstr.lower().replace(" ", "")
    if not episode == -1:
        for reg in regs:
            m = re.search(reg, matchstr)
            if m and m.lastindex == 2 and\
                    m.group(1).isdigit() and \
                    m.group(2).isdigit() and \
                    int(m.group(1)) == season and \
                    int(m.group(2)) == episode:
                return fname
            if m and m.lastindex == 1 and\
                    m.group(1).isdigit() and \
                    int(m.group(1)) == episode and \
                    season < 0:
                return fname


def getar(fname, ar, show, season, episode):
    if fname.endswith("/"):
        fname = fname[:-1]
    lof = getlof(ar, fname)
    if show:
        found = []
        for f in lof:
            if f.endswith("/"):
                continue
            fname = findshow(season, episode, f)
            if fname:
                found.append(fname)
        if len(found):
            lof = found
    if len(lof) == 1:
        return lof[0]
    else:
        return selectfile(lof)


def getsub(fname, show, season, episode):
    isar = checkarchive(fname)
    if isar:
        arname = getar(fname, isar, show, season, episode)
        if not arname:
            return
        uri = "%s://%s%s" % (isar, urllib.quote_plus(fname), arname)
        # fix for rar file system crashes sometimes if archive:// is returned
        fname = fname + arname.replace("/", "_")
        f = xbmcvfs.File(uri)
        with open(fname, "w") as out:
            out.write(f.read())
        f.close()
        return fname
    else:
        return fname


def infofromstr(txt, title=None, show=False, season=-1, episode=-1):
    def striptitle(title):
        chars = [".", ",", "_", "-"]
        for c in chars:
            title = title.replace(c, " ")
        title = title.replace("  ", "")
        title = title.strip()
        return title
    if not isinstance(txt, (str, unicode)):
        txt = str(txt)
    regmatch = False
    matchstr = txt.lower()
    # trim resolation
    for trm in trims:
        matchstr = matchstr.replace(trm, "")
    # trim year info
    matchstr = re.sub("([0-9]{4})", "", matchstr)
    matchstr = matchstr.replace("  ", " ")
    for reg in regs:
        reg = "(.*)" + reg
        m = re.search(reg, matchstr)
        if m and m.lastindex == 3:
            regmatch = True
            # epi,sea
            show = True
            if not title:
                title = striptitle(m.group(1))
            if m.group(2).isdigit():
                season = int(m.group(2))
            if m.group(3).isdigit():
                episode = int(m.group(3))
        if m and m.lastindex == 2:
            regmatch = True
            # epi only
            show = True
            if not title:
                title = striptitle(m.group(1))
            if m.group(2).isdigit():
                season = -1
                episode = int(m.group(2))
        if regmatch:
            break
    if not regmatch:
        # remove extension
        if "." in matchstr:
            matchstr = ".".join(matchstr.split(".")[:-1])
        if not title:
            title = striptitle(matchstr)
    return title, show, season, episode
