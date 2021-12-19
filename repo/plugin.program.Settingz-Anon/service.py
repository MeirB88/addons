#!/usr/bin/python

import os
import sys,re
import xbmc,time,json
import xbmcaddon,logging,hashlib, xbmcvfs

import log


logging.warning('start Log POPUP')



update_time=1
sleep_time = 1000
last_run=0

nameSelect=[]
logSelect=[]
import glob
try:
    folder = xbmc.translatePath('special://logpath')
except:
    folder = xbmc.translatePath('special://logpath')
xbmc.log(folder)
for file in glob.glob(folder+'/*.log'):
        try:nameSelect.append(file.rsplit('\\', 1)[1].upper())
        except:nameSelect.append(file.rsplit('/', 1)[1].upper())
        logSelect.append(file)
log_size=0
log_size_prev=0
while not xbmc.abortRequested:
    if(time.time() > last_run + update_time):
                      now = time.time()
                      last_run = now - (now % update_time)
                      # settings = xbmcaddon.Addon(id='plugin.program.LogPopup')
                      # df = settings.getSetting("popup")
                      # enable_debug_notice= settings.getSetting("debug")
                      #log_size = int(os.path.getsize(logSelect[0]))
                      file = open(logSelect[0], 'r') 
                      file_data=file.read() 
                      match=re.compile('Error Type:(.+?)-->End of Python script error report<--',re.DOTALL).findall(file_data)
                      match2=re.compile('CAddonInstallJob(.+?)$', re.M).findall(file_data)
                      match3=re.compile('ERROR: WARNING:root:(.+?)$', re.M).findall(file_data)
                      # if (enable_debug_notice)=='false':
                      match3=[]
                      log_size=len(match+match2+match3)
                      if log_size>log_size_prev :
                        log_size_prev=log_size
                        try:
                          logsend
                        except:
                         pass

    xbmc.sleep(1000)


