#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc, xbmcgui
from resources.lib import common
from resources.lib.rytec import RYTEC
rytec = RYTEC()

class DOWNLOADER:

    def __init__(self, manual=False):
    
        common.log('[Rytec EPG Downloader]: rytec downloader started')
        self.manual       = manual
        self.sources_list = []
        self.i            = 0
        
        self.descriptions = common.get_descriptions()
        self.len_desc     = len(self.descriptions)
        if self.len_desc == 0:
            common.log('[Rytec EPG Downloader]: empty epg setting')
            return
        self.upd          = 60/self.len_desc
            
        self.progress('create', '', 'Rytec EPG Downloader', '', 'Downloading XML Data')
        self.run()
            
    def get_epg_url(self, description):
    
        if description.startswith('http'):
            epg_url = description
        else:
            epg_url = common.get_description_url(description)
            
        return epg_url
        
    def download_epg(self, description, epg_url):
    
        ret = common.load_local_xml(epg_url)
        if ret:
            common.log('[Rytec EPG Downloader]: no epg update needed')
        else:
            if description.startswith('http'):
                if self.manual == True:
                    ret = rytec.download_epg(epg_url)
            if self.manual == False:
                ret = rytec.download_epg(epg_url)
                
        return ret
        
    def run_rytec(self, description):
        ret = False
        if not self.sources_list: 
            self.sources_list = rytec.get_sources_list()
         
        for source in self.sources_list:
            ret = rytec.get_epg(source, description)
            if ret:
                break
        return ret
        
    def run(self):
    
        for description in self.descriptions:
    
            common.log('[Rytec EPG Downloader]: '+description)
            self.i += self.upd
            self.progress('update', self.i, 'Rytec EPG Downloader', description, 'Downloading XML Data')
            ret = False
            epg_url = self.get_epg_url(description)
            
            if epg_url:
                ret = self.download_epg(description, epg_url)
                
            if not ret and not description.startswith('http'):
                ret = self.run_rytec(description)
                
        self.progress('update', 70, 'Merging XML Data', ' ', 'Please Wait...This May Take Awhile')
                
        if self.len_desc > 1:
            common.merge_epg()
            self.progress('update', 90, 'Merging XML Data', ' ', 'Please Wait...This May Take Awhile')
            common.copy_temp_merged()
            common.delete_temp_merged()
        
        self.progress('close', '', '', '', '')
        
        if self.manual:
            if ret:
                ok = dialog.ok('Rytec EPG Downloader', 'Manual Download Finished')
            else:
                ok = dialog.ok('Rytec EPG Downloader', 'Manual Download Failed')
            
    def progress(self, method, i, line1, line2, line3):
    
        if self.manual:
        
            if method == 'create':
                self.pDialog = xbmcgui.DialogProgress()
                self.pDialog.create(line1, line2, line3)
            elif method == 'update':
                self.pDialog.update(i, line1, line2, line3)
            elif method == 'close':
                self.pDialog.close()
            else:
                pass

def service():

    monitor  = xbmc.Monitor()
    a        = False
    
    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            break
            
        if not (xbmc.Player().isPlaying() or xbmc.getCondVisibility('Library.IsScanningVideo')):
            if common.download_allowed(a):
                if not common.blocked(a):
                    DOWNLOADER()
            a = True

if __name__ == '__main__':
    
    if common.get_xml_path() and common.get_activation_code():

        if common.manual_download() == True:
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Rytec EPG Downloader', 'Start Manual Download')
            if ret:
                manual = True
                DOWNLOADER(manual)
        else:
            service()