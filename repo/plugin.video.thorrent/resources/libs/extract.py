# -*- coding: utf-8 -*-
################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import zipfile, xbmcaddon, xbmc, sys, os, time,logging

KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
try:
    if KODIV > 17:
        import zfile as zipfile #FTG mod for Kodi 18
    else:
        import zipfile
except:pass

KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])


def all(_in, _out, dp=None, ignore=None, title=None,keep_userdata=False):
	allNoProgress(_in, _out, ignore)

def allNoProgress(_in, _out, ignore):
	try:
		zin = zipfile.ZipFile(_in, 'r')
		zin.extractall(_out)
	except Exception as e:
		print (str(e))
		return False
	return True