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
import sublib.iso639


class model(object):
    '''Factory class that defines a found subtitle.

    Params:
        label  : (required,string) Label to be shown on found subtitles
        iso    : (required, 2 letter iso639-1 country code) localization of
            the subtitle
        rating : (optional[0], 0 <= integer <=4 ) rating of the subtitle
        sync   : (optional[False], Bool) bool flag that determines if it is the
            exact match
        cc     : (optional[False],Bool) bool flag that determines if it is a closed
            caption
        priorty: (optional[0],int) higher the value is, topper the result is
            shown in gui, note that preffered language sorting is done
            automatically and not to be considered as a part of this value.

    Attributes:

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

    Returns:
        subtitle instance
    '''
    @property
    def label(self):
        '''Label to be shown on found subtitles'''
        return self.__label

    @property
    def iso(self):
        '''(2 letter iso639-1 country code): localization of the subtitle'''
        return self.__iso

    @property
    def sync(self):
        '''bool flag that determines if it is the exact match'''
        return self.__sync

    @property
    def cc(self):
        '''bool flag that determines if it is a closed caption'''
        return self.__cc

    @property
    def rating(self):
        '''(0 <= integer <=5 ): rating of the subtitle'''
        return self.__rating

    @property
    def args(self):
        '''Arguments to be passed to self.download method of service'''
        return self.__args

    @property
    def kwargs(self):
        '''Keyword arguments to be passed to self.download method of service'''
        return self.__kwargs

    @property
    def priority(self):
        '''Priority of the subtitle in the shown list'''
        return self.__priority

    @label.setter
    def label(self, val):
        if not isinstance(val, (str, unicode)):
            raise(TypeError(type(val)))
        self.__label = val

    @iso.setter
    def iso(self, val):
        val = val.lower().strip()
        twolet = val in sublib.iso639.one
        human = val in sublib.iso639.one.values()
        if not twolet and not human:
            raise(ValueError(val))
        if twolet:
            self.__iso = val
        if human:
            for k, v in sublib.iso639.one.iteritems():
                if  v == val:
                    self.__iso = k
                    break

    @cc.setter
    def cc(self, val):
        if not isinstance(val, bool):
            raise(TypeError(type(val)))
        self.__cc = val

    @sync.setter
    def sync(self, val):
        if not isinstance(val, bool):
            raise(TypeError(type(val)))
        self.__sync = val

    @rating.setter
    def rating(self, val):
        if not isinstance(val, int):
            raise(TypeError(type(val)))
        if val < 0 or val > 5:
            raise(ValueError(val))
        self.__rating = val

    @priority.setter
    def priority(self, val):
        if not isinstance(val, int):
            raise(TypeError(type(val)))
        self.__priority = val

    def __init__(self, label, iso, rating=0, sync=False, cc=False, priority=0):
        self.__label = None
        self.__iso = None
        self.rating = rating
        self.label = label
        self.iso = iso
        self.sync = sync
        self.priority = priority
        self.cc = cc
        self.__args = []
        self.__kwargs = {}

    def download(self, *args, **kwargs):
        '''The arguments sent to this method will be pushed to self.download
        method of the service

        Params:
            *args: arguments to be passed
            **kwargs: keyword arguments to be passed
        '''
        self.__args = args
        self.__kwargs = kwargs

    def _ispreffered(self, iso):
        return int(self.__iso == iso)

    def __repr__(self):
        return repr({
                     "label": self.__label,
                     "iso": self.__iso,
                     "rating": self.__rating,
                     "sync": self.__sync,
                     "cc": self.__cc,
                     "args": self.__args,
                     "kwargs": self.__kwargs
                     })


class sorter(object):
    def __init__(self, piso):
        self.piso = piso

    def method(self, ob):
        # first sort by user preffered lang.
        # then sort by service priority
        # then sort by subtitle rating
        return int(ob.iso == self.piso), ob.sync, ob.priority, ob.rating
