# -*- coding: utf-8 -*-
import xbmcaddon,os,xbmc,xbmcgui,urllib,re,xbmcplugin,sys,logging,json,time,threading,base64
from resources.modules import cache

Addon = xbmcaddon.Addon()
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])


if KODI_VERSION<=18:#kodi18
    if Addon.getSetting('debug')=='false':
        reload (sys )#line:61
        sys .setdefaultencoding ('utf8')#line:62
else:#kodi19
    import importlib
    importlib.reload (sys )#line:61
if KODI_VERSION<=18:#kodi18
    if Addon.getSetting('debug')=='false':
        reload (sys )#line:61
        sys .setdefaultencoding ('utf8')#line:62
else:#kodi19
    import importlib
    importlib.reload (sys )#line:61
t_path=os.path.dirname(os.path.realpath(__file__))

user_dataDir = xbmc.translatePath(Addon.getAddonInfo("profile"))
if not os.path.exists(user_dataDir):
     os.makedirs(user_dataDir)
user_dataDir_img=os.path.join(user_dataDir,'images')
if not os.path.exists(user_dataDir_img):
    os.makedirs(user_dataDir_img)
from resources.modules.addall import addLink,addDir3,addNolink
try:
    if KODI_VERSION<=18:
        from resources.modules.sdarot_17 import resolve_dns,get_final_video_and_cookie,get_ip_url,get_user_cookie_sratim
    else:
        from resources.modules.sdarot import resolve_dns,get_final_video_and_cookie,get_ip_url,get_user_cookie_sratim
except:
    import shutil
    d= os.path.join(t_path,'dns')
    if os.path.exists(d):
        shutil.rmtree(d)
    if KODI_VERSION<=18:
        dns_path=os.path.join(t_path,'dns_17')
    else:
        dns_path=os.path.join(t_path,'dns_19')
    
    shutil.copytree(dns_path, d, False, None)
    if KODI_VERSION<=18:
        from resources.modules.sdarot_17 import resolve_dns,get_final_video_and_cookie,get_ip_url,get_user_cookie_sratim
    else:
        from resources.modules.sdarot import resolve_dns,get_final_video_and_cookie,get_ip_url,get_user_cookie_sratim
if KODI_VERSION<=18:
    dns_path=os.path.join(t_path,'dns_18')
    que=urllib.quote_plus
    que_n=urllib.quote
    url_encode=urllib.urlencode
else:
    dns_path=os.path.join(t_path,'dns_17')
    que_n=urllib.parse.quote
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus
if KODI_VERSION>18:
    
    class Thread (threading.Thread):
       def __init__(self, target, *args):
        super().__init__(target=target, args=args)
       def run(self, *args):
          
          self._target(*self._args)
else:
   
    class Thread(threading.Thread):
        def __init__(self, target, *args):
           
            self._target = target
            self._args = args
            
            
            threading.Thread.__init__(self)
            
        def run(self):
            
            self._target(*self._args)
if KODI_VERSION<=18:
    from urlparse import urlparse
    import httplib
else:
    import urllib.parse as urlparse
    import http.client as httplib
API = base64.b64decode('aHR0cHM6Ly9hcGkuc2Rhcm90LnR2').decode('utf-8')
POSTER_PREFIX = 'https://static.sdarot.website/series/'
BASE_MOVIE_URL='https://sratim.tv/'
base_header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',

            'Pragma': 'no-cache',
            
           
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
            }
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
def main_menu():
    all_d=[]
    all_d.append(addDir3('סדרות','0',1,'https://i.ytimg.com/vi/B6eKLj6foMQ/hqdefault.jpg','https://1.bp.blogspot.com/-d5RdlKKZOV4/Xik8v3-ZEBI/AAAAAAAAIOY/5cU2hwrNNLowBcYmgSnpSqzRCu1J1kMBACNcBGAsYHQ/s1600/Photo%2B23-01-2020%252C%2B8%2B16%2B08.jpg','סדרות'))
    all_d.append(addDir3('סרטים','0',2,'https://static.sratim.tv/assets/images/logo.png','https://www.yomyom.net/UploadImg/ArticlesNew/images/2813/%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2/%D7%A7%D7%95%D7%9C%D7%A0%D7%95%D7%A2.jpg','סרטים'))
    
    all_d.append(addDir3('עולם סרטים באיכות ובחינם','0',14,'https://images.hdqwalls.com/wallpapers/bthumb/venom-movie-logo-4k-x5.jpg','https://i.ytimg.com/vi/2boXwMiF744/maxresdefault.jpg','סרטים'))
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def sdarot_main(iconimage,fanart):
    all_d=[]
    all_d.append(addDir3('קטגוריות','0',3,iconimage,fanart,'סדרות'))
    all_d.append(addDir3('לפי א-ב','0',4,iconimage,fanart,'סרטים'))
    all_d.append(addDir3('חיפוש','2',8,iconimage,fanart,'סרטים'))
    
   
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def sdr_cat(url,iconimage,fanart):
    all_d=[]
    headers={
    'User-agent': 'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1',
    'pkg': 'com.phone.sdarottv',
    
    'Content-Type': 'application/x-www-form-urlencoded',


    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'utf-8',

    }
    headers['auth']='1'
    
    
    req,cookie_new = resolve_dns(API + '/series/genres',headers=headers).get()
    logging.warning(req)
    req=json.loads(req)
    for items in req['genres']:
        all_d.append(addDir3(items['name'],items['id'],4,iconimage,fanart,items['name']))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def download_img(urls):
    
   
    for items in urls:
        try:
            x=resolve_dns(items).download_image()
        except:
            pass
    return 0
def sdr_gen(url,page):
    all_d=[]
    page = int(page)
    headers={
    'User-agent': 'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1',
    'pkg': 'com.phone.sdarottv',
    
    'Content-Type': 'application/x-www-form-urlencoded',


    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'utf-8',

    }
    headers['auth']='1'
    
    if url=='0':
        req,cookie_new = resolve_dns(API + '/series/list/page/{0}/perPage/100/orderBy/{1}'.format(page, 'heb'),headers=headers).get()
    else:
        req,cookie_new = resolve_dns(API + '/series/list/{0}/page/{1}/perPage/100'.format(url, page),headers=headers).get()
    req=json.loads(req)
    all_img=[]
    thread=[]
    for items in req['series']:
        image=POSTER_PREFIX+items['poster']
        if 'sdarot' in image:
                f_image=get_img_loc(image)
                
                if not os.path.exists(os.path.join(f_image)):
                    all_img.append(image)
                icon=f_image
                image=f_image
        else:
                logging.warning(icon)
        all_d.append(addDir3(items['heb'],items['id'],5,image,image,items['description']))
    if not req['pages']['page'] == req['pages']['totalPages']:
        all_d.append(addDir3('[COLOR yellow]{0}[/COLOR]'.format('הבא'),url,4,'https://i.ytimg.com/vi/B6eKLj6foMQ/hqdefault.jpg','https://1.bp.blogspot.com/-d5RdlKKZOV4/Xik8v3-ZEBI/AAAAAAAAIOY/5cU2hwrNNLowBcYmgSnpSqzRCu1J1kMBACNcBGAsYHQ/s1600/Photo%2B23-01-2020%252C%2B8%2B16%2B08.jpg','הבא',next_page=str(int(page) + 1)))
        
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    thread.append(Thread(download_img,all_img))
  
    for td in thread:
          td.start()
          
def get_img_loc(image):
    img_n=image.split('/')
    f_img=img_n[len(img_n)-1].replace('/','')
   
    f_save=os.path.join(user_dataDir_img,f_img)
    return f_save
def sdr_series(name,url,iconimage,fanart):
    all_d=[]
    headers={
    'User-agent': 'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1',
    'pkg': 'com.phone.sdarottv',

    'Content-Type': 'application/x-www-form-urlencoded',


    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'utf-8',

    }
    headers['auth']='1'
    req,cookie_new = resolve_dns(API + '/series/info/{0}'.format(url), headers=headers).get()
    req=json.loads(req)
    serie = req['serie']
    des=req['serie']['description']
    episodes = serie['episodes']
    if not episodes:
        return []
    
    items = []
    for season in sorted(episodes.keys(), key=int):
        label = u'עונה {0}'.format(season)
        
                    
        all_d.append(addDir3(label,json.dumps([url,season]),6,iconimage,fanart,des,o_name=name))
        

    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def sdr_series_ep(o_name,url,iconimage,fanart):
    se=json.loads(url)[1]
    url=json.loads(url)[0]
    headers={
    'User-agent': 'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1',
    'pkg': 'com.phone.sdarottv',
   
    'Content-Type': 'application/x-www-form-urlencoded',


    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'utf-8',

    }
    headers['auth']='1'
    req,cookie_new = resolve_dns(API + '/series/info/{0}'.format(url), headers=headers).get()
    req=json.loads(req)['serie']
   
    if req['episodes']==None:
        xbmcgui.Dialog().ok('Sdaror TV',"אין פרקים")
        return 0
    episodes = req['episodes'][str(se)]
    items = []
    all_d=[]
    for episode in episodes or []:
        label = u'פרק {0}'.format(episode['episode'])
        plot = episode['description'] or 'לא זמין'
        all_d.append(addLink(label,json.dumps([url,se,episode['episode']]),7,iconimage,fanart,plot,o_name=o_name))
        
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def play(o_name,url,iconimage,fanart,description,name):
   

    url_data=json.loads(url)
    season=url_data[1]
    episode=url_data[2]
    url, cookie=get_final_video_and_cookie(url_data[0], url_data[1], url_data[2], False, False)
    video_data={}
    
    video_data['title']=o_name+' ,'+name
    video_data['icon']=iconimage
    video_data['original_title']=o_name+' ,'+name
    video_data['plot']=description

    video_data['season']=season
    video_data['episode']=episode
    video_data['poster']=fanart
    video_data['poster3']=fanart
    video_data['fanart2']=fanart
    
    listItem = xbmcgui.ListItem(video_data['title'], path=url) 
    listItem.setInfo(type='Video', infoLabels=video_data)
    listItem.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
def utf8_urlencode(params):
    try:
        import urllib as u
        enc=u.urlencode
    except:
        from urllib.parse import urlencode
        enc=urlencode
    # problem: u.urlencode(params.items()) is not unicode-safe. Must encode all params strings as utf8 first.
   
    
    return enc(params).encode().decode('utf-8')
    
def search(iconimage,fanart,page,o_name):
    page = int(page)
    all_d=[]
    if page==0:
        search_input = ''

        
        kb = xbmc.Keyboard('', 'חפש כאן')
        kb.doModal()
        if kb.isConfirmed():
            search_input = que(kb.getText())
    else:
        search_input=o_name
    if len(search_input) < 2:
            xbmcgui.Dialog().ok('Sdaror TV','מילת החיפוש חייבת להכיל לפחות שני תווים')
    else:
        headers={
        'User-agent': 'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1',
        'pkg': 'com.phone.sdarottv',
       
        'Content-Type': 'application/x-www-form-urlencoded',


        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'utf-8',

        }
        headers['auth']='1'
        results,cookie_new = resolve_dns(API + '/series/search/{0}/page/{1}/perPage/100'.format(search_input, page), headers=headers).get()
        results=json.loads(results)['series']
        all_img=[]
        thread=[]
        logging.warning(results)
        if results==None:
            xbmcgui.Dialog().ok('Sdaror TV','אין תוצאות')
            return 0
        for s in results:
                    label = u'{0}-{1}'.format(s['heb'], s['eng'])
                    
                    image=POSTER_PREFIX+s['poster']
                    if 'sdarot' in image:
                            f_image=get_img_loc(image)
                            
                            if not os.path.exists(os.path.join(f_image)):
                                all_img.append(image)
                            icon=f_image
                            image=f_image
                    else:
                            logging.warning(icon)
                    all_d.append(addDir3(label,s['id'],5,image,image,s['description'],o_name=label))
                    
        
        #if not results['pages']['page'] == results['pages']['totalPages']:
        #    all_d.append(addDir3('[COLOR yellow]{0}[/COLOR]'.format('הבא'),url,8,'https://i.ytimg.com/vi/B6eKLj6foMQ/hqdefault.jpg','https://1.bp.blogspot.com/-d5RdlKKZOV4/Xik8v3-ZEBI/AAAAAAAAIOY/5cU2hwrNNLowBcYmgSnpSqzRCu1J1kMBACNcBGAsYHQ/s1600/Photo%2B23-01-2020%252C%2B8%2B16%2B08.jpg','הבא',next_page=str(int(page) + 1),o_name=search_input))
        
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
        thread.append(Thread(download_img,all_img))
  
        for td in thread:
              td.start()
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
    txt = txt.strip()
    return txt
def sratim_tv(iconimage,fanart):
    all_d=[]
    all_d.append(addDir3('כל הסרטים','https://sratim.tv/list?filter=1&order=rate&dir=desc',12,iconimage,fanart,'סרטים'))
    all_d.append(addDir3('סרטים חדשים','0',9,iconimage,fanart,'סרטים'))
    all_d.append(addDir3('קטגוריות','0',10,iconimage,fanart,'סרטים'))
    all_d.append(addDir3('חיפוש','0',11,iconimage,fanart,'סרטים'))
    
   
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def sratim_tv_all(url,iconimage,fanart,page):
    page=int(page)
    
    all_d=[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }
    results,cookie_new = resolve_dns(url, headers=headers).get()
    if page>0:
        if 'genre' in url:
            ur='https://sratim.tv/ajax/movies?loadMore=24&start=%s&search[genre][]=%s&search[from]=&search[to]=&search[order]=&search[dir]='%(page*24,url.split('genre[]=')[1])
        else:
            ur='https://sratim.tv/ajax/movies?loadMore=24&start=%s&search[from]=&search[to]=&search[order]=rate&search[dir]=DESC'%(page*24)
        logging.warning(ur)
        results,cookie_new = resolve_dns(ur, headers=headers,cookies=cookie_new).get()
    regex='<div class="block-wrapper">.+?img src="(.+?)" class="img-fluid" alt="(.+?)">.+?<span>(.+?)</span>.+?a href="(.+?)".+?<p>(.+?)</p>'
    m=re.compile(regex,re.DOTALL).findall(results.decode('utf-8'))
    for image,nm,year,lk,dis in m:
        all_d.append(addLink(replaceHTMLCodes(nm)+' (%s)'%year,BASE_MOVIE_URL+lk,13,'https:'+image,'https:'+image,replaceHTMLCodes(dis)))
    all_d.append(addDir3('[COLOR yellow]{0}[/COLOR]'.format('הבא'),url,12,iconimage,fanart,'הבא',next_page=str(int(page) + 1)))
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))

def sratim_tv_new(iconimage,fanart,page):
    all_d=[]
    page=int(page)
    if page>0:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest',
            'Alt-Used': 'sratim.tv:443',
            'Connection': 'keep-alive',
            'Referer': 'https://sratim.tv/',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers',
        }
        
        results,cookie_new = resolve_dns('https://sratim.tv/', headers=headers).get()
        logging.warning(cookie_new)
       

        results,cookie_new = resolve_dns('https://sratim.tv/ajax/movies?loadByType=new&page='+str(page+1), headers=headers,cookies=cookie_new).get()
    else:
        results,cookie_new = resolve_dns('https://sratim.tv/', headers=base_header).get()
    regex='<div class="block-wrapper">.+?img src="(.+?)" class="img-fluid" alt="(.+?)">.+?<span>(.+?)</span>.+?a href="(.+?)".+?<p>(.+?)</p>'
    m=re.compile(regex,re.DOTALL).findall(results.decode('utf-8'))
    for image,nm,year,lk,dis in m:
        all_d.append(addLink(replaceHTMLCodes(nm)+' (%s)'%year,BASE_MOVIE_URL+lk,13,'https:'+image,'https:'+image,replaceHTMLCodes(dis)))
    all_d.append(addDir3('[COLOR yellow]{0}[/COLOR]'.format('הבא'),url,9,iconimage,fanart,'הבא',next_page=str(int(page) + 1)))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def sratim_tv_gen(iconimage,fanart):
    all_d=[]
    results,cookie_new = resolve_dns('https://sratim.tv/', headers=base_header).get()
    regex="<li><a href=\".+?</div>(.+?)</section>"
    m_pre=re.compile(regex,re.DOTALL).findall(results.decode('utf-8'))[0]
    regex='<a href="(.+?)">(.+?)</a>'
    m=re.compile(regex).findall(m_pre)
    for lk,nm in m:
        
        all_d.append(addDir3(nm,BASE_MOVIE_URL+lk,12,iconimage,fanart,nm))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def build_final_url(url, cookie):

    
    try:
        f_k=que_n(cookie.get('Sratim'), safe='')
        return 'http:{0}|Cookie=Sratim={1}&User-Agent={2}'.format((url), f_k, base_header.get('User-Agent'))
    except:
        f_k=que_n(base_header.get('Cookie'), safe='')
        return 'http:{0}|Cookie={1}&User-Agent={2}'.format((url), f_k, base_header.get('User-Agent'))
        
def play_movie(name,url,iconimage,fanart,description):
    cookie_new={}
    if Addon.getSetting('username')!='':
        logging.warning('Check Username')
        cookie_new=get_user_cookie_sratim()
    results,cookie_new4 = resolve_dns(url, headers=base_header).get()
    logging.warning(cookie_new)
    if cookie_new=={}:
        cookie_new=cookie_new4
   
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    token,cookie_new1 = resolve_dns('http://api.sratim.tv/movie/preWatch', headers=headers,cookies=cookie_new).get()
    
    vid,cookie_new2 = resolve_dns('http://api.sratim.tv/movie/watch/id/%s/token/%s'%(url.replace('https://sratim.tv//movie/',''),token.decode('utf-8')), headers=headers,cookies=cookie_new).get()
    vid=json.loads(vid)
    
    
    req=vid
    if 'errors' in vid:
        if 'errors' in vid:
            msg=vid['errors'][0]
        else:
            msg="אנא המתן 30 שניות"
        if 1:
            dp = xbmcgui.DialogProgress()
            if KODI_VERSION>18:
                dp.create("לצפייה באיכות HD וללא המתנה ניתן לרכוש מנוי", msg+'\n'+ ''+'\n'+
                
                      "[COLOR orange][B]לרכישת מנוי להיכנס בדפדפן - https://sratim.tv/signup[/B][/COLOR]")
            else:
                dp.create("לצפייה באיכות HD וללא המתנה ניתן לרכוש מנוי", msg, '',
                
                      "[COLOR orange][B]לרכישת מנוי להיכנס בדפדפן - https://sratim.tv/signup[/B][/COLOR]")
            dp.update(0)
        
        tm=30

        if not 'errors' in vid:
         tm=0
         return vid, cookie
        else:
          tm=re.findall(r' \d+ ', vid['errors'][0])
          tm=int (tm[0].strip())
        
            
        for s in range(tm, -1, -1):
            time.sleep(1)
            if 1:
                if KODI_VERSION>18:
                    dp.update(int(((tm - s)* 100.0) / (tm+1) ),msg+'\n'+ 'עוד {0} שניות'.format(s)+'\n'+  "[COLOR orange][B]לרכישת מנוי להיכנס בדפדפן - https://sratim.tv/signup[/B][/COLOR]")
                else:
                    dp.update(int(((tm - s)* 100.0) / (tm+1) ),msg,'עוד {0} שניות'.format(s),  "[COLOR orange][B]לרכישת מנוי להיכנס בדפדפן - https://sratim.tv/signup[/B][/COLOR]")
                if dp.iscanceled():
                    dp.close()
                    return None, None
        req,cookie_new3 = resolve_dns('http://api.sratim.tv/movie/watch/id/%s/token/%s'%(url.replace('https://sratim.tv//movie/',''),token.decode('utf-8')), headers=headers,cookies=cookie_new).get()
    
    try:
        req=json.loads(req)
    except:
        pass
    if req['success']:
        qualities = req['watch']
        
        qualities_list = qualities.keys()
        max_quality = int(Addon.getSetting('max_quality'))
        
        quality = '480'

        if max_quality >= 720:
            quality = '1080' if '1080' in qualities_list and max_quality == 1080 else '720'
            if quality == '720' and '720' not in qualities_list:
                quality = '480'
        f_link=build_final_url(qualities[quality], cookie_new)
        
    video_data={}
    if KODI_VERSION<=18:
        name=name.encode('utf-8')
    logging.warning('name::'+name)
    video_data['title']=name
    video_data['icon']=iconimage
    video_data['original_title']=name
    video_data['plot']=description

    video_data['season']='0'
    video_data['episode']='0'
    video_data['poster']=fanart
    video_data['poster3']=fanart
    video_data['fanart2']=fanart
    
    listItem = xbmcgui.ListItem(video_data['title'], path=f_link) 
    listItem.setInfo(type='Video', infoLabels=video_data)
    listItem.setProperty('IsPlayable', 'true')
    ok=xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
def search_m(iconimage,fanart,page,o_name):
    page = int(page)
    all_d=[]
    if page==0:
        search_input = ''

        
        kb = xbmc.Keyboard('', 'חפש כאן')
        kb.doModal()
        if kb.isConfirmed():
            search_input = que(kb.getText())
    else:
        search_input=o_name
    if len(search_input) < 2:
            xbmcgui.Dialog().ok('Sdaror TV','מילת החיפוש חייבת להכיל לפחות שני תווים')
    else:
        data={'term':search_input}
        results,cookie_new = resolve_dns('http://api.sratim.tv/movie/search',headers=base_header,data=data).post()
        results=json.loads(results)
        for items in results['results']:
            all_d.append(addLink(items['name'],BASE_MOVIE_URL+'/movie/'+items['id'],13,iconimage,fanart,items['name']))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def download_db():
    if KODI_VERSION>18:
        import urllib.request

        fp = urllib.request.urlopen('http://admin.adminpanel.esy.es/api/first/4F5A9C3D9A86FA54EACEDDD635185/d15abfs-9fe2-4b84-b979-jeff21bcad13/', headers=base_header)
        mybytes = fp.read()

        results = mybytes.decode("utf8")
        fp.close()
    else:
        import urllib2

        response = urllib2.urlopen('http://admin.adminpanel.esy.es/api/first/4F5A9C3D9A86FA54EACEDDD635185/d15abfs-9fe2-4b84-b979-jeff21bcad13/')
        results = response.read()

    return results
def movie_world(icon,fanart):
    all_d=[]
    count=0
    results=json.loads(cache.get(download_db, 1,table='pages'))
    all_d.append(addDir3('החמים',str(-1),15,icon,fanart,'החמים'))
    for items in results['genres']:
        all_d.append(addDir3(items['title'],str(count),15,icon,fanart,items['title']))
        count+=1
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def movie_world_items(icon,fanart,url):
    all_d=[]
    results=json.loads(cache.get(download_db, 1,table='pages'))
    if url!='-1':
        res=results['genres'][int(url)]['posters']
    else:
        res=results['bigPosters']
    for items in res:
        
        if items['type']=='movie':
            mode=16
            added=''
            ur=str(items['sources'][0]['url'])
        else:
            continue
            added='(סדרה) '
            mode=17
            ur=str(items['id'])
        
        classi=items['classification']
        if classi==None:
            classi=''
        description=items['description']
        if description==None:
            description=''
        video_info={}
        video_info['title']=added+items['title']
        video_info['plot']=classi+'\n'+description
        video_info['year']=items['year']
        
        all_d.append(addLink(added+items['title'],ur,16,items['image'],items['image'],items['description'],video_info=json.dumps(video_info)))
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def play_simple(name,url,plot,icon,fanart):
    listItem = xbmcgui.ListItem(path=url)
    listItem.setInfo(type='Video', infoLabels={'name':name,'plot':plot,'poster':icon})
    listItem.setProperty('IsPlayable', 'true')
    
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listItem)
params=get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
description=None
next_page='0'
o_name=''
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
try:
    video_info=unque(params["video_info"])
except:
        pass
try:
    next_page=(params["next_page"])
except:
        pass
try:
    o_name=unque(params["o_name"])
except:
        pass

        
logging.warning('Mode:'+str(mode))
logging.warning('url:'+str(url))
#logging.warning('video_info:'+str(video_info))
if mode==None or url==None or len(url)<1:
        main_menu()
elif mode==1:
    sdarot_main(iconimage,fanart)
elif mode==2:
    sratim_tv(iconimage,fanart)
elif mode==3:
    sdr_cat(url,iconimage,fanart)
elif mode==4:
    sdr_gen(url,next_page)
elif mode==5:
    sdr_series(name,url,iconimage,fanart)
elif mode==6:
    sdr_series_ep(o_name,url,iconimage,fanart)
elif mode==7:
    play(o_name,url,iconimage,fanart,description,name)
elif mode==8:
    search(iconimage,fanart,next_page,o_name)
elif mode==9:
    sratim_tv_new(iconimage,fanart,next_page)
elif mode==10:
    sratim_tv_gen(iconimage,fanart)
elif mode==11:
    search_m(iconimage,fanart,next_page,o_name)
elif mode==12:
    import ssl
    logging.warning(ssl.OPENSSL_VERSION)
    sratim_tv_all(url,iconimage,fanart,next_page)
elif mode==13:
    play_movie(name,url,iconimage,fanart,description)
elif mode==14:
    movie_world(iconimage,fanart)
elif mode==15:
    movie_world_items(iconimage,fanart,url)
elif mode==16:
    play_simple(name,url,description,iconimage,fanart)
elif mode==17:
    tv_shows(name,url,description,iconimage,fanart)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
        