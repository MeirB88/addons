# -*- coding: utf-8 -*-
import time
import xbmc,xbmcaddon
import os
import xbmcgui

import webbrowser
import xbmc
import json
import sys
__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
		function4,
		function5,
		function6,
		#function7,
		#function8,
		#function9,
		#function10,
		#function11,
		#function12,
		#function13,
		#function14,
		#function15,
		#function16,
		#function17,
		#function18,
		#function19,
		#function20,
		#function21
        )
        
    call = dialog.select('[COLOR darkorchid]כלים - MBTV[/COLOR]', [
           '[COLOR white] הגדרת IPTV [/COLOR]' ,
           '[COLOR gold] תחזוקה (וויזארד)[/COLOR]'
           
	 ])
    if call:
        # esc is not preGolded
        if call < 0:
            return
        func = funcs[call-6]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def function1(): 
    xbmc.executebuiltin("RunPlugin(plugin://pvr.iptvsimple)")
    
def function2(): 
    xbmc.executebuiltin("RunPlugin(plugin://plugin.program.meirwizard/?mode=maint)")

       
    

  

      
		
 
menuoptions()
