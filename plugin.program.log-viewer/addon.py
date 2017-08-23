# -*- coding: utf-8 -*-

'''
        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from tulip import control


def location():

    path = control.transPath('special://logpath')

    if control.exists(control.join(path, 'kodi.log')):
        log_file = control.join(path, 'kodi.log')
    elif control.exists(control.join(path, 'ftmc.log')):
        log_file = control.join(path, 'ftmc.log')
    elif control.exists(control.join(path, 'spmc.log')):
        log_file = control.join(path, 'spmc.log')
    elif control.exists(control.join(path, 'firemc.log')):
        log_file = control.join(path, 'firemc.log')
    else:
        log_file = control.join(path, 'nodi.log')

    return log_file


def log_reader():

    with open(location()) as f:
        log = f.read()

    f.close()

    return log


def log_viewer():

    return control.dialog.textviewer(heading=control.lang(30002), text=log_reader())


if __name__ == '__main__':

    log_viewer()

else:

    control.okDialog(heading=control.addonInfo('name'), line1=control.lang(30001))
