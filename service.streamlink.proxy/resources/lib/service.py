"""
Modified for Streamlink
https://github.com/neverreply/service.streamlink.proxy
---

XBMCLocalProxy 0.1
Copyright 2011 Torben Gerkensmeyer

Modified for Livestreamer by your mom 2k15

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

import os
# import shutil
import socket
import sys
import traceback
import urlparse

from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from simpleplugin import Plugin
from streamlink import Streamlink

import xbmc
import xbmcgui
import xbmcaddon


__settings__ = xbmcaddon.Addon(id='service.streamlink.proxy')
__language__ = __settings__.getLocalizedString

_path_streamlink_plugins_ = os.path.join('service.streamlink.plugins', 'plugins')
_path_streamlink_service_ = os.path.join('service.streamlink.proxy', 'resources', 'lib')

_path_kodi_folder_ = os.path.dirname(os.path.realpath(__file__))
_neverreply_plugins_ = _path_kodi_folder_.replace(_path_streamlink_service_, _path_streamlink_plugins_)

plugin = Plugin()


class MyHandler(BaseHTTPRequestHandler):
    """
    Serves a HEAD request
    """
    def do_HEAD(self):
        plugin.log_debug('Serving HEAD request...')
        self.answer_request(0)

    """
    Serves a GET request.
    """
    def do_GET(self):
        plugin.log_debug('Serving GET request...')
        self.answer_request(1)

    def answer_request(self, sendData):
        try:
            p = urlparse.urlparse(self.path)
            try:
                params = dict(urlparse.parse_qsl(p.query))
            except:
                params = {}

            if p.path == "/stop":
                sys.exit()
            elif p.path == "/version":
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Proxy: Running\r\n")
                self.wfile.write("Version: 0.1")
            elif p.path == '/':
                self.serveFile(params, sendData)
            elif p.path == '/channel.m3u8':
                self.redirectURL(params, sendData)
            else:
                self.send_response(403)
        except:
                traceback.print_exc()
                self.wfile.close()
                return
        try:
            self.wfile.close()
        except:
            pass

    def redirectURL(self, params, sendData):
        if (sendData):
            url = params.get('url')

            if not url:
                xbmcgui.Dialog().notification(__language__(30202), __language__(30200), xbmcgui.NOTIFICATION_WARNING)
                return []

            quality = params.get('q', 'best')

            session = Streamlink()
            # custom streamlink plugins
            session.load_plugins(_neverreply_plugins_)

            # <!-- ZATTOO
            if url.startswith(('https://zattoo.com', 'https://tvonline.ewe.de', 'https://nettv.netcologne.de')):
                plugin_email = plugin.get_setting('zattoo_email')
                plugin_password = plugin.get_setting('zattoo_password')

                if plugin_email and plugin_password:
                    plugin.log_debug('Found Zattoo login')
                    session.set_plugin_option('zattoo', 'email', plugin_email)
                    session.set_plugin_option('zattoo', 'password', plugin_password)
                else:
                    plugin.log_debug('Missing Zattoo login')
            # ZATTOO -->

            try:
                streams = session.streams(url)
            except Exception:
                traceback.print_exc(file=sys.stdout)
                self.send_response(403)

            plugin.log_debug('Sending data...')

            try:
                stream = streams.get(quality)

                if not stream:
                    self.send_error(404, 'Stream Not Found')
                    return

                self.send_response(301)
                self.send_header('Location', stream.url)
                self.end_headers()
                return
            except:
                traceback.print_exc()
                self.wfile.close()
                return

    """
    Sends the requested file and add additional headers.
    """
    def serveFile(self, params, sendData):
        if (sendData):
            url = params.get('url')

            if not url:
                xbmcgui.Dialog().notification(__language__(30202), __language__(30200), xbmcgui.NOTIFICATION_WARNING)
                return []

            quality = params.get('q', 'best')

            session = Streamlink()
            # custom streamlink plugins
            session.load_plugins(_neverreply_plugins_)

            # <!-- ZATTOO
            if url.startswith(('https://zattoo.com', 'https://tvonline.ewe.de', 'https://nettv.netcologne.de')):
                plugin_email = plugin.get_setting('zattoo_email')
                plugin_password = plugin.get_setting('zattoo_password')

                if plugin_email and plugin_password:
                    plugin.log_debug('Found Zattoo login')
                    session.set_plugin_option('zattoo', 'email', plugin_email)
                    session.set_plugin_option('zattoo', 'password', plugin_password)
                else:
                    plugin.log_debug('Missing Zattoo login')
            # ZATTOO -->

            try:
                streams = session.streams(url)
            except Exception:
                traceback.print_exc(file=sys.stdout)
                self.send_response(403)
            self.send_response(200)
            plugin.log_debug('Sending headers...')
            self.end_headers()

            plugin.log_debug('Sending data...')
            fileout = None
            fileout = self.wfile
            try:
                stream = streams.get(quality)

                if not stream:
                    self.send_error(404, 'Stream Not Found')
                    return

                """fileout = None
                try:
                    fileout = stream.open()
                    shutil.copyfileobj(fileout, self.wfile)
                finally:
                    if fileout:
                        fileout.close()
                """
                try:
                    response = stream.open()
                    buf = 'INIT'
                    while (buf is not None and len(buf) > 0):
                        buf = response.read(5000 * 1024)
                        fileout.write(buf)
                        fileout.flush()
                    response.close()
                    fileout.close()
                    plugin.log_debug('Closing connection')
                except socket.error:
                    plugin.log_debug('Client Closed the connection.')
                    try:
                        response.close()
                        fileout.close()
                    except Exception:
                        return
                except Exception:
                    traceback.print_exc(file=sys.stdout)
                    response.close()
                    fileout.close()
            except:
                traceback.print_exc()
                self.wfile.close()
                return
        else:
            self.send_response(200)
            plugin.log_debug('Sending headers 2 ...')
            self.end_headers()
        try:
            self.wfile.close()
        except:
            pass


class Server(HTTPServer):
    """HTTPServer class with timeout."""

    def get_request(self):
        """Get the request and client address from the socket."""
        self.socket.settimeout(5.0)
        result = None
        while result is None:
            try:
                result = self.socket.accept()
            except socket.timeout:
                pass
        result[0].settimeout(1000)
        return result


class ThreadedHTTPServer(ThreadingMixIn, Server):
    """Handle requests in a separate thread."""
    allow_reuse_address = True

HOST = '127.0.0.1'
PORT = plugin.get_setting('listen_port', int)

if __name__ == '__main__':
    sys.stderr = sys.stdout
    server_class = ThreadedHTTPServer
    httpd = server_class((HOST, PORT), MyHandler)

    plugin.log_notice('Server Starts - {0} on port {1}'.format(HOST, PORT))
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        httpd.handle_request()
        if monitor.waitForAbort(1):
            break

httpd.server_close()
plugin.log_notice('Server Stops - {0} on port {1}'.format(HOST, PORT))
