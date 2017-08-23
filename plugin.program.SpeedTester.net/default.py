###################################################################################################
#
#                                ** Kodi SpeedTester.net Interface **                                
#
#   Credits:
#          - Matt Martz (https://github.com/sivel/speedtest-cli) for his work on the original speedtest-cli
#
#
#   Reference documentation:
#          - https://pypi.python.org/pypi/speedtest-cli/
#
#   Copyright 2012-2014 Matt Martz
#   All Rights Reserved.
#
#          Licensed under the Apache License, Version 2.0 (the "License"); you may
#          not use this file except in compliance with the License. You may obtain
#          a copy of the License at
#
#               http://www.apache.org/licenses/LICENSE-2.0
#
#          Unless required by applicable law or agreed to in writing, software
#          distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#          WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#          License for the specific language governing permissions and limitations
#          under the License.
#
####################################################################################################


import xbmc
import xbmcgui
import xbmcaddon
import os
import re
import sys
import math
import signal
import socket
import timeit
import threading
import time
import uuid

try:
    import xml.etree.cElementTree as ET
    from xml.dom import minidom as DOM
except ImportError:
    try:
        import xml.etree.ElementTree as ET
    except ImportError:
        from xml.dom import minidom as DOM

        ET = None
        if 73 - 73: II111iiii
        if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00.OoOoOO00.o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'plugin.program.SpeedTester.net'
o0OOO = xbmcaddon.Addon(I1IiI)
iIiiiI = o0OOO.getAddonInfo('id')
Iii1ii1II11i = o0OOO.getAddonInfo('name')
iI111iI = o0OOO.getAddonInfo('icon')
IiII = o0OOO.getAddonInfo('version')
iI1Ii11111iIi = xbmc.translatePath("special://profile/addon_data/%s/" % I1IiI)
i1i1II = o0OOO.getAddonInfo("path")
O0oo0OO0 = xbmc.translatePath("special://temp")
if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
if 12 - 12: o0oOoO00o
i1 = 10
oOOoo00O0O = 92
if 15 - 15: I11iii11IIi
O00o0o0000o0o = False
if 88 - 88: o0ooo / OOO0O / iIii1I11I1II1 * OoooooooOO * II111iiii * iIii1I11I1II1
if 44 - 44: oooO0oo0oOOOO / Oo0Ooo - II111iiii - i11iIiiIii % o0ooo
if 54 - 54: ooO0oo0oO0 % O0 + I1IiiI - o0oOoO00o / i111I
if 31 - 31: OoO0O00 + II111iiii
if 13 - 13: ooO0oo0oO0 * oooO0oo0oOOOO * I1IiiI


if 55 - 55: II111iiii
__version__ = '0.3.2'
if 43 - 43: OoOoOO00 - i1IIi + o0ooo + II1Ii1iI1i
if 17 - 17: o0oOOo0O0Ooo
o00ooooO0oO = 'speedtest-cli/%s' % __version__
oOoOo00oOo = None
Oo = None
if 85 - 85: ooO0oo0oO0 % I1ii11iIi11i * OOO0O
if 90 - 90: o0oOOo0O0Ooo % o0oOOo0O0Ooo % i111I * OoOoOO00
i1IIiiiii = socket.socket
if 55 - 55: i1IIi
try:
    import xml.etree.cElementTree as ET
    from xml.dom import minidom as DOM
except ImportError:
    try:
        import xml.etree.ElementTree as ET
    except ImportError:
        from xml.dom import minidom as DOM

        ET = None
        if 70 - 70: OoO0O00.OoO0O00 - OoO0O00 / I1ii11iIi11i * ooO0oo0oO0
        if 86 - 86: i11iIiiIii + II1Ii1iI1i + OOO0O * i111I + o0oOOo0O0Ooo
try:
    from urllib2 import urlopen, Request, HTTPError, URLError
except ImportError:
    from urllib.request import urlopen, Request, HTTPError, URLError

    if 61 - 61: OoO0O00 / i11iIiiIii
try:
    from httplib import HTTPConnection, HTTPSConnection
except ImportError:
    from http.client import HTTPConnection, HTTPSConnection

    if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
try:
    from Queue import Queue
except ImportError:
    from queue import Queue

    if 65 - 65: OoOoOO00
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

    if 6 - 6: I1IiiI / Oo0Ooo % II1Ii1iI1i
try:
    from urlparse import parse_qs
except ImportError:
    try:
        from urllib.parse import parse_qs
    except ImportError:
        from cgi import parse_qs

        if 84 - 84: i11iIiiIii.o0oOOo0O0Ooo
try:
    from hashlib import md5
except ImportError:
    from md5 import md5

    if 100 - 100: II1Ii1iI1i - II1Ii1iI1i - o0ooo
try:
    from argparse import ArgumentParser as ArgParser
except ImportError:
    from optparse import OptionParser as ArgParser

    if 20 - 20: OoooooooOO
try:
    import builtins
except ImportError:
    def Ii11iI1i(*args, **kwargs):
        Ooo = kwargs.pop("file", sys.stdout)
        if 68 - 68: i111I + ooO0oo0oO0.iIii1I11I1II1 - I11iii11IIi % iIii1I11I1II1 - OOO0O
        if 79 - 79: Oo0Ooo + I1IiiI - o0oOoO00o
        if 83 - 83: OOO0O
        if 64 - 64: OoO0O00 % OOO0O % o0oOoO00o / OoOoOO00 - OoO0O00
        if Ooo is None:
            return
            if 74 - 74: o0oOoO00o * O0

        def oOOo0oo(data):
            if not isinstance(data, basestring):
                data = str(data)
            Ooo.write(data)
            if 80 - 80: i111I * i11iIiiIii / o0ooo

        I11II1i = False
        IIIII = kwargs.pop("sep", None)
        if IIIII is not None:
            if isinstance(IIIII, unicode):
                I11II1i = True
            elif not isinstance(IIIII, str):
                raise TypeError("sep must be None or a string")
        ooooooO0oo = kwargs.pop("end", None)
        if ooooooO0oo is not None:
            if isinstance(ooooooO0oo, unicode):
                I11II1i = True
            elif not isinstance(ooooooO0oo, str):
                raise TypeError("end must be None or a string")
        if kwargs:
            raise TypeError("invalid keyword arguments to print()")
        if not I11II1i:
            for IIiiiiiiIi1I1 in args:
                if isinstance(IIiiiiiiIi1I1, unicode):
                    I11II1i = True
                    break
        if I11II1i:
            I1IIIii = unicode("\n")
            oOoOooOo0o0 = unicode(" ")
        else:
            I1IIIii = "\n"
            oOoOooOo0o0 = " "
        if IIIII is None:
            IIIII = oOoOooOo0o0
        if ooooooO0oo is None:
            ooooooO0oo = I1IIIii
        for OOOO, IIiiiiiiIi1I1 in enumerate(args):
            if OOOO:
                oOOo0oo(IIIII)
            oOOo0oo(IIiiiiiiIi1I1)
        oOOo0oo(ooooooO0oo)
else:
    Ii11iI1i = getattr(builtins, 'print')
    del builtins
    if 87 - 87: oooO0oo0oOOOO / i111I - i1IIi * ooO0oo0oO0 / OoooooooOO.O0
    if 1 - 1: II111iiii - i111I / i111I


class I1II1III11iii(Exception):
    if 75 - 75: iIii1I11I1II1 / ooO0oo0oO0 % o0oOOo0O0Ooo * OoOoOO00
    if 9 - 9: OoO0O00
    if 33 - 33: OOO0O.o0oOoO00o
    if 58 - 58: ooO0oo0oO0 * i11iIiiIii / OoOoOO00 % o0ooo - I1ii11iIi11i / oooO0oo0oOOOO
    if 50 - 50: I1IiiI
    if 34 - 34: I1IiiI * II111iiii % o0oOoO00o * OoOoOO00 - I1IiiI


def II1III(*args, **kwargs):
    if 19 - 19: oooO0oo0oOOOO % i1IIi % o0oOOo0O0Ooo
    if 93 - 93: iIii1I11I1II1 % oooO0oo0oOOOO * i1IIi
    global oOoOo00oOo
    Ii11Ii1I = i1IIiiiii(*args, **kwargs)
    Ii11Ii1I.bind((oOoOo00oOo, 0))
    return Ii11Ii1I
    if 72 - 72: o0oOoO00o / i1IIi * Oo0Ooo - o0ooo
    if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / OOO0O


def iIIIIii1(origin, destination):
    if 58 - 58: i11iIiiIii % i111I
    if 71 - 71: ooO0oo0oO0 + OOO0O % i11iIiiIii + I1ii11iIi11i - I11iii11IIi
    oO0OOoO0, I111Ii111 = origin
    i111IiI1I, O0iII = destination
    o0 = 6371
    if 62 - 62: iIii1I11I1II1 * OoOoOO00
    i1OOO = math.radians(i111IiI1I - oO0OOoO0)
    Oo0oOOo = math.radians(O0iII - I111Ii111)
    Oo0OoO00oOO0o = (math.sin(i1OOO / 2) * math.sin(i1OOO / 2) +
                     math.cos(math.radians(oO0OOoO0)) *
                     math.cos(math.radians(i111IiI1I)) * math.sin(Oo0oOOo / 2) *
                     math.sin(Oo0oOOo / 2))
    OOO00O = 2 * math.atan2(math.sqrt(Oo0OoO00oOO0o), math.sqrt(1 - Oo0OoO00oOO0o))
    OOoOO0oo0ooO = o0 * OOO00O
    if 98 - 98: o0oOoO00o * o0oOoO00o / o0oOoO00o + i111I
    return OOoOO0oo0ooO
    if 34 - 34: OOO0O
    if 15 - 15: i111I * OOO0O * Oo0Ooo % i11iIiiIii % OoOoOO00 - ooO0oo0oO0


def O0ooo0O0oo0(url, data=None, headers={}):
    if 91 - 91: iIii1I11I1II1 + o0ooo
    if 31 - 31: I11iii11IIi.OoOoOO00.ooO0oo0oO0
    if 75 - 75: i111I + OoO0O00.OoOoOO00.OOO0O + Oo0Ooo.OoO0O00
    if 96 - 96: ooO0oo0oO0.OOO0O - Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * ooO0oo0oO0
    if 65 - 65: II1Ii1iI1i.iIii1I11I1II1 / O0 - II1Ii1iI1i
    if 21 - 21: I1IiiI * iIii1I11I1II1
    headers['User-Agent'] = o00ooooO0oO
    return Request(url, data=data, headers=headers)
    if 91 - 91: I11iii11IIi
    if 15 - 15: II111iiii


def Ii(request):
    if 79 - 79: OoooooooOO / O0
    if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo.o0ooo
    if 5 - 5: o0oOOo0O0Ooo * OOO0O + OoOoOO00.ooO0oo0oO0 + OoOoOO00
    if 91 - 91: O0
    if 61 - 61: II111iiii
    try:
        O0OOO = urlopen(request)
        return O0OOO
    except (HTTPError, URLError, socket.error):
        return False
        if 10 - 10: ooO0oo0oO0 * i111I % OoOoOO00 / I1IiiI / OoOoOO00
        if 42 - 42: OoO0O00


class o0o(threading.Thread):
    if 84 - 84: O0
    if 74 - 74: I1ii11iIi11i - I1IiiI - Oo0Ooo.II1Ii1iI1i - I11iii11IIi

    def __init__(self, url, start):
        self.url = url
        self.result = None
        self.starttime = start
        threading.Thread.__init__(self)
        if 73 - 73: Oo0Ooo - i1IIi - i1IIi - o0oOoO00o.II1Ii1iI1i + I1ii11iIi11i

    def run(self):
        self.result = [0]
        try:
            if (timeit.default_timer() - self.starttime) <= 10:
                O0OOo00oo0oOo = O0ooo0O0oo0(self.url)
                OoOo0o = urlopen(O0OOo00oo0oOo)
                i11Iii = OoOo0o.info()
                IiIIIi1iIi = time.time()
                ooOOoooooo = int(i11Iii.getheaders("Content-Length")[0])
                II1I = 0
                while 1 and not Oo.isSet():
                    O0i1II1Iiii1I11 = len(OoOo0o.read(10240))
                    self.result.append(O0i1II1Iiii1I11)
                    if self.result[- 1] == 0:
                        break
                        if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
                    II1I += O0i1II1Iiii1I11
                    o00oooO0Oo = II1I / (1024 * 1024)
                    o0O0OOO0Ooo = float(ooOOoooooo) / (1024 * 1024)
                    iiIiI = II1I / (time.time() - IiIIIi1iIi)
                    I1 = iiIiI / 1024
                    OOO00O0O = '%.02f MB of %.02f MB' % (o00oooO0Oo, o0O0OOO0Ooo)
                    iii = 'Speed: %.02f Kb/s ' % I1
                    if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
                OoOo0o.close()
        except IOError:
            pass
            if 44 - 44: Oo0Ooo.OoO0O00 / I1ii11iIi11i + II1Ii1iI1i
            if 65 - 65: O0


def oO00OOoO00(files, quiet=False):
    if 40 - 40: I1IiiI * II1Ii1iI1i + ooO0oo0oO0 % o0oOoO00o
    if 74 - 74: oooO0oo0oOOOO - Oo0Ooo + OoooooooOO + o0ooo / OoOoOO00
    i1I1iI1iIi111i = timeit.default_timer()
    if 44 - 44: i1IIi % II111iiii + i111I

    def I1I1I(q, files):
        for file in files:
            OoOO000 = o0o(file, i1I1iI1iIi111i)
            OoOO000.start()
            q.put(OoOO000, True)
            if 14 - 14: I11iii11IIi - I1ii11iIi11i
            if not quiet and not Oo.isSet():
                sys.stdout.write('.')
                sys.stdout.flush()
                if 11 - 11: II111iiii * II111iiii % iIii1I11I1II1 * o0ooo + OoOoOO00 / I1IiiI

    ii1Ii11I = []
    if 80 - 80: II111iiii

    def O0O(q, total_files):
        while len(ii1Ii11I) < total_files:
            OoOO000 = q.get(True)
            while OoOO000.isAlive():
                OoOO000.join(timeout=0.1)
            ii1Ii11I.append(sum(OoOO000.result))
            print ((sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i)) / 1000 / 1000) * 8
            del OoOO000
            if 1 - 1: II111iiii

    OOooooO0Oo = Queue(6)
    OO = threading.Thread(target=I1I1I, args=(OOooooO0Oo, files))
    iIiIIi1 = threading.Thread(target=O0O, args=(OOooooO0Oo, len(files)))
    i1I1iI1iIi111i = timeit.default_timer()
    OO.start()
    iIiIIi1.start()
    while OO.isAlive():
        OO.join(timeout=0.1)
    while iIiIIi1.isAlive():
        iIiIIi1.join(timeout=0.1)
    return (sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i))
    if 7 - 7: OOO0O - Oo0Ooo - oooO0oo0oOOOO + OOO0O
    if 26 - 26: II1Ii1iI1i


class I11iiI1i1(threading.Thread):
    if 47 - 47: o0oOoO00o - II1Ii1iI1i.II111iiii + OoooooooOO.i11iIiiIii
    if 94 - 94: o0oOOo0O0Ooo * II1Ii1iI1i / Oo0Ooo / II1Ii1iI1i

    def __init__(self, url, start, size):
        self.url = url
        oO0 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        O0OO0O = oO0 * (int(round(int(size) / 36.0)))
        self.data = ('content1=%s' % O0OO0O[0: int(size) - 9]).encode()
        del O0OO0O
        self.result = None
        self.starttime = start
        threading.Thread.__init__(self)
        if 81 - 81: oooO0oo0oOOOO.o0oOOo0O0Ooo % O0 / I1IiiI - oooO0oo0oOOOO

    def run(self):
        try:
            if ((timeit.default_timer() - self.starttime) <= 10 and
                    not Oo.isSet()):
                O0OOo00oo0oOo = O0ooo0O0oo0(self.url, data=self.data)
                OoOo0o = urlopen(O0OOo00oo0oOo)
                OoOo0o.read(11)
                OoOo0o.close()
                self.result = len(self.data)
            else:
                self.result = 0
        except IOError:
            self.result = 0
            if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * o0ooo * O0
            if 64 - 64: ooO0oo0oO0 % iIii1I11I1II1 * oooO0oo0oOOOO


def o0iI11I1II(url, sizes, quiet=False):
    if 40 - 40: iIii1I11I1II1 / OoOoOO00 % I1ii11iIi11i + II111iiii
    if 27 - 27: II111iiii * OoOoOO00 * iIii1I11I1II1
    i1I1iI1iIi111i = timeit.default_timer()
    if 86 - 86: OoO0O00 * ooO0oo0oO0.o0oOoO00o

    def I1I1I(q, sizes):
        for iI in sizes:
            OoOO000 = I11iiI1i1(url, i1I1iI1iIi111i, iI)
            OoOO000.start()
            q.put(OoOO000, True)
            if not quiet and not Oo.isSet():
                sys.stdout.write('.')
                sys.stdout.flush()
                if 90 - 90: o0ooo % II1Ii1iI1i - iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % I1ii11iIi11i

    ii1Ii11I = []
    if 37 - 37: oooO0oo0oOOOO - I1IiiI.i111I * II1Ii1iI1i - o0oOoO00o

    def O0O(q, total_sizes):
        while len(ii1Ii11I) < total_sizes:
            OoOO000 = q.get(True)
            while OoOO000.isAlive():
                OoOO000.join(timeout=0.1)
            ii1Ii11I.append(OoOO000.result)
            print ((sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i)) / 1000 / 1000) * 8
            del OoOO000
            if 8 - 8: OoO0O00 - I1IiiI % II1Ii1iI1i * OoooooooOO - OoO0O00 * o0ooo

    OOooooO0Oo = Queue(6)
    OO = threading.Thread(target=I1I1I, args=(OOooooO0Oo, sizes))
    iIiIIi1 = threading.Thread(target=O0O, args=(OOooooO0Oo, len(sizes)))
    i1I1iI1iIi111i = timeit.default_timer()
    OO.start()
    iIiIIi1.start()
    while OO.isAlive():
        OO.join(timeout=0.1)
    while iIiIIi1.isAlive():
        iIiIIi1.join(timeout=0.1)
    return (sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i))
    if 6 - 6: OoooooooOO
    if 17 - 17: I1IiiI % o0ooo


def OOOoo(dom, tagName):
    O0oO = dom.getElementsByTagName(tagName)[0]
    if 73 - 73: I1ii11iIi11i * i11iIiiIii % oooO0oo0oOOOO.I1ii11iIi11i
    if 66 - 66: oooO0oo0oOOOO + oooO0oo0oOOOO + OOO0O / o0oOoO00o + ooO0oo0oO0
    if 30 - 30: O0
    if 44 - 44: oooO0oo0oOOOO / i111I / i111I
    if 87 - 87: Oo0Ooo.I1IiiI - II111iiii + O0 / Oo0Ooo / oooO0oo0oOOOO
    if 25 - 25: I1IiiI.I1IiiI - OoOoOO00 % OoOoOO00 - i11iIiiIii / o0ooo
    return dict(list(O0oO.attributes.items()))
    if 51 - 51: Oo0Ooo / OoOoOO00.ooO0oo0oO0 * o0oOOo0O0Ooo + OoO0O00 * I11iii11IIi
    if 73 - 73: OoO0O00 + OoooooooOO - O0 - II1Ii1iI1i - II111iiii


def O0Oo0oOOoooOOOOo():
    if 62 - 62: OOO0O
    if 74 - 74: o0oOoO00o + o0oOOo0O0Ooo
    if 71 - 71: Oo0Ooo % ooO0oo0oO0
    if 98 - 98: i111I % i11iIiiIii % OOO0O + II1Ii1iI1i
    O0OOo00oo0oOo = O0ooo0O0oo0('https://www.speedtest.net/speedtest-config.php')
    O0OOO = Ii(O0OOo00oo0oOo)
    if O0OOO is False:
        Ii11iI1i('Could not retrieve speedtest.net configuration')
        sys.exit(1)
    OOoOO0o0o0 = []
    while 1:
        OOoOO0o0o0.append(O0OOO.read(10240))
        if len(OOoOO0o0o0[- 1]) == 0:
            break
    if int(O0OOO.code) != 200:
        return None
    O0OOO.close()
    try:
        try:
            ii1I1 = ET.fromstring(''.encode().join(OOoOO0o0o0))
            OooooOOoo0 = {
                'client': ii1I1.find('client').attrib,
                'times': ii1I1.find('times').attrib,
                'download': ii1I1.find('download').attrib,
                'upload': ii1I1.find('upload').attrib}
        except Exception, iii:
            xbmc.log('Exception for ET: ' + str(iii), level=xbmc.LOGDEBUG)
            ii1I1 = DOM.parseString(''.join(OOoOO0o0o0))
            OooooOOoo0 = {
                'client': OOOoo(ii1I1, 'client'),
                'times': OOOoo(ii1I1, 'times'),
                'download': OOOoo(ii1I1, 'download'),
                'upload': OOOoo(ii1I1, 'upload')}
    except SyntaxError:
        Ii11iI1i('Failed to parse speedtest.net configuration')
        sys.exit(1)
    del ii1I1
    del OOoOO0o0o0
    return OooooOOoo0
    if 35 - 35: i111I % ooO0oo0oO0 - oooO0oo0oOOOO
    if 20 - 20: i1IIi - OOO0O


def i1iI(client, all=False):
    if 94 - 94: iIii1I11I1II1 / Oo0Ooo % o0oOoO00o * o0oOoO00o * II111iiii
    if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / ooO0oo0oO0 * iIii1I11I1II1
    if 62 - 62: ooO0oo0oO0 / oooO0oo0oOOOO - OoO0O00.i111I
    if 11 - 11: I1ii11iIi11i.OoO0O00 * I11iii11IIi * OoooooooOO + OOO0O
    IiII111i1i11 = [
        'https://www.speedtest.net/speedtest-servers-static.php',
        'http://c.speedtest.net/speedtest-servers-static.php',
    ]
    i111iIi1i1II1 = {}
    for oooO in IiII111i1i11:
        try:
            O0OOo00oo0oOo = O0ooo0O0oo0(oooO)
            O0OOO = Ii(O0OOo00oo0oOo)
            if O0OOO is False:
                raise I1II1III11iii
            i1I1i111Ii = []
            while 1:
                i1I1i111Ii.append(O0OOO.read(10240))
                if len(i1I1i111Ii[- 1]) == 0:
                    break
            if int(O0OOO.code) != 200:
                O0OOO.close()
                raise I1II1III11iii
            O0OOO.close()
            try:
                try:
                    ii1I1 = ET.fromstring(''.encode().join(i1I1i111Ii))
                    ooo = ii1I1.getiterator('server')
                except Exception, iii:
                    xbmc.log('Exception for ET: ' + str(iii), level=xbmc.LOGDEBUG)
                    ii1I1 = DOM.parseString(''.join(i1I1i111Ii))
                    ooo = ii1I1.getElementsByTagName('server')
            except SyntaxError:
                raise I1II1III11iii
            for i1i1iI1iiiI in ooo:
                try:
                    Ooo0oOooo0 = i1i1iI1iiiI.attrib
                except AttributeError:
                    Ooo0oOooo0 = dict(list(i1i1iI1iiiI.attributes.items()))
                OOoOO0oo0ooO = iIIIIii1([float(client['lat']),
                                         float(client['lon'])],
                                        [float(Ooo0oOooo0.get('lat')),
                                         float(Ooo0oOooo0.get('lon'))])
                Ooo0oOooo0['d'] = OOoOO0oo0ooO
                if OOoOO0oo0ooO not in i111iIi1i1II1:
                    i111iIi1i1II1[OOoOO0oo0ooO] = [Ooo0oOooo0]
                else:
                    i111iIi1i1II1[OOoOO0oo0ooO].append(Ooo0oOooo0)
            del ii1I1
            del i1I1i111Ii
            del ooo
        except I1II1III11iii:
            continue
            if 61 - 61: OoOoOO00 - ooO0oo0oO0 - i1IIi
            if 25 - 25: O0 * i111I + I1ii11iIi11i.o0oOOo0O0Ooo.o0oOOo0O0Ooo
        if i111iIi1i1II1:
            break
            if 58 - 58: I1IiiI
    if not i111iIi1i1II1:
        Ii11iI1i('Failed to retrieve list of speedtest.net servers')
        sys.exit(1)
        if 53 - 53: i1IIi
    o0OOOoO0 = []
    for OOoOO0oo0ooO in sorted(i111iIi1i1II1.keys()):
        for o0OoOo00o0o in i111iIi1i1II1[OOoOO0oo0ooO]:
            o0OOOoO0.append(o0OoOo00o0o)
            if len(o0OOOoO0) == 5 and not all:
                break
        else:
            continue
        break
        if 41 - 41: OOO0O % OoO0O00 - Oo0Ooo * o0ooo * Oo0Ooo
    del i111iIi1i1II1
    return o0OOOoO0
    if 69 - 69: ooO0oo0oO0 - OoooooooOO + o0oOOo0O0Ooo - i111I
    if 23 - 23: i11iIiiIii


def II1iIi11(servers):
    if 12 - 12: II1Ii1iI1i + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i.i111I
    if 5 - 5: i1IIi + I11iii11IIi / o0oOOo0O0Ooo.o0oOoO00o / i111I
    if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
    if 7 - 7: o0ooo * OoO0O00 - OOO0O + ooO0oo0oO0 * I1IiiI % OoO0O00
    iI1i111I1Ii = {}
    for i1i1iI1iiiI in servers:
        i11i1ii1I = []
        oooO = '%s/latency.txt' % os.path.dirname(i1i1iI1iiiI['url'])
        o0OO0o0o00o = urlparse(oooO)
        for OOOO in range(0, 3):
            try:
                if o0OO0o0o00o[0] == 'https':
                    oOo0 = HTTPSConnection(o0OO0o0o00o[1])
                else:
                    oOo0 = HTTPConnection(o0OO0o0o00o[1])
                OOOoOO = {'User-Agent': o00ooooO0oO}
                i1I1iI1iIi111i = timeit.default_timer()
                oOo0.request("GET", o0OO0o0o00o[2], headers=OOOoOO)
                I11IIIi = oOo0.getresponse()
                iIIiiI1II1i11 = (timeit.default_timer() - i1I1iI1iIi111i)
            except (HTTPError, URLError, socket.error):
                i11i1ii1I.append(3600)
                continue
            o0o0 = I11IIIi.read(9)
            if int(I11IIIi.status) == 200 and o0o0 == 'test=test'.encode():
                i11i1ii1I.append(iIIiiI1II1i11)
            else:
                i11i1ii1I.append(3600)
            oOo0.close()
        IIii1111 = round((sum(i11i1ii1I) / 6) * 1000, 3)
        iI1i111I1Ii[IIii1111] = i1i1iI1iiiI
    I1iI = sorted(iI1i111I1Ii.keys())[0]
    IIIIiIiIi1 = iI1i111I1Ii[I1iI]
    IIIIiIiIi1['latency'] = I1iI
    if 2 - 2: o0oOoO00o % iIii1I11I1II1 * iIii1I11I1II1.o0oOOo0O0Ooo / o0oOoO00o
    return IIIIiIiIi1
    if 27 - 27: OoO0O00 + OOO0O - i1IIi
    if 69 - 69: I11iii11IIi - O0 % I1ii11iIi11i + i11iIiiIii.OoOoOO00 / OoO0O00


def OoOoo00Ooo00(signum, frame):
    if 57 - 57: o0ooo
    if 32 - 32: II1Ii1iI1i - Oo0Ooo % OoooooooOO.o0oOoO00o / I11iii11IIi + I1IiiI
    if 76 - 76: OOO0O
    if 73 - 73: O0 * o0oOoO00o + II1Ii1iI1i + OOO0O
    global Oo
    Oo.set()
    raise SystemExit('\nCancelling...')
    if 40 - 40: II111iiii.OoOoOO00 * o0ooo + ooO0oo0oO0 + ooO0oo0oO0
    if 9 - 9: i111I % OoooooooOO.oooO0oo0oOOOO % i111I
    if 32 - 32: i11iIiiIii
    if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
    if 41 - 41: Oo0Ooo
    if 10 - 10: Oo0Ooo / Oo0Ooo / o0ooo.o0ooo


def OOoo(list=False, mini=None, server=None, share=False, simple=False, src=None, timeout=10, units=('bit', 8),
         version=False):
    iIIiiiI = xbmcgui.DialogProgress()
    oo0 = [' ', ' ', ' ']
    iIIiiiI.create(Iii1ii1II11i + ' - Powered by SpeedTest.net', oo0[0], oo0[1], oo0[2])
    iIIiiiI.update(0, oo0[0], oo0[1], oo0[2])
    if 34 - 34: I1IiiI % o0oOoO00o + OOO0O * iIii1I11I1II1
    if 33 - 33: I1IiiI / OOO0O * ooO0oo0oO0 / I1ii11iIi11i + Oo0Ooo / o0oOoO00o
    if 40 - 40: I1ii11iIi11i
    global Oo, oOoOo00oOo
    Oo = threading.Event()
    if 60 - 60: I1ii11iIi11i % OoOoOO00 * OoO0O00 % II111iiii
    if 70 - 70: OoO0O00 % oooO0oo0oOOOO + ooO0oo0oO0 / II1Ii1iI1i % O0
    if 100 - 100: o0oOOo0O0Ooo + ooO0oo0oO0 * o0oOOo0O0Ooo
    oOOo0OOOo00O = (
        'Command line interface for testing internet bandwidth using '
        'speedtest.net.\n'
        '------------------------------------------------------------'
        '--------------\n'
        'https://github.com/sivel/speedtest-cli')
    if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - II1Ii1iI1i + I1ii11iIi11i
    if 51 - 51: iIii1I11I1II1.OOO0O + iIii1I11I1II1
    if 95 - 95: I1IiiI
    if version:
        version()
        if 46 - 46: OoOoOO00 + OoO0O00
    socket.setdefaulttimeout(timeout)
    if 70 - 70: o0oOoO00o / iIii1I11I1II1
    if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
    if src:
        oOoOo00oOo = src
        socket.socket = II1III
        if 96 - 96: OoooooooOO + oooO0oo0oOOOO
    oo0[0] = 'Retrieving speedtest.net configuration...'
    iIIiiiI.update(10, oo0[0], oo0[1], oo0[2])
    if not simple:
        Ii11iI1i('Retrieving speedtest.net configuration...')
    try:
        OooooOOoo0 = O0Oo0oOOoooOOOOo()
    except URLError:
        iIIiiiI.close()
        Ii11iI1i('Cannot retrieve speedtest configuration')
        sys.exit(1)
        if 44 - 44: oooO0oo0oOOOO
    oo0[1] = 'Retrieving speedtest.net server list...'
    iIIiiiI.update(15, oo0[0], oo0[1], oo0[2])
    if not simple:
        Ii11iI1i('Retrieving speedtest.net server list...')
    if list or server:
        i111iIi1i1II1 = i1iI(OooooOOoo0['client'], True)
        if list:
            I1i11i = []
            for server in i111iIi1i1II1:
                IiIi = ('%(id)4s) %(sponsor)s (%(name)s, %(country)s) '
                        '[%(d)0.2f km]' % server)
                I1i11i.append(IiIi)
                if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - o0oOoO00o + oooO0oo0oOOOO
                if 82 - 82: oooO0oo0oOOOO / iIii1I11I1II1.I1IiiI.ooO0oo0oO0 / o0oOOo0O0Ooo
                if 42 - 42: Oo0Ooo
            try:
                unicode()
                Ii11iI1i('\n'.join(I1i11i).encode('utf-8', 'ignore'))
            except NameError:
                Ii11iI1i('\n'.join(I1i11i))
            except IOError:
                pass
            sys.exit(0)
    else:
        i111iIi1i1II1 = i1iI(OooooOOoo0['client'])
        if 19 - 19: oooO0oo0oOOOO % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
    oo0[2] = 'Testing from %(isp)s (%(ip)s)...' % OooooOOoo0['client']
    iIIiiiI.update(25, oo0[0], oo0[1], oo0[2])
    if not simple:
        Ii11iI1i('Testing from %(isp)s (%(ip)s)...' % OooooOOoo0['client'])
        if 46 - 46: Oo0Ooo
    if server:
        try:
            IIIIiIiIi1 = II1iIi11(filter(lambda i1II1I1Iii1: i1II1I1Iii1['id'] == server,
                                         i111iIi1i1II1))
        except IndexError:
            iIIiiiI.close()
            Ii11iI1i('Invalid server ID')
            sys.exit(1)
    elif mini:
        iiI11Iii, O0o0O0 = os.path.splitext(mini)
        if O0o0O0:
            oooO = os.path.dirname(mini)
        else:
            oooO = mini
        o0OO0o0o00o = urlparse(oooO)
        try:
            O0OOo00oo0oOo = O0ooo0O0oo0(mini)
            OoOo0o = urlopen(O0OOo00oo0oOo)
        except:
            Ii11iI1i('Invalid Speedtest Mini URL')
            sys.exit(1)
        else:
            o0o0 = OoOo0o.read()
            OoOo0o.close()
        Ii1II1I11i1 = re.findall('upload_extension: "([^"]+)"', o0o0.decode())
        if not Ii1II1I11i1:
            for O0o0O0 in ['php', 'asp', 'aspx', 'jsp']:
                try:
                    O0OOo00oo0oOo = O0ooo0O0oo0('%s/speedtest/upload.%s' %
                                                (mini, O0o0O0))
                    OoOo0o = urlopen(O0OOo00oo0oOo)
                except:
                    pass
                else:
                    O0OO0O = OoOo0o.read().strip()
                    if (OoOo0o.code == 200 and
                                len(O0OO0O.splitlines()) == 1 and
                            re.match('size=[0-9]', O0OO0O)):
                        Ii1II1I11i1 = [O0o0O0]
                        break
        if not o0OO0o0o00o or not Ii1II1I11i1:
            Ii11iI1i('Please provide the full URL of your Speedtest Mini server')
            sys.exit(1)
        i111iIi1i1II1 = [{
            'sponsor': 'Speedtest Mini',
            'name': o0OO0o0o00o[1],
            'd': 0,
            'url': '%s/speedtest/upload.%s' % (oooO.rstrip('/'), Ii1II1I11i1[0]),
            'latency': 0,
            'id': 0
        }]
        try:
            IIIIiIiIi1 = II1iIi11(i111iIi1i1II1)
        except:
            IIIIiIiIi1 = i111iIi1i1II1[0]
    else:
        if not simple:
            oo0[0] = oo0[1]
            oo0[1] = oo0[2]
            oo0[2] = 'Selecting best server based on latency...'
            iIIiiiI.update(30, oo0[0], oo0[1], oo0[2])
            Ii11iI1i('Selecting best server based on latency...')
        IIIIiIiIi1 = II1iIi11(i111iIi1i1II1)
        if 59 - 59: oooO0oo0oOOOO % iIii1I11I1II1.i1IIi
    if not simple:
        if 21 - 21: Oo0Ooo
        if 29 - 29: i111I / II111iiii / OOO0O * ooO0oo0oO0
        if 10 - 10: o0ooo % I11iii11IIi * I11iii11IIi.i111I / II1Ii1iI1i % ooO0oo0oO0
        try:
            unicode()
            oo0[0] = oo0[1]
            oo0[1] = oo0[2]
            oo0[2] = ('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: %(latency)s ms' % IIIIiIiIi1).encode('utf-8',
                                                                                                            'ignore')
            iIIiiiI.update(40, oo0[0], oo0[1], oo0[2])
            Ii11iI1i(('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
                      '%(latency)s ms' % IIIIiIiIi1).encode('utf-8', 'ignore'))
        except NameError:
            oo0[0] = oo0[1]
            oo0[1] = oo0[2]
            oo0[2] = 'Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: %(latency)s ms' % IIIIiIiIi1
            iIIiiiI.update(40, oo0[0], oo0[1], oo0[2])
            Ii11iI1i('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
                     '%(latency)s ms' % IIIIiIiIi1)
    else:
        oo0[0] = oo0[1]
        oo0[1] = oo0[2]
        oo0[2] = 'Ping: %(latency)s ms' % IIIIiIiIi1
        iIIiiiI.update(40, oo0[0], oo0[1], oo0[2])
        Ii11iI1i('Ping: %(latency)s ms' % IIIIiIiIi1)
        if 49 - 49: OoO0O00 / oooO0oo0oOOOO + O0 * o0oOOo0O0Ooo
    I1ii11 = [350, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
    IiII111i1i11 = []
    for iI in I1ii11:
        for OOOO in range(0, 4):
            IiII111i1i11.append('%s/random%sx%s.jpg' %
                                (os.path.dirname(IIIIiIiIi1['url']), iI, iI))
            if 74 - 74: Oo0Ooo - o0oOOo0O0Ooo.i1IIi
    oo0[0] = oo0[1]
    oo0[1] = oo0[2]
    oo0[2] = 'Testing download speed...'
    iIIiiiI.update(50, oo0[0], oo0[1], oo0[2])
    if not simple:
        Ii11iI1i('Testing download speed', end='')
    i1III = oO00OOoO00(IiII111i1i11, simple)
    if not simple:
        Ii11iI1i()
    oo0[0] = oo0[1]
    oo0[1] = oo0[2]
    oo0[2] = 'Download: %0.2f M%s/s' % ((i1III / 1000 / 1000) * units[1], units[0])
    iIIiiiI.update(70, oo0[0], oo0[1], oo0[2])
    Ii11iI1i('Download: %0.2f M%s/s' %
             ((i1III / 1000 / 1000) * units[1], units[0]))
    if 49 - 49: i11iIiiIii % II1Ii1iI1i.OoOoOO00
    Ii1i1iI = [int(.25 * 1000 * 1000), int(.5 * 1000 * 1000)]
    I1ii11 = []
    for iI in Ii1i1iI:
        for OOOO in range(0, 25):
            I1ii11.append(iI)
            if 16 - 16: ooO0oo0oO0 / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % ooO0oo0oO0
    oo0[0] = oo0[1]
    oo0[1] = oo0[2]
    oo0[2] = 'Testing upload speed...'
    iIIiiiI.update(80, oo0[0], oo0[1], oo0[2])
    if not simple:
        Ii11iI1i('Testing upload speed', end='')
    ooo0o00 = o0iI11I1II(IIIIiIiIi1['url'], I1ii11, simple)
    if not simple:
        Ii11iI1i()
    oo0[0] = oo0[1]
    oo0[1] = oo0[2]
    oo0[2] = 'Upload: %0.2f M%s/s' % ((ooo0o00 / 1000 / 1000) * units[1], units[0])
    iIIiiiI.update(99, oo0[0], oo0[1], oo0[2])
    Ii11iI1i('Upload: %0.2f M%s/s' %
             ((ooo0o00 / 1000 / 1000) * units[1], units[0]))
    if 99 - 99: O0.i111I + iIii1I11I1II1
    if share and mini:
        Ii11iI1i('Cannot generate a speedtest.net share results image while '
                 'testing against a Speedtest Mini server')
    elif share:
        I11 = int(round((i1III / 1000) * 8, 0))
        IIi = int(round(IIIIiIiIi1['latency'], 0))
        oOoO00oo0O = int(round((ooo0o00 / 1000) * 8, 0))
        if 39 - 39: iIii1I11I1II1 / O0 / oooO0oo0oOOOO - II1Ii1iI1i - o0oOoO00o % ooO0oo0oO0
        if 31 - 31: i111I - O0 / OOO0O * OoOoOO00
        if 12 - 12: o0oOOo0O0Ooo - OOO0O * o0ooo
        if 14 - 14: Oo0Ooo - II1Ii1iI1i % II1Ii1iI1i * O0.i11iIiiIii / O0
        OOO0oOOoo = [
            'download=%s' % I11,
            'ping=%s' % IIi,
            'upload=%s' % oOoO00oo0O,
            'promo=',
            'startmode=%s' % 'pingselect',
            'recommendedserverid=%s' % IIIIiIiIi1['id'],
            'accuracy=%s' % 1,
            'serverid=%s' % IIIIiIiIi1['id'],
            'hash=%s' % md5(('%s-%s-%s-%s' %
                             (IIi, oOoO00oo0O, I11, '297aae72'))
                            .encode()).hexdigest()]
        if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
        OOOoOO = {'Referer': 'https://c.speedtest.net/flash/speedtest.swf'}
        O0OOo00oo0oOo = O0ooo0O0oo0('https://www.speedtest.net/api/api.php',
                                    data='&'.join(OOO0oOOoo).encode(),
                                    headers=OOOoOO)
        OoOo0o = Ii(O0OOo00oo0oOo)
        if OoOo0o is False:
            Ii11iI1i('Could not submit results to speedtest.net')
            sys.exit(1)
        Oo000ooOOO = OoOo0o.read()
        Ii11i1I11i = OoOo0o.code
        OoOo0o.close()
        if 13 - 13: I11iii11IIi / i11iIiiIii % II111iiii % i111I.I1ii11iIi11i
        if int(Ii11i1I11i) != 200:
            Ii11iI1i('Could not submit results to speedtest.net')
            sys.exit(1)
            if 8 - 8: OoOoOO00 + Oo0Ooo - II111iiii
        IiIi1iIIi1 = parse_qs(Oo000ooOOO.decode())
        O0OoO0ooOO0o = IiIi1iIIi1.get('resultid')
        if not O0OoO0ooOO0o or len(O0OoO0ooOO0o) != 1:
            Ii11iI1i('Could not submit results to speedtest.net')
            sys.exit(1)
            if 81 - 81: O0 * II111iiii + I1IiiI * i11iIiiIii - I1ii11iIi11i / I1IiiI
        Ii11iI1i('Share results: https://www.speedtest.net/result/%s.png' %
                 O0OoO0ooOO0o[0])
        global O00o0o0000o0o
        O00o0o0000o0o = O0OoO0ooOO0o[0]
        import time
        time.sleep(2)
        iIIiiiI.close()
        oO0o00ooO = i11iI11iIiIi()
        oO0o00ooO.doModal()
        del oO0o00ooO
        if 100 - 100: o0ooo.o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
        if 14 - 14: I1ii11iIi11i.OOO0O + II111iiii / o0oOoO00o / i111I
        if 74 - 74: O0 / i1IIi


class i11iI11iIiIi(xbmcgui.WindowDialog):
    def __init__(self):
        self.imgControl = xbmcgui.ControlImage(340, 210, 600, 270,
                                               'https://www.speedtest.net/result/%s.png' % O00o0o0000o0o)
        self.addControl(self.imgControl)
        self.button0 = xbmcgui.ControlButton(int(340 + 505), int(210 + 206), 80, 50, "[B]Close[/B]")
        self.addControl(self.button0)
        self.setFocus(self.button0)
        if 78 - 78: OoooooooOO.OoO0O00 + OOO0O - i1IIi

    def onAction(self, action):
        if action == i1 or action == oOOoo00O0O:
            self.saveClose()
            if 31 - 31: OoooooooOO.ooO0oo0oO0

    def onControl(self, control):
        if control == self.button0:
            self.saveClose()
            if 83 - 83: o0oOoO00o.O0 / Oo0Ooo / ooO0oo0oO0 - II111iiii

    def saveClose(self):
        oO0oO0 = xbmcgui.Dialog()
        i1i1IIIIi1i = oO0oO0.yesno("Save Result", "Would you like to save a copy of this speed test?", "", "")
        if i1i1IIIIi1i:
            self.location = oO0oO0.browse(3, 'Where would you like to save the result?', 'files', '', False, False, '')
            print 'self.location'
            print self.location
            import urllib
            Ii11iiI = urllib.URLopener()
            Ii11iiI.retrieve('https://www.speedtest.net/result/%s.png' % O00o0o0000o0o,
                             self.location + "%s.png" % O00o0o0000o0o)
            oO0oO0.ok("Result Saved!", "'%s.png'" % O00o0o0000o0o + " was saved to '" + self.location + "'")
        oO0oO0.ok("Result Saved!", "Thank you for using Ookla Speedtest.net")
        self.close()
        if 17 - 17: Oo0Ooo % ooO0oo0oO0.i1IIi / OoooooooOO
        if 28 - 28: oooO0oo0oOOOO.II111iiii / I1ii11iIi11i + II111iiii.OoooooooOO.I11iii11IIi


class O000OOO0OOo(xbmcgui.WindowDialog):
    def __init__(self):
        self.imgControl = xbmcgui.ControlImage(340, 210, 600, 270, 'https://www.speedtest.net/result/4670696458.png')
        self.addControl(self.imgControl)
        self.button0 = xbmcgui.ControlButton(int(340 + 505), int(210 + 206), 80, 50, "[B]Close[/B]")
        self.addControl(self.button0)
        self.setFocus(self.button0)
        if 32 - 32: II1Ii1iI1i * O0

    def onAction(self, action):
        if action == i1 or action == oOOoo00O0O:
            self.saveClose()
            if 100 - 100: OOO0O % iIii1I11I1II1 * II111iiii - o0oOoO00o

    def onControl(self, control):
        if control == self.button0:
            self.saveClose()
            if 92 - 92: OOO0O

    def saveClose(self):
        if 22 - 22: Oo0Ooo % o0oOoO00o * I1ii11iIi11i / ooO0oo0oO0 % i11iIiiIii * i111I
        if 95 - 95: OoooooooOO - I11iii11IIi * I1IiiI + OoOoOO00
        oO0oO0 = xbmcgui.Dialog()
        i1i1IIIIi1i = oO0oO0.yesno("Save Result", "Would you like to save a copy of this speed test?", "", "")
        if i1i1IIIIi1i:
            self.location = oO0oO0.browse(3, 'Where would you like to save the result?', 'files', '', False, False, '')
            print 'self.location'
            print self.location
            import urllib
            Ii11iiI = urllib.URLopener()
            Ii11iiI.retrieve('https://www.speedtest.net/result/4670696458.png', self.location + "4670696458.png")
            oO0oO0.ok("Result Saved!", "'4670696458.png'" + " was saved to '" + self.location + "'")
        oO0oO0.ok("Result Saved!", "Thank you for using Ookla Speedtest.net")
        self.close()
        if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
        if 92 - 92: i111I.o0ooo


class oO(xbmcgui.Window):
    def __init__(self):
        if 92 - 92: I11iii11IIi * Oo0Ooo * Oo0Ooo * I1IiiI.iIii1I11I1II1
        if 16 - 16: OOO0O % OoooooooOO - ooO0oo0oO0 * II1Ii1iI1i * I1ii11iIi11i / OoooooooOO
        if 31 - 31: i111I.o0ooo * OOO0O + i11iIiiIii * oooO0oo0oOOOO
        self.screenx = 1920
        self.screeny = 1080
        if 93 - 93: I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * i111I
        self.image_dir = xbmc.translatePath(os.path.join(o0OOO.getAddonInfo('path'), "resources", "images"))
        self.image_background = self.image_dir + '/bg_screen.jpg'
        self.image_progress = self.image_dir + '/ajax-loader-bar.gif'
        self.image_ping = self.image_dir + '/ping_progress_bg.png'
        self.image_ping_glow = self.image_dir + '/ping_progress_glow.png'
        self.image_gauge = self.image_dir + '/gauge_bg.png'
        self.image_gauge_arrow = self.image_dir + '/gauge_ic_arrow.png'
        self.image_button_run = self.image_dir + '/btn_start_bg.png'
        self.image_button_run_glow = self.image_dir + '/btn_start_glow_active.png'
        self.image_speedtestresults = self.image_dir + '/speedtest_results_wtext.png'
        self.image_centertext_testingping = self.image_dir + '/testing_ping.png'
        self.image_result = self.image_speedtestresults
        self.default_advertisement = self.image_dir + ''
        if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo.OOO0O % I11iii11IIi
        self.buildElements()
        if 50 - 50: iIii1I11I1II1 - I11iii11IIi + ooO0oo0oO0

    def buildElements(self):
        if 69 - 69: O0
        if 85 - 85: OOO0O / O0
        if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
        self.background = xbmcgui.ControlImage(0, 0, self.screenx, self.screeny, self.image_background)
        self.addControl(self.background)
        if 62 - 62: o0ooo.I11iii11IIi.OoooooooOO
        self.imgProgress = xbmcgui.ControlImage(340, 640, 600, 20, self.image_progress, aspectRatio=0,
                                                colorDiffuse="0xFF00AACC")
        self.addControl(self.imgProgress)
        self.imgProgress.setVisible(False)
        if 11 - 11: ooO0oo0oO0 / i111I
        oooO0 = 300
        iiIIiii = 122
        iiIIIiIi1IIi = (self.screenx / 3) - (oooO0 / 2)
        ii11i = (self.screeny / 3) - (iiIIiii / 2) + 50
        self.button_run_glow = xbmcgui.ControlImage(iiIIIiIi1IIi, ii11i, oooO0, iiIIiii, self.image_button_run_glow,
                                                    aspectRatio=0)
        self.addControl(self.button_run_glow)
        self.button_run_glow.setVisible(False)
        if 35 - 35: I1ii11iIi11i * o0oOoO00o - OoO0O00 % o0oOOo0O0Ooo
        oOo00O000Oo0 = 320
        I1iI1I1I1i11i = 130
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 50
        self.imgCentertext = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, ' ', aspectRatio=0)
        self.addControl(self.imgCentertext)
        if 57 - 57: II111iiii
        oOo00O000Oo0 = 320
        I1iI1I1I1i11i = 144
        iiI11 = (self.screenx / 2) - 50
        OOoO000 = 50
        self.imgResults = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, self.image_speedtestresults,
                                               aspectRatio=0)
        self.addControl(self.imgResults)
        self.imgResults.setVisible(False)
        if 54 - 54: Oo0Ooo + oooO0oo0oOOOO + i11iIiiIii
        oOo00O000Oo0 = 600
        I1iI1I1I1i11i = 400
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2)
        self.imgPing = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, self.image_ping, aspectRatio=1)
        self.imgPing_glow = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, self.image_ping_glow,
                                                 aspectRatio=1)
        self.addControl(self.imgPing)
        self.addControl(self.imgPing_glow)
        self.imgPing.setVisible(False)
        self.imgPing_glow.setVisible(False)
        if 28 - 28: oooO0oo0oOOOO
        oOo00O000Oo0 = 548
        I1iI1I1I1i11i = 400
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2)
        ooo000o0ooO0 = 66
        I1I = 260
        oOoo000 = (self.screenx / 3) - (ooo000o0ooO0 / 2) - 5
        OooOo00o = (self.screeny / 3) - (I1I / 2) - 60
        self.imgGauge = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, self.image_gauge,
                                             aspectRatio=0)
        self.imgGauge_arrow = xbmcgui.ControlImage(oOoo000, OooOo00o, ooo000o0ooO0, I1I, self.image_gauge_arrow,
                                                   aspectRatio=0)
        self.addControl(self.imgGauge)
        self.addControl(self.imgGauge_arrow)
        self.imgGauge.setVisible(False)
        self.imgGauge_arrow.setVisible(False)
        if 20 - 20: i1IIi * o0ooo + II111iiii % o0oOOo0O0Ooo % oooO0oo0oOOOO
        if 13 - 13: Oo0Ooo
        self.textbox = xbmcgui.ControlTextBox(50, 50, 880, 300, textColor='0xFFFFFFFF')
        self.addControl(self.textbox)
        if 60 - 60: I1ii11iIi11i * I1IiiI
        if 17 - 17: ooO0oo0oO0 % Oo0Ooo / I1ii11iIi11i.I11iii11IIi * ooO0oo0oO0 - II111iiii
        oOo00O000Oo0 = 200
        I1iI1I1I1i11i = 50
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 270
        self.please_wait_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i,
                                                        label='Please wait...', textColor='0xFFFFFFFF', alignment=2 | 4)
        self.addControl(self.please_wait_textbox)
        self.please_wait_textbox.setVisible(False)
        if 41 - 41: II1Ii1iI1i
        oOo00O000Oo0 = 25
        I1iI1I1I1i11i = 50
        iiI11 = (self.screenx / 2) + 188
        OOoO000 = 102
        self.ping_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                                 textColor='0xFFFFFFFF')
        self.addControl(self.ping_textbox)
        if 77 - 77: o0ooo
        oOo00O000Oo0 = 75
        I1iI1I1I1i11i = 50
        iiI11 = (self.screenx / 2) - 40
        OOoO000 = 102
        self.dl_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                               textColor='0xFFFFFFFF')
        self.addControl(self.dl_textbox)
        if 65 - 65: II111iiii.I1IiiI % oooO0oo0oOOOO * OoO0O00
        oOo00O000Oo0 = 75
        I1iI1I1I1i11i = 50
        iiI11 = (self.screenx / 2) + 72
        OOoO000 = 102
        self.ul_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                               textColor='0xFFFFFFFF')
        self.addControl(self.ul_textbox)
        if 38 - 38: OoOoOO00 / o0oOoO00o % Oo0Ooo
        oOo00O000Oo0 = 200
        I1iI1I1I1i11i = 50
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 170
        self.dlul_prog_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                                      textColor='0xFFFFFFFF', font='font30', alignment=2 | 4)
        self.addControl(self.dlul_prog_textbox)
        if 11 - 11: o0oOoO00o - oooO0oo0oOOOO + II111iiii - iIii1I11I1II1
        if 7 - 7: I11iii11IIi - i111I / II111iiii * II1Ii1iI1i.o0oOoO00o * o0oOoO00o
        self.button_run = xbmcgui.ControlButton(iiIIIiIi1IIi, ii11i, oooO0, iiIIiii, "[B]Run Speedtest[/B]",
                                                focusTexture=self.image_button_run,
                                                noFocusTexture=self.image_button_run, alignment=2 | 4,
                                                textColor='0xFF000000', focusedColor='0xFF000000',
                                                shadowColor='0xFFCCCCCC', disabledColor='0xFF000000')
        self.addControl(self.button_run)
        self.setFocus(self.button_run)
        self.button_run_glow.setVisible(True)
        if 61 - 61: i111I % OOO0O - OoO0O00 / Oo0Ooo
        oOo00O000Oo0 = 300
        I1iI1I1I1i11i = 122
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 250
        self.button_close = xbmcgui.ControlButton(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, "[B]Close[/B]",
                                                  focusTexture=self.image_button_run,
                                                  noFocusTexture=self.image_button_run, alignment=2 | 4,
                                                  textColor='0xFF000000', focusedColor='0xFF000000',
                                                  shadowColor='0xFFCCCCCC')
        self.addControl(self.button_close)
        self.button_close.setVisible(False)
        if 4 - 4: OoooooooOO - i1IIi % II1Ii1iI1i - ooO0oo0oO0 * o0oOOo0O0Ooo
        self.setAnimations()
        if 85 - 85: OoooooooOO * iIii1I11I1II1.o0oOoO00o / OoooooooOO % I1IiiI % O0

    def showResult(self):
        oOo00O000Oo0 = 640
        I1iI1I1I1i11i = 288
        iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
        OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 50
        self.imgFinalResults = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, self.image_result,
                                                    aspectRatio=0)
        self.addControl(self.imgFinalResults)
        self.imgFinalResults.setVisible(False)
        self.imgFinalResults.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 delay=2000 time=3000 condition=Control.IsVisible(%d)' % self.imgFinalResults.getId())
        ])
        self.imgFinalResults.setVisible(True)
        if 36 - 36: II1Ii1iI1i / II111iiii / I11iii11IIi / I11iii11IIi + I1ii11iIi11i

    def setAnimations(self):
        self.imgPing.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.imgPing.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgPing.getId())
        ])
        self.imgPing_glow.setAnimations([
            ('conditional',
             'effect=fade start=0 time=1000 pulse=true condition=Control.IsEnabled(%d)' % self.imgPing_glow.getId()),
            ('conditional',
             'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.imgPing_glow.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgPing_glow.getId())
        ])
        self.imgGauge.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.imgGauge.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgGauge.getId())
        ])
        self.imgGauge_arrow.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 time=1000 condition=Control.IsVisible(%d)' % self.imgGauge_arrow.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgGauge_arrow.getId())
        ])
        self.imgProgress.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 time=500 condition=Control.IsVisible(%d)' % self.imgProgress.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgProgress.getId())
        ])
        self.imgCentertext.setAnimations([
            ('conditional', 'effect=fade start=70 time=1000 condition=true pulse=true')
        ])
        self.imgResults.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 delay=2000 time=3000 condition=Control.IsVisible(%d)' % self.imgResults.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgResults.getId())
        ])
        self.button_run.setAnimations([
            ('conditional', 'effect=fade time=3000 condition=Control.IsVisible(%d)' % self.button_run_glow.getId()),
            ('conditional',
             'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.button_run.getId())
        ])
        self.button_run_glow.setAnimations([
            ('conditional', 'effect=fade start=0 time=1000 condition=true pulse=true')
        ])
        self.button_close.setAnimations([
            ('conditional',
             'effect=fade start=0 end=100 delay=300 time=1000 condition=Control.IsVisible(%d)' % self.button_close.getId())
        ])
        if 95 - 95: I11iii11IIi

    def configGauge(self, speed, last_speed=0, time=1000):
        Ooo0oo = 122
        if last_speed == 0:
            last_speed = Ooo0oo
        IIi11IIiIii1 = 0
        if speed <= 1:
            I1iIII1 = 91
            iIii = Ooo0oo
            oOo0OoOOo0 = 1
            iII11I1Ii1 = 0
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 2:
            I1iIII1 = 59
            iIii = 90
            oOo0OoOOo0 = 1
            iII11I1Ii1 = 1
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 3:
            I1iIII1 = 29
            iIii = 58
            oOo0OoOOo0 = 1
            iII11I1Ii1 = 2
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 5:
            I1iIII1 = 0
            iIii = 28
            oOo0OoOOo0 = 2
            iII11I1Ii1 = 3
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 10:
            I1iIII1 = 0
            iIii = 28
            oOo0OoOOo0 = 5
            iII11I1Ii1 = 5
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = float((float(speed) - float(iII11I1Ii1))) * float((float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 20:
            I1iIII1 = 29
            iIii = 58
            oOo0OoOOo0 = 10
            iII11I1Ii1 = 10
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = I1iIII1 + float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 30:
            I1iIII1 = 59
            iIii = 90
            oOo0OoOOo0 = 10
            iII11I1Ii1 = 20
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = I1iIII1 + float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 50:
            I1iIII1 = 91
            iIii = Ooo0oo
            oOo0OoOOo0 = 20
            iII11I1Ii1 = 30
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = I1iIII1 + float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed > 50:
            IIi11IIiIii1 = Ooo0oo
        IIi1IIIIi = "%.0f" % float(IIi11IIiIii1)
        if speed > 5:
            IIi1IIIIi = '-' + str(IIi1IIIIi)
            if 70 - 70: ooO0oo0oO0 / II111iiii - iIii1I11I1II1 - o0oOoO00o
        ooo000o0ooO0 = 66
        I1I = 260
        oOoo000 = (self.screenx / 3) - (ooo000o0ooO0 / 2) + 28
        OooOo00o = (self.screeny / 3) + (I1I / 2) - 88
        self.imgGauge_arrow.setAnimations([
            ('conditional', 'effect=rotate start=%d end=%d center=%d,%d condition=Control.IsVisible(%d) time=%d' % (
            int(last_speed), int(IIi1IIIIi), oOoo000, OooOo00o, self.imgGauge.getId(), time))
        ])
        return IIi1IIIIi
        if 11 - 11: iIii1I11I1II1.OoooooooOO.II111iiii / i1IIi - i111I

    def displayAdvertisement(self):
        try:
            Oo000ooOOO = urlopen(ii1ii11).readline().strip(' \t\n\r')
        except:
            Oo000ooOOO = self.default_advertisement
        print Oo000ooOOO
        if 84 - 84: O0.i111I - II111iiii.OOO0O / II111iiii
        iii1 = 1280
        I1i = 720
        oOo00O000Oo0 = 210
        I1iI1I1I1i11i = 500
        iiI11 = iii1 - oOo00O000Oo0 - 30
        OOoO000 = I1i - I1iI1I1I1i11i - 20
        if 86 - 86: Oo0Ooo / oooO0oo0oOOOO + O0 * o0oOoO00o
        if 19 - 19: II111iiii * I11iii11IIi + II1Ii1iI1i
        if 65 - 65: ooO0oo0oO0.o0ooo.OoO0O00.o0oOoO00o - ooO0oo0oO0
        if 19 - 19: i11iIiiIii + o0oOoO00o % OOO0O

    def onAction(self, action):
        if action == i1 or action == oOOoo00O0O:
            self.saveClose()
            if 14 - 14: OoO0O00.II111iiii.i111I / II1Ii1iI1i % I1ii11iIi11i - OOO0O

    def onControl(self, control):
        if control == self.button_run:
            if 67 - 67: i111I - ooO0oo0oO0.i1IIi
            self.speedtest(share=True, simple=True)
            if 35 - 35: o0oOoO00o + OOO0O - oooO0oo0oOOOO.o0oOoO00o.I11iii11IIi
            self.imgCentertext.setImage(' ')
            self.imgProgress.setEnabled(False)
            self.please_wait_textbox.setVisible(False)
            self.dlul_prog_textbox.setLabel('')
            self.dl_textbox.setLabel('')
            self.ul_textbox.setLabel('')
            self.ping_textbox.setLabel('')
            self.imgResults.setEnabled(False)
            self.imgGauge_arrow.setVisible(False)
            self.imgGauge.setEnabled(False)
            self.showResult()
            self.button_close.setVisible(True)
            self.setFocus(self.button_close)
        if control == self.button_close:
            self.close()
            if 87 - 87: OoOoOO00

    def saveClose(self):
        if 25 - 25: i1IIi.OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
        if 50 - 50: OoO0O00.i11iIiiIii - oooO0oo0oOOOO.oooO0oo0oOOOO
        self.close()
        if 31 - 31: ooO0oo0oO0 / Oo0Ooo * i1IIi.OoOoOO00

    def update_textbox(self, text):
        self.textbox.setText("\n".join(text))
        if 57 - 57: ooO0oo0oO0 + iIii1I11I1II1 % i1IIi % I1IiiI

    def error(self, message):
        if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1.i111I % oooO0oo0oOOOO.OoooooooOO
        self.imgProgress.setImage(' ')
        self.button_close.setVisible(True)
        self.setFocus(self.button_close)
        if 94 - 94: II1Ii1iI1i + iIii1I11I1II1 % OoO0O00

    def downloadSpeed(self, files, quiet=False):
        if 93 - 93: II1Ii1iI1i - ooO0oo0oO0 + iIii1I11I1II1 * o0oOOo0O0Ooo + o0ooo.o0oOoO00o
        if 49 - 49: OoooooooOO * i111I - Oo0Ooo.oooO0oo0oOOOO
        i1I1iI1iIi111i = timeit.default_timer()
        if 89 - 89: OOO0O + II1Ii1iI1i * OOO0O / OOO0O

        def I1I1I(q, files):
            for file in files:
                OoOO000 = o0o(file, i1I1iI1iIi111i)
                OoOO000.start()
                q.put(OoOO000, True)
                if 46 - 46: OoO0O00
                if not quiet and not Oo.isSet():
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    if 71 - 71: i111I / i111I * oooO0oo0oOOOO * oooO0oo0oOOOO / II111iiii

        ii1Ii11I = []
        if 35 - 35: ooO0oo0oO0 * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo.OoOoOO00

        def O0O(q, total_files):
            O00o00O = 0
            while len(ii1Ii11I) < total_files:
                OoOO000 = q.get(True)
                while OoOO000.isAlive():
                    OoOO000.join(timeout=0.1)
                ii1Ii11I.append(sum(OoOO000.result))
                ii1iii11i1 = ((sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i)) / 1000 / 1000) * 8
                O00o00O = self.configGauge(ii1iii11i1, O00o00O)
                self.dlul_prog_textbox.setLabel('%.02f Mbps ' % ii1iii11i1)
                del OoOO000
                if 4 - 4: I11iii11IIi.I11iii11IIi % I1ii11iIi11i % II1Ii1iI1i / II1Ii1iI1i

        OOooooO0Oo = Queue(6)
        OO = threading.Thread(target=I1I1I, args=(OOooooO0Oo, files))
        iIiIIi1 = threading.Thread(target=O0O, args=(OOooooO0Oo, len(files)))
        i1I1iI1iIi111i = timeit.default_timer()
        OO.start()
        iIiIIi1.start()
        while OO.isAlive():
            OO.join(timeout=0.1)
        while iIiIIi1.isAlive():
            iIiIIi1.join(timeout=0.1)
        return (sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i))
        if 29 - 29: Oo0Ooo * OOO0O * I1ii11iIi11i / i11iIiiIii

    def uploadSpeed(self, url, sizes, quiet=False):
        if 26 - 26: I11iii11IIi % o0ooo % oooO0oo0oOOOO % II1Ii1iI1i
        if 55 - 55: OOO0O % OoooooooOO / OoooooooOO % OoooooooOO
        i1I1iI1iIi111i = timeit.default_timer()
        if 52 - 52: I1ii11iIi11i + I1ii11iIi11i.II111iiii

        def I1I1I(q, sizes):
            for iI in sizes:
                OoOO000 = I11iiI1i1(url, i1I1iI1iIi111i, iI)
                OoOO000.start()
                q.put(OoOO000, True)
                if not quiet and not Oo.isSet():
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    if 34 - 34: OoooooooOO.O0 / oooO0oo0oOOOO * OoOoOO00 - I1ii11iIi11i

        ii1Ii11I = []
        if 36 - 36: i1IIi / O0 / OoO0O00 - O0 - i1IIi

        def O0O(q, total_sizes):
            O00o00O = 0
            while len(ii1Ii11I) < total_sizes:
                OoOO000 = q.get(True)
                while OoOO000.isAlive():
                    OoOO000.join(timeout=0.1)
                ii1Ii11I.append(OoOO000.result)
                if 22 - 22: i1IIi + II1Ii1iI1i
                ii1iii11i1 = ((sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i)) / 1000 / 1000) * 8
                O00o00O = self.configGauge(ii1iii11i1, O00o00O)
                self.dlul_prog_textbox.setLabel('%.02f Mbps ' % ii1iii11i1)
                del OoOO000
                if 54 - 54: OOO0O % ooO0oo0oO0.o0ooo + oooO0oo0oOOOO - ooO0oo0oO0 * I1IiiI

        OOooooO0Oo = Queue(6)
        OO = threading.Thread(target=I1I1I, args=(OOooooO0Oo, sizes))
        iIiIIi1 = threading.Thread(target=O0O, args=(OOooooO0Oo, len(sizes)))
        i1I1iI1iIi111i = timeit.default_timer()
        OO.start()
        iIiIIi1.start()
        while OO.isAlive():
            OO.join(timeout=0.1)
        while iIiIIi1.isAlive():
            iIiIIi1.join(timeout=0.1)
        return (sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i))
        if 92 - 92: o0oOOo0O0Ooo + o0ooo / Oo0Ooo % OoO0O00 % I11iii11IIi.OoooooooOO

    def speedtest(self, list=False, mini=None, server=None, share=False, simple=False, src=None, timeout=10,
                  units=('bit', 8), version=False):
        self.imgPing.setVisible(True)
        self.imgPing_glow.setVisible(True)
        oo0 = []
        if 52 - 52: OOO0O / i11iIiiIii - ooO0oo0oO0.I11iii11IIi % iIii1I11I1II1 + o0oOOo0O0Ooo
        if 71 - 71: oooO0oo0oOOOO % i111I * OoOoOO00.O0 / II1Ii1iI1i.I1ii11iIi11i
        if 58 - 58: Oo0Ooo / oooO0oo0oOOOO
        global Oo, oOoOo00oOo
        Oo = threading.Event()
        if 44 - 44: ooO0oo0oO0
        oOOo0OOOo00O = (
            'Command line interface for testing internet bandwidth using '
            'speedtest.net.\n'
            '------------------------------------------------------------'
            '--------------\n'
            'https://github.com/sivel/speedtest-cli')
        if 54 - 54: II1Ii1iI1i - i111I - o0ooo.iIii1I11I1II1
        socket.setdefaulttimeout(timeout)
        if 79 - 79: II1Ii1iI1i.OoO0O00
        if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo.o0oOOo0O0Ooo % OOO0O
        if src:
            oOoOo00oOo = src
            socket.socket = II1III
            if 15 - 15: II1Ii1iI1i * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
        oo0.append('Retrieving speedtest.net configuration...')
        self.update_textbox(oo0)
        if not simple:
            Ii11iI1i('Retrieving speedtest.net configuration...')
        try:
            OooooOOoo0 = O0Oo0oOOoooOOOOo()
        except URLError:
            Ii11iI1i('Cannot retrieve speedtest configuration')
            return False
            if 60 - 60: I1IiiI * o0ooo % OoO0O00 + oooO0oo0oOOOO
        oo0.append('Retrieving speedtest.net server list...')
        self.update_textbox(oo0)
        self.imgCentertext.setImage(self.image_centertext_testingping)
        if not simple:
            Ii11iI1i('Retrieving speedtest.net server list...')
        if list or server:
            i111iIi1i1II1 = i1iI(OooooOOoo0['client'], True)
            if list:
                I1i11i = []
                for server in i111iIi1i1II1:
                    IiIi = ('%(id)4s) %(sponsor)s (%(name)s, %(country)s) '
                            '[%(d)0.2f km]' % server)
                    I1i11i.append(IiIi)
                    if 52 - 52: i1IIi
                    if 84 - 84: II1Ii1iI1i / I11iii11IIi
                    if 86 - 86: OoOoOO00 * II111iiii - O0.OoOoOO00 % iIii1I11I1II1 / ooO0oo0oO0
                try:
                    unicode()
                    Ii11iI1i('\n'.join(I1i11i).encode('utf-8', 'ignore'))
                except NameError:
                    Ii11iI1i('\n'.join(I1i11i))
                except IOError:
                    pass
                sys.exit(0)
        else:
            i111iIi1i1II1 = i1iI(OooooOOoo0['client'])
            if 11 - 11: I1IiiI * oooO0oo0oOOOO + I1ii11iIi11i / I1ii11iIi11i
        oo0.append('Testing from %(isp)s (%(ip)s)...' % OooooOOoo0['client'])
        self.update_textbox(oo0)
        if 37 - 37: i11iIiiIii + i1IIi
        if not simple:
            Ii11iI1i('Testing from %(isp)s (%(ip)s)...' % OooooOOoo0['client'])
            if 23 - 23: o0oOoO00o + i111I.OoOoOO00 * I1IiiI + I1ii11iIi11i
        if server:
            try:
                IIIIiIiIi1 = II1iIi11(filter(lambda i1II1I1Iii1: i1II1I1Iii1['id'] == server,
                                             i111iIi1i1II1))
            except IndexError:
                Ii11iI1i('Invalid server ID')
                return False
        elif mini:
            iiI11Iii, O0o0O0 = os.path.splitext(mini)
            if O0o0O0:
                oooO = os.path.dirname(mini)
            else:
                oooO = mini
            o0OO0o0o00o = urlparse(oooO)
            try:
                O0OOo00oo0oOo = O0ooo0O0oo0(mini)
                OoOo0o = urlopen(O0OOo00oo0oOo)
            except:
                Ii11iI1i('Invalid Speedtest Mini URL')
                return False
            else:
                o0o0 = OoOo0o.read()
                OoOo0o.close()
            Ii1II1I11i1 = re.findall('upload_extension: "([^"]+)"', o0o0.decode())
            if not Ii1II1I11i1:
                for O0o0O0 in ['php', 'asp', 'aspx', 'jsp']:
                    try:
                        O0OOo00oo0oOo = O0ooo0O0oo0('%s/speedtest/upload.%s' %
                                                    (mini, O0o0O0))
                        OoOo0o = urlopen(O0OOo00oo0oOo)
                    except:
                        pass
                    else:
                        O0OO0O = OoOo0o.read().strip()
                        if (OoOo0o.code == 200 and
                                    len(O0OO0O.splitlines()) == 1 and
                                re.match('size=[0-9]', O0OO0O)):
                            Ii1II1I11i1 = [O0o0O0]
                            break
            if not o0OO0o0o00o or not Ii1II1I11i1:
                Ii11iI1i('Please provide the full URL of your Speedtest Mini server')
                return False
            i111iIi1i1II1 = [{
                'sponsor': 'Speedtest Mini',
                'name': o0OO0o0o00o[1],
                'd': 0,
                'url': '%s/speedtest/upload.%s' % (oooO.rstrip('/'), Ii1II1I11i1[0]),
                'latency': 0,
                'id': 0
            }]
            try:
                IIIIiIiIi1 = II1iIi11(i111iIi1i1II1)
            except:
                IIIIiIiIi1 = i111iIi1i1II1[0]
        else:
            if not simple:
                oo0.append('Selecting best server based on latency...')
                self.update_textbox(oo0)
                Ii11iI1i('Selecting best server based on latency...')
            IIIIiIiIi1 = II1iIi11(i111iIi1i1II1)
            if 18 - 18: I11iii11IIi * o0oOOo0O0Ooo.I11iii11IIi / O0
            if 8 - 8: o0oOOo0O0Ooo
            if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * OOO0O - OoOoOO00
        if not simple:
            if 78 - 78: II1Ii1iI1i / II111iiii % OoOoOO00
            if 52 - 52: ooO0oo0oO0 - o0oOoO00o * oooO0oo0oOOOO
            if 17 - 17: OoooooooOO + ooO0oo0oO0 * i111I * OoOoOO00
            try:
                unicode()
                oo0.append(
                    ('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: %(latency)s ms' % IIIIiIiIi1).encode('utf-8',
                                                                                                           'ignore'))
                self.update_textbox(oo0)
                Ii11iI1i(('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
                          '%(latency)s ms' % IIIIiIiIi1).encode('utf-8', 'ignore'))
            except NameError:
                oo0.append('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: %(latency)s ms' % IIIIiIiIi1)
                self.update_textbox(oo0)
                Ii11iI1i('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
                         '%(latency)s ms' % IIIIiIiIi1)
        else:
            oo0.append('Ping: %(latency)s ms' % IIIIiIiIi1)
            self.update_textbox(oo0)
            self.ping_textbox.setLabel("%.0f" % float(IIIIiIiIi1['latency']))
            Ii11iI1i('Ping: %(latency)s ms' % IIIIiIiIi1)
            if 36 - 36: O0 + Oo0Ooo
            if 5 - 5: Oo0Ooo * OoOoOO00
            if 46 - 46: OOO0O
        I1ii11 = [350, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
        IiII111i1i11 = []
        for iI in I1ii11:
            for OOOO in range(0, 4):
                IiII111i1i11.append('%s/random%sx%s.jpg' %
                                    (os.path.dirname(IIIIiIiIi1['url']), iI, iI))
                if 33 - 33: o0oOoO00o - II111iiii * OoooooooOO - Oo0Ooo - ooO0oo0oO0
        self.imgCentertext.setImage(' ')
        self.imgPing.setEnabled(False)
        self.imgPing_glow.setEnabled(False)
        self.imgGauge.setVisible(True)
        time.sleep(1)
        self.configGauge(0)
        self.imgGauge_arrow.setVisible(True)
        if 84 - 84: o0ooo + Oo0Ooo - OoOoOO00 * OoOoOO00
        oo0.append('Testing download speed...')
        self.update_textbox(oo0)
        if not simple:
            Ii11iI1i('Testing download speed', end='')
        i1III = self.downloadSpeed(IiII111i1i11, simple)
        if not simple:
            Ii11iI1i()
        oo0.append('Download: %0.2f M%s/s' % ((i1III / 1000 / 1000) * units[1], units[0]))
        self.update_textbox(oo0)
        self.dl_textbox.setLabel("%.2f" % float((i1III / 1000 / 1000) * units[1]))
        Ii11iI1i('Download: %0.2f M%s/s' %
                 ((i1III / 1000 / 1000) * units[1], units[0]))
        self.configGauge(0, (i1III / 1000 / 1000) * 8, time=3000)
        time.sleep(2)
        if 61 - 61: OoooooooOO.oooO0oo0oOOOO.OoooooooOO / Oo0Ooo
        if 72 - 72: i1IIi
        if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i.OoooooooOO
        Ii1i1iI = [int(.25 * 1000 * 1000), int(.5 * 1000 * 1000)]
        I1ii11 = []
        for iI in Ii1i1iI:
            for OOOO in range(0, 25):
                I1ii11.append(iI)
                if 63 - 63: I1ii11iIi11i
        oo0.append('Testing upload speed...')
        self.update_textbox(oo0)
        if not simple:
            Ii11iI1i('Testing upload speed', end='')
        ooo0o00 = self.uploadSpeed(IIIIiIiIi1['url'], I1ii11, simple)
        if not simple:
            Ii11iI1i()
        oo0.append('Upload: %0.2f M%s/s' % ((ooo0o00 / 1000 / 1000) * units[1], units[0]))
        self.update_textbox(oo0)
        self.ul_textbox.setLabel("%.2f" % float((ooo0o00 / 1000 / 1000) * units[1]))
        Ii11iI1i('Upload: %0.2f M%s/s' %
                 ((ooo0o00 / 1000 / 1000) * units[1], units[0]))
        self.configGauge(0, (ooo0o00 / 1000 / 1000) * 8, time=3000)
        time.sleep(2)
        if 6 - 6: OOO0O / I1ii11iIi11i
        if share and mini:
            Ii11iI1i('Cannot generate a speedtest.net share results image while '
                     'testing against a Speedtest Mini server')
        elif share:
            I11 = int(round((i1III / 1000) * 8, 0))
            IIi = int(round(IIIIiIiIi1['latency'], 0))
            oOoO00oo0O = int(round((ooo0o00 / 1000) * 8, 0))
            if 57 - 57: i111I
            if 67 - 67: OoO0O00.OOO0O
            if 87 - 87: oooO0oo0oOOOO % II1Ii1iI1i
            if 83 - 83: II111iiii - i111I
            OOO0oOOoo = [
                'download=%s' % I11,
                'ping=%s' % IIi,
                'upload=%s' % oOoO00oo0O,
                'promo=',
                'startmode=%s' % 'pingselect',
                'recommendedserverid=%s' % IIIIiIiIi1['id'],
                'accuracy=%s' % 1,
                'serverid=%s' % IIIIiIiIi1['id'],
                'hash=%s' % md5(('%s-%s-%s-%s' %
                                 (IIi, oOoO00oo0O, I11, '297aae72'))
                                .encode()).hexdigest()]
            if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
            OOOoOO = {'Referer': 'https://c.speedtest.net/flash/speedtest.swf'}
            O0OOo00oo0oOo = O0ooo0O0oo0('https://www.speedtest.net/api/api.php',
                                        data='&'.join(OOO0oOOoo).encode(),
                                        headers=OOOoOO)
            OoOo0o = Ii(O0OOo00oo0oOo)
            if OoOo0o is False:
                Ii11iI1i('Could not submit results to speedtest.net')
                return False
            Oo000ooOOO = OoOo0o.read()
            Ii11i1I11i = OoOo0o.code
            OoOo0o.close()
            if 86 - 86: iIii1I11I1II1 + OoOoOO00.i11iIiiIii - II1Ii1iI1i
            if int(Ii11i1I11i) != 200:
                Ii11iI1i('Could not submit results to speedtest.net')
                return False
                if 51 - 51: OoOoOO00
            IiIi1iIIi1 = parse_qs(Oo000ooOOO.decode())
            O0OoO0ooOO0o = IiIi1iIIi1.get('resultid')
            if not O0OoO0ooOO0o or len(O0OoO0ooOO0o) != 1:
                Ii11iI1i('Could not submit results to speedtest.net')
                return False
                if 14 - 14: I11iii11IIi % oooO0oo0oOOOO % Oo0Ooo - i11iIiiIii
            Ii11iI1i('Share results: https://www.speedtest.net/result/%s.png' %
                     O0OoO0ooOO0o[0])
            global O00o0o0000o0o
            if 53 - 53: II1Ii1iI1i % Oo0Ooo
            if not os.path.isdir(iI1Ii11111iIi):
                os.mkdir(iI1Ii11111iIi)
            self.image_result = os.path.join(iI1Ii11111iIi, '%s.png' % O0OoO0ooOO0o[0])
            OOOoOO = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            O0ooOo0o0Oo = Request('https://www.speedtest.net/result/%s.png' % O0OoO0ooOO0o[0], headers=OOOoOO)
            OooO0oOo = urlopen(O0ooOo0o0Oo).read()
            oOOo00O0OOOo = open(self.image_result, 'w+')
            oOOo00O0OOOo.write(OooO0oOo)
            oOOo00O0OOOo.close()
            oo0.append('Results saved: %s' % self.image_result)
            self.update_textbox(oo0)
            if 31 - 31: i111I % ooO0oo0oO0 * i111I
            if 45 - 45: i1IIi.I1IiiI + ooO0oo0oO0 - OoooooooOO % OOO0O
            if 1 - 1: iIii1I11I1II1
            if 93 - 93: i1IIi.i11iIiiIii.Oo0Ooo
            if 99 - 99: i111I - o0ooo - oooO0oo0oOOOO % OoO0O00
            if 21 - 21: II111iiii % I1ii11iIi11i.i1IIi - OoooooooOO
            if 4 - 4: OoooooooOO.OOO0O
            if 78 - 78: I1ii11iIi11i + i111I - O0


import base64

if 10 - 10: o0ooo % I1IiiI
ii1ii11 = base64.b64decode('aHR0cDovL3d3dy5hcm51Ym94b3RhLmNvbS9zcGVlZHRlc3QvYWR2ZXJ0aW1hZ2VfcG9ydHJhaXQucGhw')
if 97 - 97: OoooooooOO - o0ooo
oooo00 = base64.b64decode('aHR0cDovL3d3dy5hcm51Ym94b3RhLmNvbS9zcGVlZHRlc3QvYWR2ZXJ0dmlkZW8ucGhw')
if 96 - 96: I1ii11iIi11i % OOO0O % II1Ii1iI1i - OOO0O % OoOoOO00 + I1ii11iIi11i


class iIOo0O:
    def __init__(self, ProjectID, UserID):
        self.google = HTTPConnection("www.google-analytics.com")
        self.v = '1'
        self.tid = ProjectID
        self.cid = UserID
        self.buildHeaders()
        self.buildParams()
        if 1 - 1: O0 / o0oOoO00o % o0ooo.Oo0Ooo + I11iii11IIi

    def buildHeaders(self):
        self.Headers = {"Host": "www.google-analytics.com"}
        if 27 - 27: o0ooo % OoooooooOO + I11iii11IIi % i1IIi / oooO0oo0oOOOO / OoooooooOO

    def buildParams(self):
        self.Params = [("v", self.v), ("tid", self.tid), ("cid", self.cid)]
        if 11 - 11: ooO0oo0oO0 % II1Ii1iI1i - i11iIiiIii - oooO0oo0oOOOO + OOO0O + I11iii11IIi

    def GASend(self):
        try:
            from urllib import urlencode
            self.google.request("POST", "/collect", urlencode(self.Params), self.Headers)
        except:
            return - 1
            if 87 - 87: o0ooo * i1IIi / I1ii11iIi11i
        return 1
        if 6 - 6: o0oOOo0O0Ooo + Oo0Ooo - OoooooooOO % ooO0oo0oO0 * OoOoOO00

    def GAResponse(self):
        try:
            Oo000ooOOO = self.google.getresponse()
            if Oo000ooOOO.status != "200":
                return - 2
        except:
            return - 1
            if 69 - 69: i1IIi
        return 1
        if 59 - 59: II111iiii - o0oOOo0O0Ooo

    def sendEvent(self, EventCatagory, EventAction):
        self.buildParams()
        self.Body = [("t", "event"), ("ec", EventCatagory), ("ea", EventAction)]
        self.Params = self.Params + self.Body
        print self.Params
        if 24 - 24: Oo0Ooo - i1IIi + i111I
        self.GASend()
        return self.GAResponse()
        if 38 - 38: OoooooooOO / I1ii11iIi11i.O0 / i1IIi / Oo0Ooo + iIii1I11I1II1

    def sendEvent2(self, EventCatagory, EventAction, eventLabel):
        self.buildParams()
        self.Body = [("t", "event"), ("ec", EventCatagory), ("ea", EventAction), ("el", eventLabel)]
        self.Params = self.Params + self.Body
        if 96 - 96: o0oOoO00o
        if 18 - 18: o0oOoO00o * i111I - II1Ii1iI1i
        self.GASend()
        return self.GAResponse()
        if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % oooO0oo0oOOOO

    def sendPageView(self, DocumentHost, DocumentPath, DocumentTitle):
        self.buildParams()
        self.Body = [("t", "pageview"), ("dh", DocumentHost), ("dp", DocumentPath), ("dt", DocumentTitle)]
        self.Params = self.Params + self.Body
        print self.Params
        if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
        self.GASend()
        return self.GAResponse()
        if 13 - 13: OoooooooOO * oooO0oo0oOOOO - II1Ii1iI1i / ooO0oo0oO0 + i111I + I11iii11IIi


def iii1III1i():
    iiiIi = os.path.join(O0oo0OO0, "speedtest-uuid")
    II1Iii = False
    if (os.path.isfile(iiiIi) == True):
        O0oooo0OoO0oo = open(iiiIi, "r")
        IiiiIi1iI1iI = O0oooo0OoO0oo.readline()
        O0oooo0OoO0oo.close()
        hex = IiiiIi1iI1iI.replace('urn:', '').replace('uuid:', '')
        hex = hex.strip('{}').replace('-', '')
        if len(hex) != 32:
            print ('badly formed hexadecimal UUID string')
            II1Iii = False
        try:
            OO00o = uuid.UUID(hex, version=4)
            II1Iii = True
        except:
            II1Iii = False
    if not II1Iii:
        IiiiIi1iI1iI = uuid.uuid4()
        try:
            iiiIi = os.path.join(O0oo0OO0, "speedtest-uuid");
            O0oooo0OoO0oo = open(iiiIi, "w")
            O0oooo0OoO0oo.write(str(IiiiIi1iI1iI))
            O0oooo0OoO0oo.close()
        except Exception, iii:
            xbmc.log('Exception generating UUID cookie: ' + str(iii), level=xbmc.LOGDEBUG)
    return IiiiIi1iI1iI
    if 60 - 60: I1ii11iIi11i - oooO0oo0oOOOO - I1IiiI / o0oOOo0O0Ooo


class oooo00i1(object):
    def __init__(self, video_url):
        if 95 - 95: OoO0O00.i1IIi / i11iIiiIii
        if 38 - 38: Oo0Ooo - i111I.Oo0Ooo
        if 38 - 38: i1IIi + II1Ii1iI1i
        if 91 - 91: II111iiii % o0oOoO00o % I11iii11IIi + II111iiii / oooO0oo0oOOOO
        ooooOooo0 = 'http://www.youtube.com/get_video_info?video_id='
        if 'http://www.youtube.com/watch?v' in parse_qs(video_url).keys():
            ooooOooo0 += parse_qs(video_url)['http://www.youtube.com/watch?v'][0]
        elif 'https://www.youtube.com/watch?v' in parse_qs(video_url).keys():
            ooooOooo0 = 'https://www.youtube.com/get_video_info?video_id=' + \
                        parse_qs(video_url)['https://www.youtube.com/watch?v'][0]
        elif 'v' in parse_qs(video_url).keys():
            ooooOooo0 += parse_qs(video_url)['v'][0]
        else:
            sys.exit('Error : Invalid Youtube URL Passing %s' % video_url)
        O0OOo00oo0oOo = Request(ooooOooo0)
        try:
            self.video_info = parse_qs(urlopen(O0OOo00oo0oOo).read())
        except URLError:
            sys.exit('Error : Invalid Youtube URL Passing %s' % video_url)
            if 73 - 73: OoOoOO00.I1IiiI


def II1i11i1iIi11(videoinfo):
    if not isinstance(videoinfo, oooo00i1):
        if 83 - 83: II1Ii1iI1i
        if 25 - 25: i111I + OoOoOO00.o0oOOo0O0Ooo % OoOoOO00 * ooO0oo0oO0
        if 32 - 32: i11iIiiIii - o0ooo
        return False
    else:
        oo00ooOoo = videoinfo.video_info['url_encoded_fmt_stream_map'][0].split(',')
        iii1IIIiiiI = [parse_qs(OoO00oo00) for OoO00oo00 in oo00ooOoo]
        Oo0Oo0O = [dict(url=OoO00oo00['url'][0], type=OoO00oo00['type']) for OoO00oo00 in iii1IIIiiiI]
        return Oo0Oo0O
        if 44 - 44: OoooooooOO % OoooooooOO


def I11Ii(url_str):
    iIiII = oooo00i1(url_str)
    i1i1IIIIIIIi = II1i11i1iIi11(iIiII)
    oooO = ''
    if 65 - 65: o0oOOo0O0Ooo
    for OoO00oo00 in i1i1IIIIIIIi:
        I1ii1II1iII = OoO00oo00['type'][0]
        I1ii1II1iII = I1ii1II1iII.split(';')[0]
        if I1ii1II1iII.lower() == 'video/mp4'.lower():
            oooO = OoO00oo00['url']
            break
            if 8 - 8: OoOoOO00 / O0 * O0 % o0ooo - Oo0Ooo + i111I
    if not oooO == '':
        return oooO
        if 83 - 83: O0.I1IiiI
        if 95 - 95: i111I.OoooooooOO - i1IIi - OoooooooOO - OoO0O00 % iIii1I11I1II1


class oO0ooOO(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
        self.doModal()
        if 16 - 16: Oo0Ooo + OOO0O / Oo0Ooo / OoO0O00 % oooO0oo0oOOOO % I1ii11iIi11i

    def onInit(self):
        if 22 - 22: II111iiii * OoO0O00 * i111I + I1ii11iIi11i * o0oOOo0O0Ooo
        self.userID = iii1III1i()
        self.analytics = iIOo0O("UA-65633418-1", self.userID)
        self.analytics_video = "Closed before retrieving video"
        self.testRun = False
        if 100 - 100: i1IIi / I11iii11IIi
        if 3 - 3: II111iiii % I1ii11iIi11i - OoooooooOO * Oo0Ooo.iIii1I11I1II1
        if 37 - 37: o0oOoO00o / Oo0Ooo.i111I * i111I
        self.screenx = 1920
        self.screeny = 1080
        if 80 - 80: ooO0oo0oO0 % I1ii11iIi11i
        self.image_dir = xbmc.translatePath(os.path.join(o0OOO.getAddonInfo('path'), "resources", "images"))
        self.image_background = self.image_dir + '/bg_screen.jpg'
        self.image_shadow = self.image_dir + '/shadowframe.png'
        self.image_progress = self.image_dir + '/ajax-loader-bar.gif'
        self.image_ping = self.image_dir + '/ping_progress_bg.png'
        self.image_ping_glow = self.image_dir + '/ping_progress_glow.png'
        self.image_gauge = self.image_dir + '/gauge_bg.png'
        self.image_gauge_arrow = self.image_dir + '/gauge_ic_arrow.png'
        self.image_button_run = self.image_dir + '/btn_start_bg.png'
        self.image_button_run_glow = self.image_dir + '/btn_start_glow_active.png'
        self.image_speedtestresults = self.image_dir + '/speedtest_results_wtext.png'
        self.image_centertext_testingping = self.image_dir + '/testing_ping.png'
        self.image_result = self.image_speedtestresults
        if 91 - 91: i111I / O0 - II1Ii1iI1i.I1IiiI
        if 82 - 82: I11iii11IIi * ooO0oo0oO0 / oooO0oo0oOOOO
        self.playVideo(False)
        if 2 - 2: I1IiiI + o0oOOo0O0Ooo.o0oOOo0O0Ooo.O0 / i111I
        self.textbox = xbmcgui.ControlTextBox(50, 50, 880, 300, textColor='0xFFFFFFFF')
        self.addControl(self.textbox)
        self.displayButtonRun()
        self.displayButtonClose()
        self.setFocus(self.button_run)
        if 40 - 40: o0oOOo0O0Ooo - II111iiii / Oo0Ooo
        if 14 - 14: I1ii11iIi11i

    def onAction(self, action):
        if action == i1 or action == oOOoo00O0O:
            self.saveClose()
            if 5 - 5: o0oOOo0O0Ooo.iIii1I11I1II1 % iIii1I11I1II1

    def displayButtonRun(self, function="true"):
        if (function == "true"):
            oooO0 = 300
            iiIIiii = 122
            iiIIIiIi1IIi = (self.screenx / 3) - (oooO0 / 2)
            ii11i = (self.screeny / 3) - (iiIIiii / 2) + 50
            if 56 - 56: OoooooooOO - i111I - i1IIi
            self.button_run_glow = xbmcgui.ControlImage(iiIIIiIi1IIi, ii11i, oooO0, iiIIiii, '', aspectRatio=0)
            self.addControl(self.button_run_glow)
            self.button_run_glow.setVisible(False)
            self.button_run_glow.setImage(self.image_button_run_glow)
            self.button_run_glow.setAnimations([
                ('conditional', 'effect=fade start=0 time=1000 condition=true pulse=true')
            ])
            if 8 - 8: o0ooo / ooO0oo0oO0.I1IiiI + I1ii11iIi11i / i11iIiiIii
            self.button_run = xbmcgui.ControlButton(iiIIIiIi1IIi, ii11i, oooO0, iiIIiii, "[B]Run Speedtest[/B]",
                                                    focusTexture=self.image_button_run,
                                                    noFocusTexture=self.image_button_run, alignment=2 | 4,
                                                    textColor='0xFF000000', focusedColor='0xFF000000',
                                                    shadowColor='0xFFCCCCCC', disabledColor='0xFF000000')
            self.addControl(self.button_run)
            self.setFocus(self.button_run)
            self.button_run.setVisible(False)
            self.button_run.setAnimations([
                ('conditional',
                 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.button_run.getId())
            ])
            self.button_run_ID = self.button_run.getId()
            if 31 - 31: OOO0O - iIii1I11I1II1 + o0oOoO00o.Oo0Ooo / I11iii11IIi % iIii1I11I1II1
            self.button_run.setEnabled(True)
            self.button_run.setVisible(True)
            self.button_run_glow.setEnabled(True)
            self.button_run_glow.setVisible(True)
        else:
            self.button_run.setEnabled(False)
            self.button_run.setVisible(False)
            self.button_run_glow.setEnabled(False)
            self.button_run_glow.setVisible(False)
            if 6 - 6: I11iii11IIi * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOOo0O0Ooo / i1IIi

    def displayButtonClose(self, function="true"):
        if (function == "true"):
            iii1 = 1280
            I1i = 720
            o0o0oOO = 300
            i1IiI = 122
            i1I1i = iii1 - o0o0oOO - 100
            OO0o = I1i - i1IiI - 180
            if 32 - 32: OoooooooOO - OoOoOO00 - i11iIiiIii * o0oOOo0O0Ooo / Oo0Ooo + OoooooooOO
            self.button_close_glow = xbmcgui.ControlImage(i1I1i, OO0o, o0o0oOO, i1IiI, '', aspectRatio=0)
            self.addControl(self.button_close_glow)
            self.button_close_glow.setVisible(False)
            self.button_close_glow.setImage(self.image_button_run_glow)
            self.button_close_glow.setAnimations([
                ('conditional',
                 'effect=fade start=0 time=1000 delay=2000 pulse=true condition=Control.IsVisible(%d)' % self.button_close_glow.getId())
            ])
            if 35 - 35: i1IIi - o0oOOo0O0Ooo * o0oOoO00o
            self.button_close = xbmcgui.ControlButton(99999, 99999, o0o0oOO, i1IiI, "[B]Close[/B]",
                                                      focusTexture=self.image_button_run,
                                                      noFocusTexture=self.image_button_run, alignment=2 | 4,
                                                      textColor='0xFF000000', focusedColor='0xFF000000',
                                                      shadowColor='0xFFCCCCCC')
            self.addControl(self.button_close)
            self.button_close.setVisible(False)
            self.button_close.setPosition(i1I1i, OO0o)
            self.button_close_ID = self.button_close.getId()
            self.button_close.setAnimations([
                ('conditional',
                 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.button_close.getId())
            ])
        elif (function == "visible"):
            self.button_close.setVisible(True)
            self.button_close_glow.setVisible(True)
            self.setFocus(self.button_close)
        else:
            self.button_close.setVisible(False)
            self.button_close_glow.setVisible(False)
            if 63 - 63: o0oOoO00o * I1ii11iIi11i.OoooooooOO / ooO0oo0oO0 * Oo0Ooo.OOO0O

    def displayPingTest(self, function="true"):
        if (function == "true"):
            if 62 - 62: i1IIi / OOO0O.I1IiiI * o0oOOo0O0Ooo
            oOo00O000Oo0 = 320
            I1iI1I1I1i11i = 130
            iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
            OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 50
            self.imgCentertext = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, ' ', aspectRatio=0)
            self.addControl(self.imgCentertext)
            if 21 - 21: o0oOOo0O0Ooo
            oOo00O000Oo0 = 600
            I1iI1I1I1i11i = 400
            iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
            OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2)
            self.imgPing = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, '', aspectRatio=1)
            self.imgPing_glow = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, '', aspectRatio=1)
            self.addControl(self.imgPing)
            self.addControl(self.imgPing_glow)
            self.imgPing.setVisible(False)
            self.imgPing_glow.setVisible(False)
            self.imgPing.setImage(self.image_ping)
            self.imgPing_glow.setImage(self.image_ping_glow)
            self.imgPing.setAnimations([
                ('conditional',
                 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.imgPing.getId()),
                ('conditional',
                 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgPing.getId())
            ])
            self.imgPing_glow.setAnimations([
                ('conditional',
                 'effect=fade start=0 time=1000 pulse=true condition=Control.IsEnabled(%d)' % self.imgPing_glow.getId()),
                ('conditional',
                 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.imgPing_glow.getId()),
                ('conditional',
                 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgPing_glow.getId())
            ])
            self.imgCentertext.setAnimations([
                ('conditional', 'effect=fade start=70 time=1000 condition=true pulse=true')
            ])
        elif (function == "visible"):
            self.imgPing.setVisible(True)
            self.imgPing_glow.setVisible(True)
        else:
            self.imgPing.setVisible(False)
            self.imgPing_glow.setVisible(False)
            if 81 - 81: i111I / iIii1I11I1II1 - OOO0O * o0ooo.I1IiiI * I1ii11iIi11i
            self.imgCentertext.setVisible(False)
            if 95 - 95: I1IiiI

    def displayGaugeTest(self, function="true"):
        if (function == "true"):
            if 88 - 88: I11iii11IIi % OoO0O00 + o0ooo + o0ooo * II111iiii
            oOo00O000Oo0 = 548
            I1iI1I1I1i11i = 400
            iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
            OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2)
            ooo000o0ooO0 = 66
            I1I = 260
            oOoo000 = (self.screenx / 3) - (ooo000o0ooO0 / 2) - 5
            OooOo00o = (self.screeny / 3) - (I1I / 2) - 60
            self.imgGauge = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, '', aspectRatio=0)
            self.imgGauge_arrow = xbmcgui.ControlImage(oOoo000, OooOo00o, ooo000o0ooO0, I1I, '', aspectRatio=0)
            self.addControl(self.imgGauge)
            self.addControl(self.imgGauge_arrow)
            self.imgGauge.setVisible(False)
            self.imgGauge_arrow.setVisible(False)
            self.imgGauge.setImage(self.image_gauge)
            self.imgGauge_arrow.setImage(self.image_gauge_arrow)
            self.imgGauge.setAnimations([
                ('conditional',
                 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self.imgGauge.getId()),
                ('conditional',
                 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgGauge.getId())
            ])
            self.imgGauge_arrow.setAnimations([
                ('conditional',
                 'effect=fade start=0 end=100 time=1000 condition=Control.IsVisible(%d)' % self.imgGauge_arrow.getId()),
                ('conditional',
                 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgGauge_arrow.getId())
            ])
            if 78 - 78: OoooooooOO
            oOo00O000Oo0 = 200
            I1iI1I1I1i11i = 50
            iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
            OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 170
            self.dlul_prog_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                                          textColor='0xFFFFFFFF', font='font30', alignment=2 | 4)
            self.addControl(self.dlul_prog_textbox)
        elif (function == "visible"):
            self.imgGauge.setEnabled(True)
            self.imgGauge.setVisible(True)
            self.imgGauge_arrow.setEnabled(True)
            self.imgGauge_arrow.setVisible(True)
        else:
            self.imgGauge.setEnabled(False)
            self.imgGauge.setVisible(False)
            self.imgGauge_arrow.setEnabled(False)
            self.imgGauge_arrow.setVisible(False)
            self.dlul_prog_textbox.setLabel('')
            if 77 - 77: I1ii11iIi11i / i1IIi / Oo0Ooo % ooO0oo0oO0

    def displayProgressBar(self, function="true"):
        if (function == "true"):
            if 48 - 48: i111I - I11iii11IIi + iIii1I11I1II1 + OoooooooOO
            self.imgProgress = xbmcgui.ControlImage(340, 640, 600, 20, '', aspectRatio=0, colorDiffuse="0xFF00AACC")
            self.addControl(self.imgProgress)
            self.imgProgress.setVisible(False)
            self.imgProgress.setImage(self.image_progress)
            self.imgProgress.setAnimations([
                ('conditional',
                 'effect=fade start=0 end=100 time=500 condition=Control.IsVisible(%d)' % self.imgProgress.getId()),
                ('conditional',
                 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self.imgProgress.getId())
            ])
            self.imgProgress.setVisible(True)
            if 4 - 4: II111iiii.i111I + II1Ii1iI1i * o0ooo.OOO0O
            oOo00O000Oo0 = 200
            I1iI1I1I1i11i = 50
            iiI11 = (self.screenx / 3) - (oOo00O000Oo0 / 2)
            OOoO000 = (self.screeny / 3) - (I1iI1I1I1i11i / 2) + 270
            self.please_wait_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i,
                                                            label='Please wait...', textColor='0xFFFFFFFF',
                                                            alignment=2 | 4)
            self.addControl(self.please_wait_textbox)
        elif (function == "visible"):
            self.please_wait_textbox.setVisible(True)
            self.imgProgress.setEnabled(True)
            self.imgProgress.setVisible(True)
        else:
            self.please_wait_textbox.setVisible(False)
            self.imgProgress.setEnabled(False)
            self.imgProgress.setVisible(False)
            if 87 - 87: OoOoOO00 / OoO0O00 / i11iIiiIii

    def displayResults(self, function="true"):
        if (function == "true"):
            iii1 = 1280
            I1i = 720
            if 74 - 74: oooO0oo0oOOOO / I1ii11iIi11i % o0oOOo0O0Ooo
            oOo00O000Oo0 = 320
            I1iI1I1I1i11i = 144
            OO0o0OO0 = iii1 - oOo00O000Oo0 - 28
            OooOo0OOO = 40
            if 6 - 6: o0oOoO00o.i111I + II1Ii1iI1i.o0ooo
            if 70 - 70: OoO0O00
            self.imgResults = xbmcgui.ControlImage(OO0o0OO0, OooOo0OOO, oOo00O000Oo0, I1iI1I1I1i11i, '', aspectRatio=0)
            self.addControl(self.imgResults)
            self.imgResults.setVisible(False)
            self.imgResults.setImage(self.image_speedtestresults)
            self.imgResults.setAnimations([
                # I1ii11iIi11i / i1IIi % OoOoOO00
                # o0ooo % II1Ii1iI1i
                # iIii1I11I1II1 . Oo0Ooo + Oo0Ooo - o0oOOo0O0Ooo % o0ooo
                # II1Ii1iI1i + I1ii11iIi11i * ooO0oo0oO0
                ('conditional',
                 'effect=slide start=%d time=2000 delay=50 tween=linear easing=in condition=Control.IsVisible(%d)' % (
                 oOo00O000Oo0 + 50, self.imgResults.getId())),
                ('conditional',
                 'effect=fade start=100 end=0 time=300 delay=1000 condition=!Control.IsEnabled(%d)' % self.imgResults.getId())
            ])
            self.imgResults.setVisible(True)
            if 16 - 16: i111I / I1IiiI + OoO0O00 % iIii1I11I1II1 - i1IIi.oooO0oo0oOOOO
            oOo00O000Oo0 = 75
            I1iI1I1I1i11i = 50
            iiI11 = OO0o0OO0 + 10
            OOoO000 = OooOo0OOO + 52
            self.dl_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                                   textColor='0xFFFFFFFF')
            self.addControl(self.dl_textbox)
            if 26 - 26: o0oOOo0O0Ooo * I11iii11IIi.i1IIi
            oOo00O000Oo0 = 75
            I1iI1I1I1i11i = 50
            iiI11 = OO0o0OO0 + 122
            OOoO000 = OooOo0OOO + 52
            self.ul_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                                   textColor='0xFFFFFFFF')
            self.addControl(self.ul_textbox)
            if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
            oOo00O000Oo0 = 25
            I1iI1I1I1i11i = 50
            iiI11 = OO0o0OO0 + 238
            OOoO000 = OooOo0OOO + 52
            self.ping_textbox = xbmcgui.ControlLabel(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, label='',
                                                     textColor='0xFFFFFFFF')
            self.addControl(self.ping_textbox)
        elif (function == "visible"):
            self.imgResults.setEnabled(True)
            self.imgResults.setVisible(True)
        else:
            self.imgResults.setEnabled(False)
            self.dl_textbox.setLabel('')
            self.ul_textbox.setLabel('')
            self.ping_textbox.setLabel('')
            if 62 - 62: i11iIiiIii % ooO0oo0oO0.I11iii11IIi.ooO0oo0oO0

    def showEndResult(self):
        iii1 = 1280
        I1i = 720
        if 84 - 84: i11iIiiIii * OoO0O00
        if 18 - 18: ooO0oo0oO0 - II1Ii1iI1i - OoOoOO00 / o0ooo - O0
        if 30 - 30: O0 + I1ii11iIi11i + II111iiii
        if 14 - 14: o0oOOo0O0Ooo / ooO0oo0oO0 - iIii1I11I1II1 - oooO0oo0oOOOO % OOO0O
        oOo00O000Oo0 = 320
        I1iI1I1I1i11i = 144
        iiI11 = iii1 - oOo00O000Oo0 - 28
        OOoO000 = 40
        if 49 - 49: OOO0O * oooO0oo0oOOOO / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
        if 57 - 57: OoOoOO00 - oooO0oo0oOOOO / OOO0O % i11iIiiIii
        self.imgFinalResults = xbmcgui.ControlImage(iiI11, OOoO000, oOo00O000Oo0, I1iI1I1I1i11i, '', aspectRatio=0)
        self.addControl(self.imgFinalResults)
        self.imgFinalResults.setVisible(False)
        self.imgFinalResults.setEnabled(False)
        if 3 - 3: o0oOoO00o.OOO0O % I1IiiI + I1ii11iIi11i
        self.imgFinalResults.setImage(self.image_result)
        self.imgFinalResults.setAnimations([
            # i1IIi . II1Ii1iI1i / o0oOOo0O0Ooo / I1IiiI
            # ooO0oo0oO0
            # oooO0oo0oOOOO % OoooooooOO . I1IiiI
            ('conditional',
             'effect=fade start=0 end=100 time=1000 delay=100 condition=Control.IsVisible(%d)' % self.imgFinalResults.getId()),
            ('conditional',
             'effect=zoom end=150 start=100 center=%s time=2000 delay=3000 condition=Control.IsVisible(%d)' % (
             "auto", self.imgFinalResults.getId())),
            ('conditional',
             'effect=slide end=-100,25 time=2000 delay=3000 tween=linear easing=in condition=Control.IsVisible(%d)' % self.imgFinalResults.getId())
        ])
        self.imgFinalResults.setVisible(True)
        self.imgFinalResults.setEnabled(True)
        if 34 - 34: II1Ii1iI1i * OoOoOO00 - I11iii11IIi - I1IiiI - II1Ii1iI1i

    def playVideo(self, function="true"):
        self.videowindow = self.getControl(23)
        if xbmc.getCondVisibility('System.HasAddon(script.system.settings)') and xbmcaddon.Addon(
            id="script.system.settings").getSetting("OEM_DIST") in ["ARNU BOX", "MBOX"]:
            i11IiIIi11I = True; self.analytics_video = "ARNU Box - No video played";
        else:
            i11IiIIi11I = False;
        if (function == "true") and not i11IiIIi11I:
            if 78 - 78: I11iii11IIi
            try:
                Oo0O0Oo00O = urlopen(oooo00).readline().strip(' \t\n\r')
            except:
                Oo0O0Oo00O = ''
                if 9 - 9: o0oOOo0O0Ooo.I1IiiI - I1ii11iIi11i
                if 32 - 32: OoooooooOO / I1IiiI / iIii1I11I1II1 + II111iiii.oooO0oo0oOOOO.o0oOOo0O0Ooo
                if 21 - 21: iIii1I11I1II1 / II111iiii % i1IIi
            IIiI1i = Oo0O0Oo00O
            xbmc.Player().play(IIiI1i, windowed=True)
            if 6 - 6: I1ii11iIi11i / o0oOoO00o - ooO0oo0oO0
            self.videowindow.setVisible(True)
            self.analytics_video = 'Play - %s' % Oo0O0Oo00O
        else:
            self.videowindow.setVisible(False)
            if 62 - 62: i111I % ooO0oo0oO0

    def onAction(self, action):
        if action == i1 or action == oOOoo00O0O:
            self.saveClose()
            if 54 - 54: OoOoOO00 % o0oOoO00o.OoOoOO00 * ooO0oo0oO0 + OoOoOO00 % i1IIi

    def onClick(self, control):
        if control == self.button_run_ID:
            self.testRun = True
            if 23 - 23: o0ooo - ooO0oo0oO0 + II1Ii1iI1i - OoOoOO00 * OoOoOO00.Oo0Ooo
            self.displayButtonRun(False)
            self.displayResults()
            self.displayProgressBar()
            self.displayPingTest()
            self.displayGaugeTest()
            self.analytics.sendPageView("SpeedtestAddon", "speed_test_run", "Oo000ooOOO")
            if 47 - 47: oooO0oo0oOOOO % iIii1I11I1II1
            self.speedtest(share=True, simple=True)
            if 11 - 11: I1IiiI % II1Ii1iI1i - OoO0O00 - oooO0oo0oOOOO + o0oOOo0O0Ooo
            if 98 - 98: o0oOoO00o + II1Ii1iI1i - OoO0O00
            self.displayProgressBar(False)
            self.displayPingTest(False)
            self.displayGaugeTest(False)
            self.displayResults(False)
            self.showEndResult()
            self.displayButtonClose("visible")
            self.playVideo()
        if control == self.button_close_ID:
            self.saveClose()
            if 79 - 79: ooO0oo0oO0 / o0ooo.OoOoOO00 - I1ii11iIi11i

    def saveClose(self):
        if 47 - 47: OoooooooOO % O0 * o0oOoO00o.II1Ii1iI1i
        if 38 - 38: O0 - I11iii11IIi % o0ooo
        if 64 - 64: iIii1I11I1II1
        if xbmc.Player().isPlaying():
            IIi1iI = "Video played for " + str(round(xbmc.Player().getTime(), 2)) + " sec"
        else:
            IIi1iI = '';
        xbmc.Player().stop()
        self.close()
        if 92 - 92: OoO0O00 * OOO0O
        if self.testRun:
            if 35 - 35: i11iIiiIii

    def update_textbox(self, text):
        self.textbox.setText("\n".join(text))
        if 99 - 99: II111iiii.o0oOOo0O0Ooo + O0

    def error(self, message):
        if 71 - 71: I11iii11IIi + i1IIi * Oo0Ooo % Oo0Ooo / Oo0Ooo
        self.imgProgress.setImage(' ')
        self.button_close.setVisible(True)
        self.setFocus(self.button_close)
        if 55 - 55: OoooooooOO + o0ooo + OoooooooOO * OOO0O

    def configGauge(self, speed, last_speed=0, time=1000):
        Ooo0oo = 122
        if last_speed == 0:
            last_speed = Ooo0oo
        IIi11IIiIii1 = 0
        if speed <= 1:
            I1iIII1 = 91
            iIii = Ooo0oo
            oOo0OoOOo0 = 1
            iII11I1Ii1 = 0
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 2:
            I1iIII1 = 59
            iIii = 90
            oOo0OoOOo0 = 1
            iII11I1Ii1 = 1
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 3:
            I1iIII1 = 29
            iIii = 58
            oOo0OoOOo0 = 1
            iII11I1Ii1 = 2
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 5:
            I1iIII1 = 0
            iIii = 28
            oOo0OoOOo0 = 2
            iII11I1Ii1 = 3
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = iIii - float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 10:
            I1iIII1 = 0
            iIii = 28
            oOo0OoOOo0 = 5
            iII11I1Ii1 = 5
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = float((float(speed) - float(iII11I1Ii1))) * float((float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 20:
            I1iIII1 = 29
            iIii = 58
            oOo0OoOOo0 = 10
            iII11I1Ii1 = 10
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = I1iIII1 + float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 30:
            I1iIII1 = 59
            iIii = 90
            oOo0OoOOo0 = 10
            iII11I1Ii1 = 20
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = I1iIII1 + float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed <= 50:
            I1iIII1 = 91
            iIii = Ooo0oo
            oOo0OoOOo0 = 20
            iII11I1Ii1 = 30
            o0o0oOo0oO = (iIii - I1iIII1)
            IIi11IIiIii1 = I1iIII1 + float((float(speed) - float(iII11I1Ii1))) * float(
                (float(o0o0oOo0oO) / float(oOo0OoOOo0)))
        elif speed > 50:
            IIi11IIiIii1 = Ooo0oo
        IIi1IIIIi = "%.0f" % float(IIi11IIiIii1)
        if speed > 5:
            IIi1IIIIi = '-' + str(IIi1IIIIi)
            if 68 - 68: O0
        ooo000o0ooO0 = 66
        I1I = 260
        oOoo000 = (self.screenx / 3) - (ooo000o0ooO0 / 2) + 28
        OooOo00o = (self.screeny / 3) + (I1I / 2) - 88
        self.imgGauge_arrow.setAnimations([
            ('conditional', 'effect=rotate start=%d end=%d center=%d,%d condition=Control.IsVisible(%d) time=%d' % (
            int(last_speed), int(IIi1IIIIi), oOoo000, OooOo00o, self.imgGauge.getId(), time))
        ])
        return IIi1IIIIi
        if 2 - 2: OoO0O00 + O0 * OoO0O00 - II1Ii1iI1i + oooO0oo0oOOOO

    def downloadSpeed(self, files, quiet=False):
        if 43 - 43: I1ii11iIi11i - OoOoOO00
        if 36 - 36: I1ii11iIi11i - o0oOoO00o
        i1I1iI1iIi111i = timeit.default_timer()
        if 24 - 24: o0oOOo0O0Ooo + OOO0O + i111I - iIii1I11I1II1

        def I1I1I(q, files):
            for file in files:
                OoOO000 = o0o(file, i1I1iI1iIi111i)
                OoOO000.start()
                q.put(OoOO000, True)
                if 49 - 49: i111I.OOO0O * OoOoOO00 % I11iii11IIi.O0
                if not quiet and not Oo.isSet():
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    if 48 - 48: O0 * II1Ii1iI1i - O0 / II1Ii1iI1i + OoOoOO00

        ii1Ii11I = []
        if 52 - 52: OoO0O00 % II1Ii1iI1i * II111iiii

        def O0O(q, total_files):
            O00o00O = 0
            while len(ii1Ii11I) < total_files:
                OoOO000 = q.get(True)
                while OoOO000.isAlive():
                    OoOO000.join(timeout=0.1)
                ii1Ii11I.append(sum(OoOO000.result))
                ii1iii11i1 = ((sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i)) / 1000 / 1000) * 8
                O00o00O = self.configGauge(ii1iii11i1, O00o00O)
                self.dlul_prog_textbox.setLabel('%.02f Mbps ' % ii1iii11i1)
                del OoOO000
                if 4 - 4: i111I % O0 - OoooooooOO + OOO0O.oooO0oo0oOOOO % II111iiii

        OOooooO0Oo = Queue(6)
        OO = threading.Thread(target=I1I1I, args=(OOooooO0Oo, files))
        iIiIIi1 = threading.Thread(target=O0O, args=(OOooooO0Oo, len(files)))
        i1I1iI1iIi111i = timeit.default_timer()
        OO.start()
        iIiIIi1.start()
        while OO.isAlive():
            OO.join(timeout=0.1)
        while iIiIIi1.isAlive():
            iIiIIi1.join(timeout=0.1)
        return (sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i))
        if 9 - 9: II111iiii * II111iiii.i11iIiiIii * iIii1I11I1II1

    def uploadSpeed(self, url, sizes, quiet=False):
        if 18 - 18: OoO0O00.II111iiii % OoOoOO00 % II1Ii1iI1i
        if 87 - 87: iIii1I11I1II1.OoooooooOO * OoOoOO00
        i1I1iI1iIi111i = timeit.default_timer()
        if 100 - 100: OoO0O00 / i1IIi - I1IiiI % II1Ii1iI1i - iIii1I11I1II1

        def I1I1I(q, sizes):
            for iI in sizes:
                OoOO000 = I11iiI1i1(url, i1I1iI1iIi111i, iI)
                OoOO000.start()
                q.put(OoOO000, True)
                if not quiet and not Oo.isSet():
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    if 17 - 17: i111I / o0oOOo0O0Ooo % Oo0Ooo

        ii1Ii11I = []
        if 71 - 71: I11iii11IIi.o0ooo.OoO0O00

        def O0O(q, total_sizes):
            O00o00O = 0
            while len(ii1Ii11I) < total_sizes:
                OoOO000 = q.get(True)
                while OoOO000.isAlive():
                    OoOO000.join(timeout=0.1)
                ii1Ii11I.append(OoOO000.result)
                if 68 - 68: i11iIiiIii % oooO0oo0oOOOO * OoO0O00 * I11iii11IIi * II111iiii + O0
                ii1iii11i1 = ((sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i)) / 1000 / 1000) * 8
                O00o00O = self.configGauge(ii1iii11i1, O00o00O)
                self.dlul_prog_textbox.setLabel('%.02f Mbps ' % ii1iii11i1)
                del OoOO000
                if 66 - 66: i111I % I1ii11iIi11i % OoooooooOO

        OOooooO0Oo = Queue(6)
        OO = threading.Thread(target=I1I1I, args=(OOooooO0Oo, sizes))
        iIiIIi1 = threading.Thread(target=O0O, args=(OOooooO0Oo, len(sizes)))
        i1I1iI1iIi111i = timeit.default_timer()
        OO.start()
        iIiIIi1.start()
        while OO.isAlive():
            OO.join(timeout=0.1)
        while iIiIIi1.isAlive():
            iIiIIi1.join(timeout=0.1)
        return (sum(ii1Ii11I) / (timeit.default_timer() - i1I1iI1iIi111i))
        if 34 - 34: o0oOOo0O0Ooo / o0oOoO00o % O0.OoO0O00.i1IIi

    def speedtest(self, list=False, mini=None, server=None, share=False, simple=False, src=None, timeout=10,

       units=('bit', 8), version=False):
        self.imgPing.setVisible(True)
        self.imgPing_glow.setVisible(True)
        oo0 = ['Running Speed Tester']
        if 29 - 29: O0.o0ooo
        if 66 - 66: oooO0oo0oOOOO * iIii1I11I1II1 % iIii1I11I1II1 * I11iii11IIi - OOO0O - I11iii11IIi
        if 70 - 70: o0ooo + oooO0oo0oOOOO
        global Oo, oOoOo00oOo
        Oo = threading.Event()
        if 93 - 93: o0ooo + II1Ii1iI1i
        oOOo0OOOo00O = (
            'Command line interface for testing internet bandwidth using '
            'speedtest.net.\n'
            '------------------------------------------------------------'
            '--------------\n'
            'https://github.com/sivel/speedtest-cli')
        if 33 - 33: O0
        socket.setdefaulttimeout(timeout)
        if 78 - 78: O0 / II111iiii * OoO0O00
        if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % o0ooo - iIii1I11I1II1 % O0
        if src:
            oOoOo00oOo = src
            socket.socket = II1III
            if 58 - 58: I11iii11IIi + iIii1I11I1II1
        oo0.append('Retrieving speedtest.net configuration...')
        self.update_textbox(oo0)
        if not simple:
            Ii11iI1i('Retrieving speedtest.net configuration...')
        try:
            OooooOOoo0 = O0Oo0oOOoooOOOOo()
        except URLError:
            Ii11iI1i('Cannot retrieve speedtest configuration')
            return False
            if 65 - 65: II111iiii - o0ooo % o0oOOo0O0Ooo - OoOoOO00 * o0oOoO00o + II1Ii1iI1i
        oo0.append('Retrieving speedtest.net server list...')
        self.update_textbox(oo0)
        self.imgCentertext.setImage(self.image_centertext_testingping)
        if not simple:
            Ii11iI1i('Retrieving speedtest.net server list...')
        if list or server:
            i111iIi1i1II1 = i1iI(OooooOOoo0['client'], True)
            if list:
                I1i11i = []
                for server in i111iIi1i1II1:
                    IiIi = ('%(id)4s) %(sponsor)s (%(name)s, %(country)s) '
                            '[%(d)0.2f km]' % server)
                    I1i11i.append(IiIi)
                    if 79 - 79: OOO0O.OoOoOO00 % o0ooo - Oo0Ooo
                    if 69 - 69: OOO0O - o0oOOo0O0Ooo.OOO0O
                    if 9 - 9: oooO0oo0oOOOO % i11iIiiIii / Oo0Ooo
                try:
                    unicode()
                    Ii11iI1i('\n'.join(I1i11i).encode('utf-8', 'ignore'))
                except NameError:
                    Ii11iI1i('\n'.join(I1i11i))
                except IOError:
                    pass
                sys.exit(0)
        else:
            i111iIi1i1II1 = i1iI(OooooOOoo0['client'])
            if 20 - 20: oooO0oo0oOOOO * O0 + i111I - OoooooooOO.i111I
        oo0.append('Testing from %(isp)s (%(ip)s)...' % OooooOOoo0['client'])
        self.update_textbox(oo0)
        if 60 - 60: o0oOOo0O0Ooo.o0oOOo0O0Ooo / o0oOoO00o
        if not simple:
            Ii11iI1i('Testing from %(isp)s (%(ip)s)...' % OooooOOoo0['client'])
            if 45 - 45: O0.i11iIiiIii % o0oOoO00o.OoOoOO00 % I11iii11IIi % iIii1I11I1II1
        if server:
            try:
                IIIIiIiIi1 = II1iIi11(filter(lambda i1II1I1Iii1: i1II1I1Iii1['id'] == server,
                                             i111iIi1i1II1))
            except IndexError:
                Ii11iI1i('Invalid server ID')
                return False
        elif mini:
            iiI11Iii, O0o0O0 = os.path.splitext(mini)
            if O0o0O0:
                oooO = os.path.dirname(mini)
            else:
                oooO = mini
            o0OO0o0o00o = urlparse(oooO)
            try:
                O0OOo00oo0oOo = O0ooo0O0oo0(mini)
                OoOo0o = urlopen(O0OOo00oo0oOo)
            except:
                Ii11iI1i('Invalid Speedtest Mini URL')
                return False
            else:
                o0o0 = OoOo0o.read()
                OoOo0o.close()
            Ii1II1I11i1 = re.findall('upload_extension: "([^"]+)"', o0o0.decode())
            if not Ii1II1I11i1:
                for O0o0O0 in ['php', 'asp', 'aspx', 'jsp']:
                    try:
                        O0OOo00oo0oOo = O0ooo0O0oo0('%s/speedtest/upload.%s' %
                                                    (mini, O0o0O0))
                        OoOo0o = urlopen(O0OOo00oo0oOo)
                    except:
                        pass
                    else:
                        O0OO0O = OoOo0o.read().strip()
                        if (OoOo0o.code == 200 and
                                    len(O0OO0O.splitlines()) == 1 and
                                re.match('size=[0-9]', O0OO0O)):
                            Ii1II1I11i1 = [O0o0O0]
                            break
            if not o0OO0o0o00o or not Ii1II1I11i1:
                Ii11iI1i('Please provide the full URL of your Speedtest Mini server')
                return False
            i111iIi1i1II1 = [{
                'sponsor': 'Speedtest Mini',
                'name': o0OO0o0o00o[1],
                'd': 0,
                'url': '%s/speedtest/upload.%s' % (oooO.rstrip('/'), Ii1II1I11i1[0]),
                'latency': 0,
                'id': 0
            }]
            try:
                IIIIiIiIi1 = II1iIi11(i111iIi1i1II1)
            except:
                IIIIiIiIi1 = i111iIi1i1II1[0]
        else:
            if not simple:
                oo0.append('Selecting best server based on latency...')
                self.update_textbox(oo0)
                Ii11iI1i('Selecting best server based on latency...')
            IIIIiIiIi1 = II1iIi11(i111iIi1i1II1)
            if 58 - 58: iIii1I11I1II1.OoOoOO00 - i11iIiiIii * iIii1I11I1II1 % i11iIiiIii / I1IiiI
            if 80 - 80: I1ii11iIi11i / iIii1I11I1II1 % OoOoOO00
            if 80 - 80: OoO0O00 % o0oOoO00o
        if not simple:
            if 99 - 99: OOO0O / iIii1I11I1II1 - II1Ii1iI1i * I1ii11iIi11i % I1IiiI
            if 13 - 13: OoO0O00
            if 70 - 70: o0ooo + O0.oooO0oo0oOOOO * II1Ii1iI1i
            try:
                unicode()
                oo0.append(
                    ('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: %(latency)s ms' % IIIIiIiIi1).encode('utf-8',
                                                                                                           'ignore'))
                self.update_textbox(oo0)
                Ii11iI1i(('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
                          '%(latency)s ms' % IIIIiIiIi1).encode('utf-8', 'ignore'))
            except NameError:
                oo0.append('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: %(latency)s ms' % IIIIiIiIi1)
                self.update_textbox(oo0)
                Ii11iI1i('Hosted by %(sponsor)s (%(name)s) [%(d)0.2f km]: '
                         '%(latency)s ms' % IIIIiIiIi1)
        else:
            oo0.append('Ping: %(latency)s ms' % IIIIiIiIi1)
            self.update_textbox(oo0)
            self.ping_textbox.setLabel("%.0f" % float(IIIIiIiIi1['latency']))
            Ii11iI1i('Ping: %(latency)s ms' % IIIIiIiIi1)
        self.imgCentertext.setImage(' ')
        self.imgPing.setEnabled(False)
        self.imgPing_glow.setEnabled(False)
        if 2 - 2: OoooooooOO.ooO0oo0oO0.I11iii11IIi
        if 42 - 42: ooO0oo0oO0 % oooO0oo0oOOOO / OoO0O00 - oooO0oo0oOOOO * i11iIiiIii
        if 19 - 19: oooO0oo0oOOOO * I1IiiI % i11iIiiIii
        I1ii11 = [350, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
        IiII111i1i11 = []
        for iI in I1ii11:
            for OOOO in range(0, 4):
                IiII111i1i11.append('%s/random%sx%s.jpg' %
                                    (os.path.dirname(IIIIiIiIi1['url']), iI, iI))
        self.imgGauge.setVisible(True)
        time.sleep(1)
        self.configGauge(0)
        self.imgGauge_arrow.setVisible(True)
        if 24 - 24: o0oOOo0O0Ooo
        oo0.append('Testing download speed...')
        self.update_textbox(oo0)
        if not simple:
            Ii11iI1i('Testing download speed', end='')
        i1III = self.downloadSpeed(IiII111i1i11, simple)
        if not simple:
            Ii11iI1i()
        oo0.append('Download: %0.2f M%s/s' % ((i1III / 1000 / 1000) * units[1], units[0]))
        self.update_textbox(oo0)
        self.dl_textbox.setLabel("%.2f" % float((i1III / 1000 / 1000) * units[1]))
        Ii11iI1i('Download: %0.2f M%s/s' %
                 ((i1III / 1000 / 1000) * units[1], units[0]))
        self.configGauge(0, (i1III / 1000 / 1000) * 8, time=3000)
        time.sleep(2)
        if 10 - 10: o0oOOo0O0Ooo % II1Ii1iI1i / ooO0oo0oO0
        if 28 - 28: ooO0oo0oO0 % OOO0O
        if 48 - 48: i11iIiiIii % oooO0oo0oOOOO
        Ii1i1iI = [int(.25 * 1000 * 1000), int(.5 * 1000 * 1000)]
        I1ii11 = []
        for iI in Ii1i1iI:
            for OOOO in range(0, 25):
                I1ii11.append(iI)
                if 29 - 29: o0oOoO00o + i11iIiiIii % i111I
        oo0.append('Testing upload speed...')
        self.update_textbox(oo0)
        if not simple:
            Ii11iI1i('Testing upload speed', end='')
        ooo0o00 = self.uploadSpeed(IIIIiIiIi1['url'], I1ii11, simple)
        if not simple:
            Ii11iI1i()
        oo0.append('Upload: %0.2f M%s/s' % ((ooo0o00 / 1000 / 1000) * units[1], units[0]))
        self.update_textbox(oo0)
        self.ul_textbox.setLabel("%.2f" % float((ooo0o00 / 1000 / 1000) * units[1]))
        Ii11iI1i('Upload: %0.2f M%s/s' %
                 ((ooo0o00 / 1000 / 1000) * units[1], units[0]))
        self.configGauge(0, (ooo0o00 / 1000 / 1000) * 8, time=3000)
        time.sleep(2)
        if 93 - 93: OoOoOO00 % iIii1I11I1II1
        if share and mini:
            Ii11iI1i('Cannot generate a speedtest.net share results image while '
                     'testing against a Speedtest Mini server')
        elif share:
            I11 = int(round((i1III / 1000) * 8, 0))
            IIi = int(round(IIIIiIiIi1['latency'], 0))
            oOoO00oo0O = int(round((ooo0o00 / 1000) * 8, 0))
            if 90 - 90: I1IiiI - ooO0oo0oO0 / II1Ii1iI1i / O0 / i111I
            if 87 - 87: OoOoOO00 / I11iii11IIi + iIii1I11I1II1
            if 93 - 93: iIii1I11I1II1 + oooO0oo0oOOOO % OOO0O
            if 21 - 21: ooO0oo0oO0
            OOO0oOOoo = [
                'download=%s' % I11,
                'ping=%s' % IIi,
                'upload=%s' % oOoO00oo0O,
                'promo=',
                'startmode=%s' % 'pingselect',
                'recommendedserverid=%s' % IIIIiIiIi1['id'],
                'accuracy=%s' % 1,
                'serverid=%s' % IIIIiIiIi1['id'],
                'hash=%s' % md5(('%s-%s-%s-%s' %
                                 (IIi, oOoO00oo0O, I11, '297aae72'))
                                .encode()).hexdigest()]
            if 6 - 6: I11iii11IIi
            OOOoOO = {'Referer': 'https://c.speedtest.net/flash/speedtest.swf'}
            O0OOo00oo0oOo = O0ooo0O0oo0('https://www.speedtest.net/api/api.php',
                                        data='&'.join(OOO0oOOoo).encode(),
                                        headers=OOOoOO)
            OoOo0o = Ii(O0OOo00oo0oOo)
            if OoOo0o is False:
                Ii11iI1i('Could not submit results to speedtest.net')
                return False
            Oo000ooOOO = OoOo0o.read()
            Ii11i1I11i = OoOo0o.code
            OoOo0o.close()
            if 46 - 46: I11iii11IIi + oooO0oo0oOOOO
            if int(Ii11i1I11i) != 200:
                Ii11iI1i('Could not submit results to speedtest.net')
                return False
                if 79 - 79: OoooooooOO - I11iii11IIi * I11iii11IIi.OoOoOO00
            IiIi1iIIi1 = parse_qs(Oo000ooOOO.decode())
            O0OoO0ooOO0o = IiIi1iIIi1.get('resultid')
            if not O0OoO0ooOO0o or len(O0OoO0ooOO0o) != 1:
                Ii11iI1i('Could not submit results to speedtest.net')
                return False
                if 100 - 100: II111iiii * i111I % I1IiiI / I1ii11iIi11i
            Ii11iI1i('Share results: https://www.speedtest.net/result/%s.png' %
                     O0OoO0ooOO0o[0])
            global O00o0o0000o0o
            if 90 - 90: I1ii11iIi11i.OOO0O.OoOoOO00.II1Ii1iI1i
            if not os.path.isdir(iI1Ii11111iIi):
                os.mkdir(iI1Ii11111iIi)
            self.image_result = os.path.join(iI1Ii11111iIi, '%s.png' % O0OoO0ooOO0o[0])
            OOOoOO = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            O0ooOo0o0Oo = Request('https://www.speedtest.net/result/%s.png' % O0OoO0ooOO0o[0], headers=OOOoOO)
            OooO0oOo = urlopen(O0ooOo0o0Oo).read()
            oOOo00O0OOOo = open(self.image_result, 'w+')
            oOOo00O0OOOo.write(OooO0oOo)
            oOOo00O0OOOo.close()
            oo0.append('Results saved: %s' % self.image_result)
            self.update_textbox(oo0)
            print oo0
            if 4 - 4: II1Ii1iI1i + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
            if 74 - 74: II111iiii.O0 - I1IiiI + I11iii11IIi % i11iIiiIii % OoOoOO00
            if 78 - 78: II1Ii1iI1i + OoOoOO00 + I11iii11IIi - I11iii11IIi.i11iIiiIii / OoO0O00


if __name__ == '__main__':
    if 27 - 27: II1Ii1iI1i - O0 % i111I * o0ooo.I11iii11IIi % iIii1I11I1II1
    if 37 - 37: OoooooooOO + O0 - i1IIi % OOO0O
    oO0o00ooO = oO0ooOO("main.xml", o0OOO.getAddonInfo('path'), "Default")
    if 24 - 24: OoOoOO00
    del oO0o00ooO
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
