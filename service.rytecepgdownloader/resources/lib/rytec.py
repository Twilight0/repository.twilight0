#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import gzip
import re
import random
import xbmc
import xbmcvfs
import xml.etree.ElementTree as ET
from StringIO import StringIO
import common


class RYTEC:

    def __init__(self):
    
        self.epgsources  = 'aHR0cDovL2VwZ2FsZmFzaXRlLmR5bmRucy50di9rb2RpLWVwZ3NvdXJjZXM='
        self.headers     = {'User-Agent': 'Rytec EPG Downloader by Jin'}

    def get_sources_list(self):
    
        common.log('[Rytec EPG Downloader]: get sources list')
        
        sources_list = []
        
        try:
            r = requests.get(common.bdecode(self.epgsources), headers=self.headers)
            if r.status_code == 200:
                sources_list = r.text.splitlines()
                random.shuffle(sources_list)
                #sources_list = gzip.GzipFile(fileobj=StringIO(r.content)).read().splitlines()
        except Exception as e:
            common.log('[Rytec EPG Downloader]: error in get sources list')
            common.log(e)
            
        return sources_list
            
    def get_epg(self, source, description):
    
        common.log('[Rytec EPG Downloader]: get epg')
        ret     = False
        epg_url = None
        
        data    = self.get_source(source)
        if data:
            epg_url = self.get_epg_url(data, description)
        if epg_url:
            ret = self.download_epg(epg_url)
                
        if ret and epg_url:
            self.save_epg_url(epg_url, description)
                
        return ret
        
    def get_source(self, source):
    
        common.log('[Rytec EPG Downloader]: get source')
        data = ''
        
        try:
            data = requests.get(source, headers=self.headers).text
        except Exception as e:
            common.log('[Rytec EPG Downloader]: error in get source')
            common.log(e)
            
        return data

    def get_epg_url(self, data, description):
    
        common.log('[Rytec EPG Downloader]: get epg url')
        epg_url = None
        
        try:
            root = ET.fromstring(data)
            for source in root.findall('source'):
                sd = source.find('description').text
                url = source.find('url').text
                if description == sd:
                    epg_url = url
                    break
        except Exception as e:
            common.log('[Rytec EPG Downloader]: error in get epg url')
            common.log(e)
            
        return epg_url
            
    def download_epg(self, epg_url):
    
        common.log('[Rytec EPG Downloader]: download epg')
        ret = False
        
        try:
            name = epg_url.split('/')[-1]
            xml_file = common.get_xml_file(name)
            from contextlib import closing
            with closing(requests.get(epg_url, headers=self.headers, stream=True)) as r:
                if r.status_code == 200:
                    if 'application/' in r.headers['content-type'] or 'text/xml' in r.headers['content-type']:
                        common.log('[Rytec EPG Downloader]: epg download started')
                        f = xbmcvfs.File(xml_file, 'wb')
                        for chunk in r.iter_content(chunk_size=1024): 
                            if chunk:
                                f.write(chunk)
                            else:
                                common.log('[Rytec EPG Downloader]: epg download failed')
                                break
                                return ret
                        common.log('[Rytec EPG Downloader]: epg download complete')
                        f.close()
                        ret = True
                else:
                    common.log('[Rytec EPG Downloader]: epg url offline')
                    common.log('%s - %s' % (str(r.status_code), str(r.headers)))
        except Exception as e:
            common.log('[Rytec EPG Downloader]: error in download epg')
            common.log(e)
            
        return ret
        
    def save_epg_url(self, epg_url, description):
    
        common.log('[Rytec EPG Downloader]: save epg url to config')
        
        try:
            common.save_epg_url(epg_url, description)
        except Exception as e:
            common.log('[Rytec EPG Downloader]: could not write url to config')
            common.log(e)