#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcaddon
import xbmc
import xbmcvfs
import xbmcgui
import gzip
import os
import sys
import base64
import time
from StringIO import StringIO

id = 'service.rytecepgdownloader'
addon = xbmcaddon.Addon(id=id)

def log(msg, level=xbmc.LOGNOTICE):
    xbmc.log(str(msg), level)

def manual_download():
    manual_download = False
    try:
        if sys.argv[1:][0] == 'manual_download':
            manual_download = True
    except:
        pass
    return manual_download
    
def get_descriptions():
    descriptions = []
    set = [ addon.getSetting('xmltv_rytec_1'), 
            addon.getSetting('xmltv_rytec_2'), 
            addon.getSetting('xmltv_rytec_3'), 
            addon.getSetting('xmltv_rytec_4'), 
            addon.getSetting('xmltv_rytec_5'), 
            addon.getSetting('xmltv_url_1'),
            addon.getSetting('xmltv_url_2'),
            addon.getSetting('xmltv_url_3'),
            addon.getSetting('xmltv_url_4'),
            addon.getSetting('xmltv_url_5')
            ]
    for s in set:
        if s:
            if not s == 'None' or s.startswith('http'):
                descriptions.append(s)
    return descriptions

def load_local_xml(epg_url):
    ret = False
    name = epg_url.split('/')[-1]
    xml_file = get_xml_file(name)
    if xbmcvfs.exists(xml_file):
        ret = check_date(xml_file)
    return ret

def get_description_url(description):
    epg_url = None
    try:
        epg_url = bdecode(addon.getSetting(description))
    except:
        log('[Rytec EPG Downloader]: no epg url found in settings')
        log(description)
    return epg_url

def save_epg_url(epg_url, description):
    addon.setSetting(description, bencode(epg_url))

def get_xml_path():
    xml_path = addon.getSetting('path').decode('utf-8')
    if not xml_path:
        addon.openSettings()
        xml_path = addon.getSetting('path').decode('utf-8')
    return xml_path

def get_merged():
    xml_path = get_xml_path()
    merged = os.path.join(xml_path,'merged_epg.xml.gz')
    if xbmcvfs.exists(merged):
        xbmcvfs.delete(merged)
    return merged
    
def get_temp_merged():
    datapath = xbmc.translatePath('special://temp')
    temp = os.path.join(datapath,'temp')
    if not xbmcvfs.exists(temp):
        xbmcvfs.mkdir(temp)
    temp_merged = os.path.join(temp, 'merged_epg.xml.gz')
    return temp_merged

def copy_temp_merged():
    merged = get_merged()
    temp_merged = get_temp_merged()
    xbmcvfs.copy(temp_merged, merged)

def delete_temp_merged():
    temp_merged = get_temp_merged()
    if xbmcvfs.exists(temp_merged):
        xbmcvfs.delete(temp_merged)

def get_xml_file(name):
    xml_path = get_xml_path()
    xml_file = os.path.join(xml_path, name)
    return xml_file

def bencode(original_string):
    encoded_string = base64.b64encode(original_string)
    return encoded_string

def bdecode(encoded_string):
    decoded_string = base64.b64decode(encoded_string)
    return decoded_string

def check_date(file):
    cache_days = 3
    st = xbmcvfs.Stat(file)
    modified = st.st_mtime()
    current = round(time.time())
    t = current - modified
    if (t / 3600) < 24*cache_days:
        return True

def download_allowed(a):
    gmt = time.gmtime()
    if gmt.tm_hour > 2 and gmt.tm_hour < 7:
        if not a:
            log('[Rytec EPG Downloader]: epg download not allowed between 3 and 7 GMT')
        return False
    else:
        return True
        
def get_counter():
    counter = addon.getSetting('counter')
    if not counter:
        counter = '0'
    return counter

def blocked(a):
    counter = int(get_counter())
    ct = round(time.time())
    if counter == 0:
        counter += 1
        addon.setSetting('counter', str(counter))
        addon.setSetting('bt', str(ct).split('.')[0])
        return False
    elif counter == 1:
        counter += 1
        addon.setSetting('counter', str(counter))
        return False
    elif counter > 1:
        bt = int(addon.getSetting('bt'))
        t = ct - bt
        if (t / 3600) > 23:
            addon.setSetting('counter', '0')
            return False
        else:
            if not a:
                log('[Rytec EPG Downloader]: %sh blocked' % (24 - (t / 3600)))
            return True
    else:
        return True

def get_activation_code():
    ac = addon.getSetting('ac')
    if bencode(ac) == 'MzAyNQ==':
        return True
    else:
        addon.openSettings()
        ac = addon.getSetting('ac')
        if bencode(ac) == 'MzAyNQ==':
            return True
        else:    
            return False

def merge_epg():
    xml_path = get_xml_path()
    temp_merged = get_temp_merged()
    ltw = None
    
    log('[Rytec EPG Downloader]: start merging files')
    dirs, files = xbmcvfs.listdir(xml_path)
    i=1
    total = len(files)
    for xmltv in files:
        if (xmltv.endswith('.gz') or xmltv.endswith('.xml') or xmltv.endswith('.xz')) and not xmltv.startswith('merged_epg.xml'):
            try:
                if xmltv.endswith('.gz'):
                    inF = gzip.GzipFile(fileobj=StringIO(xbmcvfs.File(os.path.join(xml_path,xmltv)).read()))
                elif xmltv.endswith('.xz'):
                    try:
                        import lzma
                    except ImportError:
                        from backports import lzma
                    inF = lzma.open(xbmcvfs.File(os.path.join(xml_path,xmltv)), 'rb')
                else:
                    inF = xbmcvfs.File(os.path.join(xml_path,xmltv))
                b = inF.read()
                inF.close()
                b = b.replace('</tv>','')
                if i==1:
                    ltw = b.splitlines()
                else:
                    lines = b.splitlines()
                    li = 0
                    for line in lines:
                        if li == 0 or li == 1: 
                            pass
                        else: 
                            ltw.append(line)
                        li += 1
                i += 1
            except Exception as e:
                log('[Rytec EPG Downloader]: error in merge epg')
                log(xmltv)
                log(e)
    
    if ltw:
        f_in = '\n'.join(ltw)
        f_in = f_in+'</tv>'
        f_out = gzip.open(temp_merged, 'wb')
        f_out.write(f_in)
        f_out.close()

    log('[Rytec EPG Downloader]: merging files done')