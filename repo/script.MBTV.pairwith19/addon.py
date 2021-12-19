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
		function7,
		function8,
		function9,
		function10,
		function11,
		function12,
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
        
    call = dialog.select('[COLOR darkorchid]תפריט אימות - MBTV[/COLOR]', [
	'[COLOR=Gold]===אימות חשבון RD===[/COLOR]',
	'[COLOR=White]FEN[/COLOR]',
	'[COLOR=White]SEREN[/COLOR]',
	'[COLOR=White]THE CREW[/COLOR]',
	'[COLOR=White]THE OATH[/COLOR]',
	'[COLOR=Gold]===אימות חשבון טראקט[/COLOR]',
	'[COLOR=White]FEN[/COLOR]',
	'[COLOR=White]SEREN[/COLOR]',
	'[COLOR=White]THE CREW[/COLOR]',
	'[COLOR=White]THE OATH[/COLOR]',
    '[COLOR=Gold]===טלמדיה===[/COLOR]',
    '[COLOR=White]אימות חשבון טלמדיה[/COLOR]', ])
    if call:
        # esc is not preGolded
        if call < 0:
            return
        func = funcs[call-12]
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

def function1(): 0
    
def function2():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.fen/?mode=myaccounts.open&amp;query=1.21)")

	
def function3():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.seren/?action=authRealDebrid)")
    

def function4():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.thecrew/?action=authTrakt)")
    
      
def function5():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.theoath/?action=authTrakt)")
      

def function6(): 0
    

def function7(): 
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.fen/?mode=myaccounts.open&amp;query=0.1)")
	
		
def function8():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.seren/?action=authTrakt)")

				
def function9():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.thecrew/?action=authTrakt)")

    
def function10():
    xbmc.executebuiltin("RunPlugin(plugin://plugin.video.theoath/?action=authTrakt)")

   
def function11(): 0

  
def function12():
     xbmc.executebuiltin("RunPlugin(plugin://plugin.video.telemedia19?mode=5&url=www)")

      
		
 
menuoptions()
