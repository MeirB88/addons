# -*- coding: utf-8 -*-
import sys,urllib,json,logging
import xbmcgui,xbmcplugin,xbmc

KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    que=urllib.quote_plus
    url_encode=urllib.urlencode
else:
    from urllib.parse import quote  
    from urllib.parse import urlencode  
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus
    
    
def utf8_urlencode(params):
    try:
        import urllib as u
        enc=u.urlencode
    except:
        from urllib.parse import urlencode
        enc=urlencode
    # problem: u.urlencode(params.items()) is not unicode-safe. Must encode all params strings as utf8 first.
    # UTF-8 encodes all the keys and values in params dictionary
    for k,v in list(params.items()):
        # TRY urllib.unquote_plus(artist.encode('utf-8')).decode('utf-8')
        if type(v) in (int, float):
            params[k] = v
        else:
            try:
                params[k.encode('utf-8')] = v.encode('utf-8')
            except Exception as e:
                pass
                #logging.warning( '**ERROR utf8_urlencode ERROR** %s' % e )
    
    return enc(params).encode().decode('utf-8')
def addNolink( name, url,mode,isFolder, iconimage="DefaultFolder.png",fan="DefaultFolder.png"):
 

          
           
          u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)
          if KODI_VERSION<=18:
            liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
          else:
            liz=xbmcgui.ListItem(name)
            
          

          liz.setInfo(type="Video", infoLabels={ "Title": unque( name)   })
          liz.setProperty( "Fanart_Image", fan )
          liz.setProperty("IsPlayable","false")
          liz.setProperty( "Fanart_Image", iconimage )
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description,video_info={},generes='',next_page='',o_name=''):

        #u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)+"&iconimage="+que(iconimage)+"&fanart="+que(fanart)+"&description="+que(description)
        iconimage=iconimage.strip()
        fanart=fanart.strip()
        params={}
        params['name']=name
        params['url']=url
        params['mode']=mode
        params['iconimage']=iconimage
        params['fanart']=fanart
        params['description']=description
        params['next_page']=next_page
        params['o_name']=o_name
        all_ur=utf8_urlencode(params)
        u=sys.argv[0]+"?mode="+str(mode)+'&'+all_ur
        
        ok=True
        menu_items=[]
        menu_items.append(('[I]Clear Cache[/I]', 'XBMC.RunPlugin(%s)' % ('%s?url=www&mode=35')%(sys.argv[0])))
        if KODI_VERSION<=18:
            liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        else:
            liz=xbmcgui.ListItem(name)
        if video_info!={}:
                
            info=(video_info)
                
        else:
            info={ "Title": unque( name), "Plot": description   }
        if generes!='':
            info['genre']=generes
        remove_keys=['fanart','icon','original_title','tv_title','fast','heb title','imdb','poster','studios','tmdb']
        for key in remove_keys:
            if key in info:
                del info[key]
        
        
        if mode==46:
            menu_items.append(('[I]הוספה למועדפים[/I]', 'XBMC.RunPlugin(%s?mode=7&name=%s&url=%s&iconimage=%s&fanart=%s&description=%s&video_info=%s)'  % ( sys.argv[0] ,name,url,iconimage,fanart,que(description.encode('utf8')),video_info)))
            menu_items.append(('[I]הסר מהמועדפים[/I]', 'XBMC.RunPlugin(%s?mode=9&video_info=%s&name=%s&url=%s&iconimage=%s&fanart=%s&description=%s)'  % ( sys.argv[0] ,que(json.dumps(video_info)),name,url,iconimage,fanart,description)))
            menu_items.append(('[I]מתי משודר[/I]', 'XBMC.RunPlugin(%s?mode=47&video_info=%s&name=%s&url=www&iconimage=%s&fanart=%s&description=%s)'  % ( sys.argv[0] ,que(json.dumps(video_info)),name,iconimage,fanart,description)))
            menu_items.append(('[I]סרטונים[/I]', 'Container.update(%s?mode=50&video_info=%s&name=%s&url=www&iconimage=%s&fanart=%s&description=%s)'  % ( sys.argv[0] ,que(json.dumps(video_info)),name,iconimage,fanart,description)))
            
        liz.setInfo( type="Video", infoLabels=info)
        liz.setProperty( "Fanart_Image", fanart )
        art = {}
        art.update({'poster': iconimage})
        liz.setArt(art)
        liz.addContextMenuItems(menu_items, replaceItems=False)
        #ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return u,liz,True
        



def addLink( name, url,mode, iconimage,fanart,description,data='',video_info={},id='',all_w={},original_title='NONONON',o_name=''):

          #u=sys.argv[0]+"?url="+que(url)+"&id="+id+"&mode="+str(mode)+"&name="+(name)+"&data="+str(data)+"&iconimage="+que(iconimage)+"&fanart="+que(fanart)+"&description="+(description)
 

          iconimage=iconimage.strip()
          fanart=fanart.strip()
          params={}
          params['name']=name
          params['url']=url
          params['mode']=mode
          params['iconimage']=iconimage
          params['fanart']=fanart
          params['description']=description
          params['id']=id
          params['video_info']=(video_info)
          params['o_name']=o_name
          all_ur=utf8_urlencode(params)
          u=sys.argv[0]+"?mode="+str(mode)+'&'+all_ur
          menu_items=[]
          menu_items.append(('[I]Clear Cache[/I]', 'XBMC.RunPlugin(%s)' % ('%s?url=www&mode=35')%(sys.argv[0])))
          
          #u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)
          if KODI_VERSION<=18:
            liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
          else:
            liz=xbmcgui.ListItem(name)
          if video_info!={}:
                
                info=json.loads(video_info)
                
          else:
            info={ "Title": unque( name), "Plot": description   }
          remove_keys=['fanart','icon','original_title','tv_title','fast','heb title','imdb','poster','studios','tmdb']
          for key in remove_keys:
              if key in info:
                del info[key]
          
          if mode==16 or 'הגרל' in description:
            
            info['playcount']=0
            info['overlay']=0
            liz.setProperty('ResumeTime', '0')
            liz.setProperty('TotalTime', '11110')
          elif name in all_w:
              logging.warning('Found new seek')
              liz.setProperty('ResumeTime', all_w[name]['seek_time'])
              liz.setProperty('TotalTime', all_w[name]['total_time'])
          elif original_title+name in all_w:
              logging.warning('Found new seekTV')
              liz.setProperty('ResumeTime', all_w[original_title+name]['seek_time'])
              liz.setProperty('TotalTime', all_w[original_title+name]['total_time'])
          liz.setInfo(type="Video", infoLabels=info)
          art = {}
          art.update({'poster': iconimage})
          liz.setArt(art)
          liz.setProperty("IsPlayable","true")
          liz.setProperty( "Fanart_Image", fanart )
          liz.addContextMenuItems(menu_items, replaceItems=False)
          #xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)
          return u,liz,False