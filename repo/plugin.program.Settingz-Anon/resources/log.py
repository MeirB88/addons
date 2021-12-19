import xbmcaddon,os,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin,sys, xbmcvfs
import traceback,json
import logging,shutil,glob
import HTMLParser,time
from shutil import copyfile
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    translatepath=xbmc.translatePath

else:
    translatepath=xbmcvfs.translatePath
HOME           = translatepath('special://home/')
ADDONS         = os.path.join(HOME,     'addons')
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
def logsend():
        Addon = xbmcaddon.Addon()
        user_dataDir_pre = translatepath(Addon.getAddonInfo("profile")).decode("utf-8")


        nameSelect=[]
        logSelect=[]
        import glob
        folder = translatepath('special://logpath')
        xbmc.log(folder)
        for file in glob.glob(folder+'/*.log'):
            try:nameSelect.append(file.rsplit('\\', 1)[1].upper())
            except:nameSelect.append(file.rsplit('/', 1)[1].upper())
            logSelect.append(file)
            
        
        file = open(logSelect[0], 'r') 
        home1=translatepath("special://home/")
        home2=translatepath("special://home/").replace('\\','\\\\')
        home3=translatepath("special://xbmc/")
        home4=translatepath("special://xbmc/").replace('\\','\\\\')
        home5=translatepath("special://masterprofile/")
        home6=translatepath("special://masterprofile/").replace('\\','\\\\')
        home7=translatepath("special://profile/")
        home8=translatepath("special://profile/").replace('\\','\\\\')
        home9=translatepath("special://temp/")
        home10=translatepath("special://temp/").replace('\\','\\\\')
        file_data=file.read().replace(home1,'').replace(home2,'').replace(home3,'').replace(home4,'').replace(home5,'').replace(home6,'').replace(home7,'').replace(home8,'').replace(home9,'').replace(home10,'')
        match=re.compile('Error Type:(.+?)-->End of Python script error report<--',re.DOTALL).findall(file_data)
        match2=re.compile('CAddonInstallJob(.+?)$', re.M).findall(file_data)
        match3=re.compile('ERROR: WARNING:root:(.+?)$', re.M).findall(file_data)
        n=0
        line_numbers=[]
        file = open(logSelect[0], 'r') 
        file_data=file.readlines() 
        match_final=[]
        x=0
        y=0
        z=0
        for  line in (file_data):
         
         if 'Error Type:' in line:
          match_final.append(match[x])
          x=x+1
          line_numbers.append(n)
         elif 'CAddonInstallJob' in line:
          match_final.append(match2[y])
          y=y+1
         # elif 'ERROR: WARNING:root:' in line :#and enable_debug_notice=='true':
          # match_final.append(match3[z])
          # z=z+1

        if (len(match_final))>0:
          # dialog = xbmcgui.DialogBusy()
          # dialog.create()
            file = open(os.path.join(user_dataDir_pre, 'log.txt'), 'w') 
            file.write('\n'.join(match_final))
            file.close()
            if not os.path.exists(translatepath("special://home/addons/") + 'script.module.requests'):
              xbmc.executebuiltin("RunPlugin(plugin://script.module.requests)")
          #  break
            howsentlog()
            import requests
            docu=xbmc . translatePath ( 'special://profile/addon_data/plugin.program.Settingz-Anon/log.txt')
            files = {
            'chat_id': (None, '-274262389'),
            'document': (docu, open(docu, 'rb')),
            }
            t='aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDk2Nzc3MjI5NzpBQUhndG1zWEotelVMakM0SUFmNHJKc0dHUlduR09ZaFhORS9zZW5kRG9jdW1lbnQ='
            response = requests.post(t.decode('base64'), files=files)


