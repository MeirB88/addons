import sys,urllib,logging
import xbmcgui,xbmcplugin,xbmc,xbmcaddon,xbmcvfs
lang=xbmc.getLanguage(0)
import base64
import os
Addon = xbmcaddon.Addon()
user_dataDir = xbmc.translatePath(Addon.getAddonInfo("profile"))
if not xbmcvfs.exists(user_dataDir+'/'):
     os.makedirs(user_dataDir)

def addNolink( name, url,mode,isFolder,fan='DefaultFolder.png', iconimage="DefaultFolder.png",plot=' ',year=' ',generes=' ',rating=' ',trailer=' ',original_title=' '):
 

          
            params={}
            params['name']=name
            params['iconimage']=iconimage
            params['fanart']=fan
            params['description']=plot
            params['url']=url
            params['original_title']=original_title
            
            #all_ur=utf8_urlencode(params)
            u=sys.argv[0]+"?&mode="+str(mode)+'&name='+name+'&iconimage='+iconimage+'&fanart='+fan+'&description='+urllib.parse.quote_plus(plot)+'&url='+urllib.parse.quote_plus(url)+'&original_title='+original_title
           
            video_data={}
            video_data['title']=name
            
            
            if year!='':
                video_data['year']=year
            if generes!=' ':
                video_data['genre']=generes
            video_data['rating']=str(rating)
        
            video_data['poster']=fan
            video_data['plot']=plot
            if trailer!='':
                video_data['trailer']=trailer

            liz = xbmcgui.ListItem( name)
            liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage, 'poster': iconimage})
            liz.setInfo(type="Video", infoLabels=video_data)
            liz.setProperty( "Fanart_Image", fan )
            liz.setProperty("IsPlayable","false")
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)
###############################################################################################################        
def utf8_urlencode(params):
    import urllib as u
    # problem: u.urlencode(params.items()) is not unicode-safe. Must encode all params strings as utf8 first.
    # UTF-8 encodes all the keys and values in params dictionary
    par2=params
    for k,v in params.items():
        # TRY urllib.unquote_plus(artist.encode('utf-8')).decode('utf-8')
        if type(v) in (int, float):
            par2[k] = v
        else:
            try:
                par2[k.encode('utf-8')] = v.encode('utf-8')
            except Exception as e:
                logging.warning( '**ERROR utf8_urlencode ERROR** %s' % e )
    
    return u.urlencode(par2.items()).decode('utf-8')
def addDir3(name,url,mode,iconimage,fanart,description,image_master='',last_id='',video_info={},data=' ',original_title=' ',id=' ',season=' ',episode=' ',tmdbid=' ',eng_name=' ',show_original_year=' ',rating=0,heb_name=' ',isr=0,generes=' ',trailer=' ',dates=' ',watched='no',fav_status='false',collect_all=False,ep_number='',watched_ep='',remain='',groups_id='0',hist='',join_menu=False,menu_leave=False,remove_from_fd_g=False,all_w={}):
        
        name=name.replace("|",' ')
        description=description.replace("|",' ')
        original_title=original_title.replace("|",' ')

        params={}
        params['iconimage']=iconimage
        params['fanart']=fanart
        params['description']=description
        params['url']=url
        
        #all_ur=utf8_urlencode(params)
        u=sys.argv[0]+"?mode="+str(mode)+"&iconimage="+iconimage+"&fanart="+fanart+"&description="+ urllib.parse.quote_plus(description)+"&url="+ urllib.parse.quote_plus(url)+"&name="+(name)+"&image_master="+(image_master)+"&heb_name="+(heb_name)+"&last_id="+(last_id)+"&dates="+(dates)+"&data="+str(data)+"&original_title="+(original_title)+"&id="+(id)+"&season="+str(season)+"&episode="+str(episode)+"&tmdbid="+str(tmdbid)+"&eng_name="+(eng_name)+"&show_original_year="+(show_original_year)+"&isr="+str(isr)+"&fav_status="+fav_status+"&groups_id="+groups_id
        ok=True
        show_sources=True
        if mode==20 or mode==15:
            if Addon.getSetting("one_click")=='true':
                if Addon.getSetting("sh_one_click")=='false':
                   show_sources=False
        menu_items=[]
        menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32063), 'Action(Info)'))
        if remove_from_fd_g:
            #Remove from FD groups
            menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32082), 'XBMC.RunPlugin(%s)' % ('%s?url=%s&mode=35&name=%s')%(sys.argv[0],url,name)))
        if join_menu:
            #join Channel
            menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32062), 'XBMC.RunPlugin(%s)' % ('%s?url=%s&mode=22&name=join')%(sys.argv[0],url)))
        if menu_leave:
            #Leave Channel
            menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32031), 'XBMC.RunPlugin(%s)' % ('%s?url=%s&mode=23&name=%s')%(sys.argv[0],url,name)))
        
        if mode==16:
            #Remove
            menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32056), 'XBMC.RunPlugin(%s)' % ('%s?url=%s&mode=29&name=%s')%(sys.argv[0],url,name)))
        if mode==16:
            #add to my TV
            menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32069), 'XBMC.RunPlugin(%s)' % ('%s?url=%s&mode=27&name=%s&data=%s&iconimage=%s&fanart=%s&description=%s')%(sys.argv[0],id,name,data,iconimage,fanart,description)))
        if mode==2:
            #add to my TV
            menu_items.append(('[I]%s[/I]'%Addon.getLocalizedString(32080), 'XBMC.RunPlugin(%s)' % ('%s?url=%s&mode=34&name=%s&data=%s&iconimage=%s&fanart=%s&description=%s')%(sys.argv[0],url,name,data,iconimage,fanart,description)))
        video_data={}
        video_data['title']=name
        if (episode!=' ' and episode!='%20' and episode!=None) :
          video_data['mediatype']='tvshow'
          video_data['TVshowtitle']=original_title
          video_data['Season']=int(str(season).replace('%20','0'))
          video_data['Episode']=int(str(episode).replace('%20','0'))
          tv_show='tv'
        else:
           video_data['mediatype']='movies'
           video_data['TVshowtitle']=''
           video_data['tvshow']=''
           video_data['season']=0
           video_data['episode']=0
           tv_show='movie'
        if  mode==7:
            tv_show='tv'
        video_data['OriginalTitle']=original_title
        if data!=' ':
            video_data['year']=data
        if generes!=' ':
            video_data['genre']=generes
        video_data['rating']=str(rating)
    
        video_data['poster']=fanart
        video_data['plot']=description
        if trailer!=' ':
            video_data['trailer']=trailer
      

        
        '''
        str_e1=list(u.encode('utf8'))
        for i in range(0,len(str_e1)):
           str_e1[i]=str(ord(str_e1[i]))
        str_e='$$'.join(str_e1)
        '''
        if tv_show=='tv':
            ee=str(episode)
        else:
            ee=str(id)
        if video_info!={}:
            
            video_data=video_info
        if ee in all_w:
            
            video_data['playcount']=0
            video_data['overlay']=0
            
           
            name=name.replace('[COLOR white]','[COLOR lightblue]')
            video_data['title']=name
            
        liz=xbmcgui.ListItem(name)
        liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage, 'poster': iconimage})
        liz.addContextMenuItems(menu_items, replaceItems=False)
        

        if ee in all_w:
            liz.setProperty('ResumeTime', all_w[ee]['resume'])
            liz.setProperty('TotalTime', all_w[ee]['totaltime'])
            try:
                if Addon.getSetting("filter_watched")=='true':
                    time_to_filter=float(Addon.getSetting("filter_watched_time"))
                    pre_time=float((float(all_w[ee]['resume'])*100)/float(all_w[ee]['totaltime']))
                    if pre_time>time_to_filter:
                        return u,None,show_sources
            except:
                pass
        

        video_data['title']=video_data['title'].replace("|",' ')
        video_data['plot']=video_data['plot'].replace("|",' ')
        
        
        liz.setInfo( type="Video", infoLabels=video_data)
        liz.setProperty( "Fanart_Image", fanart )
        #ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return u,liz,show_sources



def addLink( name, url,mode,isFolder, iconimage,fanart,description,data='',rating='',generes='',no_subs='0',tmdb='0',season='0',episode='0',original_title='',da='',year=0,all_w={},in_groups=False):
          name=name.replace("|",' ')
          description=description.replace("|",' ')
          params={}
          params['name']=name
          params['iconimage']=iconimage
          params['fanart']=fanart
          params['description']=description
          params['url']=url
        
          #all_ur=utf8_urlencode(params)
          u=sys.argv[0]+"?url="+ urllib.parse.quote_plus(url)+"&name="+name+"&iconimage="+iconimage+"&fanart="+fanart+"&description="+urllib.parse.quote_plus(description)+"&url="+urllib.parse.quote_plus(url)+"&no_subs="+str(no_subs)+"&season="+str(season)+"&episode="+str(episode)+"&mode="+str(mode)+"&original_title="+str(original_title)+"&id="+str(tmdb)+"&data="+str(data)
 

          video_data={}
          video_data['title']=name
            
            
          if year!='':
                video_data['year']=year
          if generes!='':
                video_data['genre']=generes
          if rating!=0:
            video_data['rating']=str(rating)
        
          video_data['poster']=fanart
          video_data['plot']=description
          f_text_op=Addon.getSetting("filter_text")
          filer_text=False
          if len(f_text_op)>0:
                filer_text=True
                if ',' in f_text_op:
                    all_f_text=f_text_op.split(',')
                else:
                    all_f_text=[f_text_op]
            
          if filer_text:
            for items_f in all_f_text:
                if items_f.lower() in name.lower():
                    return 0
          #u=sys.argv[0]+"?url="+ urllib.parse.quote_plus(url)+"&mode="+str(mode)+"&name="+ urllib.parse.quote_plus(name)
          liz = xbmcgui.ListItem( name)
          liz.setArt({'thumb' : iconimage, 'fanart': iconimage, 'icon': iconimage, 'poster': iconimage})
          if in_groups:
              #ee=base64.b64encode(str(name).replace("'","%27"))
              
              ee=str(name)
              if ee in all_w:
                
                video_data['playcount']=0
                video_data['overlay']=0
                video_data['title']='[COLOR lightblue]'+original_title+'[/COLOR]'
                liz.setProperty('ResumeTime', all_w[ee]['resume'])
                liz.setProperty('TotalTime', all_w[ee]['totaltime'])
                try:
                    if Addon.getSetting("filter_watched")=='true':
                        time_to_filter=float(Addon.getSetting("filter_watched_time"))
                        pre_time=float((float(all_w[ee]['resume'])*100)/float(all_w[ee]['totaltime']))
                        if pre_time>time_to_filter:
                            return 0
                except:
                    pass
          liz.setInfo(type="Video", infoLabels=video_data)
          liz.setProperty("IsPlayable","false")
          liz.setProperty( "Fanart_Image", fanart )
          
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)