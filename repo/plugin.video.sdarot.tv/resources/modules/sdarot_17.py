# -*- coding: utf-8 -*-
import socket,ssl,os,io,urlparse
import time,cache,xbmcaddon,xbmc
import dns.resolver
global global_var,stop_all#global
global progress
progress=''
global_var=[]
stop_all=0
Addon = xbmcaddon.Addon()

if Addon.getSetting("regex_mode")=='1':
    import regex  as re
else:
    import re

type=['tv','subs']

import urllib2,urllib,logging,base64,json
user_dataDir_pre = xbmc.translatePath(Addon.getAddonInfo("profile")).decode("utf-8")
user_dataDir_img=os.path.join(user_dataDir_pre,'images')
if not os.path.exists(user_dataDir_img):
    os.makedirs(user_dataDir_img)
    
HEADERS={
    'User-agent': 'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1',
    'pkg': 'com.phone.sdarottv',
    
    'Content-Type': 'application/x-www-form-urlencoded',


    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'utf-8',

    }
HEADERS_MOVIES = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }
local=False
try:
  import xbmcgui,xbmcaddon,xbmc
  CACHE_FILE = os.path.join(xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode('utf-8'), 'cache.json')
except:
  local=True
  dataPath=os.path.dirname(os.path.realpath(__file__))
  CACHE_FILE=os.path.join(dataPath,'cache_f')
  
API = base64.decodestring('aHR0cHM6Ly9hcGkuc2Rhcm90LnR2')

POSTER_PREFIX = base64.decodestring('aHR0cHM6Ly9zdGF0aWMuc2Rhcm90LndvcmxkL3Nlcmllcy8=')

import httplib,hashlib


def get_ip(address):
    handlers = [
        urllib2.HTTPHandler(),
        urllib2.HTTPSHandler()
    ]
    opener = urllib2.build_opener(*handlers)
    req = urllib2.Request(base64.decodestring('aHR0cHM6Ly9kbnMuZ29vZ2xlLmNvbS9yZXNvbHZlP25hbWU9')+address)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    try:
        response = opener.open(req,timeout=100)
        data = response.read()
        response.close()
    except Exception as ex:
        logging.warning('ex:'+str(ex))
        return None
    data = json.loads(data)
    return data['Answer'][0]['data']


def cache_ip(address):
    try:
        if not os.path.isfile(CACHE_FILE):
            a_list = {}
        else:
            with open(CACHE_FILE, 'r') as handle:
                a_list = json.load(handle)
        a_key = base64.encodestring(urlparse.urlparse(address).netloc)
        if not a_list.get(a_key):
            a_list[a_key] = {'a': 0, 'b': ''}
        now = int(time.time())
        if now - a_list[a_key]['a'] > 86400:
            a_list[a_key]['b'] =  base64.encodestring(get_ip(base64.decodestring(a_key)))
            a_list[a_key]['a'] =  now
            with io.open(CACHE_FILE, 'w', encoding='utf-8') as handle:
                handle.write(unicode(json.dumps(a_list, ensure_ascii=False)))
        return base64.decodestring(a_list[a_key]['b'])
    except Exception as ex:
        logging.warning('ex2:'+str(ex))
        return None
def MyResolver(host):
  resolver = dns.resolver.Resolver()
  dns_value=Addon.getSetting('dns')
  resolver.nameservers = [dns_value]
  answer = resolver.query(host,'A')

  return answer.rrset.items[0].address
class MyHTTPConnection(httplib.HTTPConnection):
  def connect(self):
    logging.warning(MyResolver(self.host))
    resolve_ip=cache.get(MyResolver,24,self.host, table='cookies')
    self.sock = socket.create_connection((resolve_ip,self.port),self.timeout)
class MyHTTPSConnection(httplib.HTTPSConnection):
  def connect(self):
    logging.warning(MyResolver(self.host))
    resolve_ip=cache.get(MyResolver,24,self.host, table='cookies')
    
    sock = socket.create_connection((resolve_ip, self.port), self.timeout)
    self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file)

class MyHTTPHandler(urllib2.HTTPHandler):
  def http_open(self,req):
    return self.do_open(MyHTTPConnection,req)

class MyHTTPSHandler(urllib2.HTTPSHandler):
  def https_open(self,req):
    return self.do_open(MyHTTPSConnection,req)
    
    
    
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
def get_auth(string_to_encode):

    a=encrypt_string(string_to_encode+'Sdarot AndroidTV 4,1.2.0p; Android: 23,6.0.1')
    
    b=encrypt_string(a+'KvtIUb//NH;$6U^]DP\'Uc33}Q5YMM-i?')
    return b
class resolve_dns():
    
    def __init__(self,url,headers=HEADERS,cookies={},data={}):
        self.url=url
        headers['auth']=get_auth(url.replace(API,''))
        self.headers=headers
        self.cookies=cookies
        self.data=data
    def download_image(self):
        import cookielib
        handlers = [MyHTTPHandler,MyHTTPSHandler]
        cookjar = cookielib.CookieJar()
        handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookjar)]
        if 'sratim' in self.url:#Addon.getSetting('dns_solver')=='1':
            handlers = [urllib2.HTTPHandler(), urllib2.HTTPSHandler(context=ctx), urllib2.HTTPCookieProcessor(cookjar)]
        opener = urllib2.build_opener(*handlers)
        #opener.addheaders.append(('Set-Cookie', urllib.urlencode(self.cookies)))

        if 'Sdarot' in self.cookies:

          self.headers['Cookie']='Sdarot={0}'.format((self.cookies.get('Sdarot')))
        elif 'Sratim' in self.cookies:
            self.headers['Cookie']='Sratim={0}'.format((self.cookies.get('Sratim')))
        
        img_n=self.url.split('/')
        f_img=img_n[len(img_n)-1].replace('/','')
        f_save=os.path.join(user_dataDir_img,f_img)
        
        
        urllib2.install_opener(opener)
        urlReader = urllib2.urlopen( self.url ).read() 
        with open( f_save, "wb" ) as f:
          f.write( urlReader )
          
        
     
            
       
    def get_ip(self):
        import requests
        
        req = (base64.decodestring('aHR0cHM6Ly9kbnMuZ29vZ2xlLmNvbS9yZXNvbHZlP25hbWU9')+API.replace('https://',''))
        data=requests.get(req,headers=self.headers).json()

        return data['Answer'][0]['data']
    def get(self):
        import requests
        
        import cookielib
        
        if 'sratim' in self.url:#Addon.getSetting('dns_solver')=='1':
            new_ip=cache.get(self.get_ip,24, table='cookies')
            
            
            print 'NEW IP'
            print new_ip
            print API
            self.url=self.url.replace(API,'https://'+new_ip)
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
        handlers = [MyHTTPHandler,MyHTTPSHandler]
        cookjar = cookielib.CookieJar()
        handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookjar)]
        if 'sratim' in self.url:#Addon.getSetting('dns_solver')=='1':
            handlers = [urllib2.HTTPHandler(), urllib2.HTTPSHandler(context=ctx), urllib2.HTTPCookieProcessor(cookjar)]
        opener = urllib2.build_opener(*handlers)
        #opener.addheaders.append(('Set-Cookie', urllib.urlencode(self.cookies)))
        print self.cookies
        if 'Sdarot' in self.cookies:

          self.headers['Cookie']='Sdarot={0}'.format((self.cookies.get('Sdarot')))
        elif 'Sratim' in self.cookies:
            self.headers['Cookie']='Sratim={0}'.format((self.cookies.get('Sratim')))
        request = urllib2.Request(self.url,  headers=self.headers,data=urllib.urlencode(self.data))

        request.get_method = lambda: 'GET'
        html = opener.open(request).read()

        cookie_new={}
        for cook in cookjar:
          cookie_new[cook.name]=cook.value
        return html,cookie_new

    def post(self):
        import cookielib
        
        if 'sratim' in self.url:#Addon.getSetting('dns_solver')=='1':
            new_ip=cache.get(self.get_ip,24, table='cookies')
            
            
            
            
            self.url=self.url.replace(API,'https://'+new_ip)
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        handlers = [MyHTTPHandler,MyHTTPSHandler]
        cookjar = cookielib.CookieJar()
        handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookjar)]
        if 'sratim' in self.url:#Addon.getSetting('dns_solver')=='1':
            handlers = [urllib2.HTTPHandler(), urllib2.HTTPSHandler(context=ctx), urllib2.HTTPCookieProcessor(cookjar)]
        opener = urllib2.build_opener(*handlers)
        #opener.addheaders.append(('Set-Cookie', urllib.urlencode(self.cookies)))

        
        if 'Sdarot' in self.cookies:

          self.headers['Cookie']='Sdarot={0}'.format((self.cookies.get('Sdarot')))

        request = urllib2.Request(self.url,  headers=self.headers,data=urllib.urlencode(self.data))

        request.get_method = lambda: 'POST'
      

        html = opener.open(request).read()
        cookie_new={}
        for cook in cookjar:
          cookie_new[cook.name]=cook.value
        return html,cookie_new
    def image(self):
        import cookielib
        

        handlers = [MyHTTPHandler,MyHTTPSHandler]
        cookjar = cookielib.CookieJar()
        handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookjar)]
        
        opener = urllib2.build_opener(*handlers)
        #opener.addheaders.append(('Set-Cookie', urllib.urlencode(self.cookies)))

        
        if 'Sdarot' in self.cookies:

          self.headers['Cookie']='Sdarot={0}'.format((self.cookies.get('Sdarot')))

        request = urllib2.Request(self.url,  headers=self.headers,data=urllib.urlencode(self.data))

        request.get_method = lambda: 'POST'
      

        html = opener.open(request)
        localFile = open('desktop.jpg', 'wb')
        localFile.write(html.read())
        localFile.close()
    
    
def get_user_cookie_sratim(cookie_pre=''):
    username = Addon.getSetting('username')
    password = Addon.getSetting('Password_sdr')
    
    if username and password:

        data = {
            'username': username,
            'password': password
        }

        #req = requests.post(API + '/login', data=data, headers=HEADERS)
        req,cookie_new=resolve_dns('https://api.sratim.tv/user/login', data=data, headers=HEADERS_MOVIES).post()
        
        res = json.loads(req)
        
        if 'errors' in res:
            if res['success']==False:
                xbmc.executebuiltin(u'Notification(%s,%s)' % ('Sdarot', ' Sratim.TV'+ ', '.join(res['errors'])))
            return cookie_pre
            
        if res['success']:
            
            return cookie_new

        else:
            #xbmcgui.Dialog().ok('בדוק שם משתמש וסיסמא של סדרות טיוי', ', '.join(res['errors']).encode('utf-8'))
            
            if u'\u05d0\u05ea\u05d4 \u05db\u05d1\u05e8 \u05de\u05d7\u05d5\u05d1\u05e8 \u05dc\u05de\u05e2\u05e8\u05db\u05ea!' in res['errors']:
                
                
                return {}
            
            #Addon.setSetting('password', '')
    #else:
    #    xbmcgui.Dialog().ok('שגיאה', 'בדוק שם משתמש וסיסמא של סדרות טיוי')
    return {}
def get_user_cookie(cookie_pre=''):
    username = Addon.getSetting('username')
    password = Addon.getSetting('Password_sdr')

    if username and password:

        data = {
            'username': username,
            'password': password
        }
        
        #req = requests.post(API + '/login', data=data, headers=HEADERS)
        req,cookie_new=resolve_dns(API + '/user/login', data=data, headers=HEADERS).post()
        
        res = json.loads(req)

        if 'errors' in res:
            if res['success']==False:
                xbmc.executebuiltin(u'Notification(%s,%s)' % ('Mando', ' SDAROT.TV'+ ', '.join(res['errors'])))
            return cookie_pre
            
        if res['success']:
            
            return cookie_new

        else:
            #xbmcgui.Dialog().ok('בדוק שם משתמש וסיסמא של סדרות טיוי', ', '.join(res['errors']).encode('utf-8'))
            
            if u'\u05d0\u05ea\u05d4 \u05db\u05d1\u05e8 \u05de\u05d7\u05d5\u05d1\u05e8 \u05dc\u05de\u05e2\u05e8\u05db\u05ea!' in res['errors']:
                
                
                return {}
            
            #Addon.setSetting('password', '')
    #else:
    #    xbmcgui.Dialog().ok('שגיאה', 'בדוק שם משתמש וסיסמא של סדרות טיוי')
    return {}
def get_ip_url(url):
    base = urlparse.urlparse(url)
    watch = cache_ip(url)
    return url.replace(base.netloc, watch)
def build_final_url(url, cookie):

    try:
        f_k=urllib.quote(cookie.get('Sdarot'), safe='')
        return 'http:{0}|Cookie=Sdarot={1}&User-Agent={2}'.format(get_ip_url(url), f_k, HEADERS.get('User-agent'))
    except:
        f_k=urllib.quote(HEADERS.get('Cookie'), safe='')
        return 'http:{0}|Cookie={1}&User-Agent={2}'.format(get_ip_url(url), f_k, HEADERS.get('User-agent'))
    


def get_final_video_and_cookie(sid, season, episode, choose_quality=False, download=False):
    token,cookie=cache.get(get_sdarot_ck,3,sid,season,episode, table='cookies')

    logging.warning('Doner Test:'+token)
    if token == 'donor':
        vid = get_video_url(sid, season, episode, token, cookie, choose_quality)

    else:
        if download:
            #plugin.notify('התחבר כמנוי כדי להוריד פרק זה', image=ICON)
            return None, None
        else:
            vid = get_video_url(sid, season, episode, token, cookie, choose_quality)
            logging.warning(vid)
            if 'errors' in vid:
                msg=vid['errors'][0]
            else:
                msg="אנא המתן 30 שניות"
            if local==False:
                dp = xbmcgui.DialogProgress()
                dp.create("לצפייה באיכות HD וללא המתנה ניתן לרכוש מנוי", msg, '',
                          "[COLOR orange][B]לרכישת מנוי להיכנס בדפדפן - www.sdarot.tv/donate[/B][/COLOR]")
                dp.update(0)
            
            tm=30
   
            if not 'errors' in vid:
             tm=0
             return vid, cookie
            else:
              tm=re.findall(r' \d+ ', vid['errors'][0])
              tm=int (tm[0].strip())
            if tm>28:
              
              token,cookie=cache.get(get_sdarot_ck,0,sid,season,episode, table='cookies')
            
            
            
            

            for s in range(tm, -1, -1):
                time.sleep(1)
                if local==False:
                    dp.update(int(((tm - s)* 100.0) / (tm+1) ), msg, 'עוד {0} שניות'.format(s), '')
                    if dp.iscanceled():
                        dp.close()
                        return None, None
                

        vid = get_video_url(sid, season, episode, token, cookie, choose_quality)
        
    if vid:
            return vid, cookie
def get_video_url(sid, season, episode, token, cookie, choose_quality):

    #req = requests.post(API + '/episode/watch/sid/{0}/se/{1}/ep/{2}'.format(sid, season, episode),
    #                    data={'token': token}, cookies=cookie, headers=HEADERS).json()
    req,cookie_new=resolve_dns(API + '/episode/watch/sid/{0}/se/{1}/ep/{2}'.format(sid, season, episode),
                        data={'token': token}, cookies=cookie, headers=HEADERS).post()
    req=json.loads(req)
    if req['success']:
        qualities = req['watch']
        if choose_quality:
            return qualities
        else:
            qualities_list = qualities.keys()
            max_quality = int(Addon.getSetting('max_quality'))
            quality = '480'

            if max_quality >= 720:
                quality = '1080' if '1080' in qualities_list and max_quality == 1080 else '720'
                if quality == '720' and '720' not in qualities_list:
                    quality = '480'
            
            return build_final_url(qualities[quality], cookie)
    
    return req
def get_sdarot_ck(sid,season,episode,cookie={}):
            #cookie=cache.get(get_user_cookie,1, table='user_cookies')
            if cookie=={}:
                cookie = get_user_cookie()
            logging.warning('user Cook')
            logging.warning(cookie)
            
            d={'SID': sid, 'season': season, 'episode': episode}
            req,cookie_new=resolve_dns(API + '/episode/preWatch', data={'SID': sid, 'season': season, 'episode': episode},
                                cookies=cookie, headers=HEADERS).post()
            '''
            logging.warning( 'cook new' )
            logging.warning(cookie_new)
            logging.warning(d)
            logging.warning(API + '/episode/preWatch')
            logging.warning(cookie)
            '''
            
            #req = requests.post(API + '/episode/preWatch', data={'SID': sid, 'season': season, 'episode': episode},
            #                    cookies=cookie, headers=HEADERS)
            #token = req.text
            
            token=req
          
            if not cookie:
              cookie = cookie_new
            return token,cookie
def get_links(tv_movie,original_title,name,season_n,episode_n,season,episode,show_original_year,id):
            global global_var,stop_all,progress
            progress='Start'
            f_links='NO LINK'
            logging.warning('Searching sdarot')
            start_time=time.time()
            da=[]
            sd_link=''
            da.append((tv_movie,original_title,name,season_n,episode_n,season,episode,show_original_year,id))
            logging.warning('Sdarot:'+original_title)
            logging.warning(da)
            progress='Requests'
            logging.warning(API + '/series/search/{0}/page/{1}/perPage/100'.format(name.replace('%','%25'), '0'))
            req,cookie_new=resolve_dns(API + '/series/search/{0}/page/{1}/perPage/100'.format(name.replace('%','%25'), '0')).get()
           
         
            '''
            s = requests.Session()
            req = requests.Request(method='GET', url=API, headers=HEADERS)
            prep = req.prepare()
            prep.url = API + '/series/search/{0}/page/{1}/perPage/100'.format(name, '1')
            
            req = s.send(prep)
            '''
            
            all_links=[]
            results = json.loads(req)['series']
            logging.warning(results)
            if not results:
                progress='Requests2'
                req,cookie_new=resolve_dns(API + '/series/search/{0}/page/{1}/perPage/100'.format(original_title, '0')).get()
               
                results = json.loads(req)['series']
                logging.warning(results)
            if results:
                
                items = []
                for s in results:
                    progress='Requests3'
                    req ,cookie_new= resolve_dns(API + '/series/info/{0}'.format(s['id']), headers=HEADERS).get()
                    req=json.loads(req)
                    logging.warning(req)
                    #req = requests.get(API + '/series/info/{0}'.format(s['id']), headers=HEADERS).json()
                    serie = req['serie']
                    ep_found=0
                    se_found=0
                    episodes = serie['episodes']
                    
                    if episodes!=None:
                        for sen in episodes:
                          
                          if sen==season:
                            se_found=1
                        
                        if se_found==1:
                           
                            if (len(episodes)>=int(season)):
                              for items_in in episodes[season]:
                                ep=items_in['episode']
                         
                                if episode==ep:
                                  ep_found=1
                                  break
                           
                            if ep_found==1:
                                sd_link=json.dumps((s['id'], season, episode))
                                #f_links=get_final_video_and_cookie(s['id'], season, episode, False, False)
                                if not episodes:
                                    return []
                                break
                                
                                #all_links.append((s['heb'],sd_link,'Sdarot','480'))
                                #links_sdarot=all_links
            progress='Token'
            x=0
            tick_x=0
            token,cookie=cache.get(get_sdarot_ck,3,s['id'],unicode(season),unicode(episode), table='cookies')
            progress='Done Token'
            
            logging.warning('Cookie search')
            logging.warning(cookie)
            if token == 'donor':
                res='1080'
            else:
                res='480'
            if sd_link!='':
                all_links.append((s['heb'],sd_link,'Direct',res))
                logging.warning(all_links)
                global_var=all_links
                elapsed_time = time.time() - start_time
                progress=' Done '+time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                while x<10:
                    if tick_x==0:
                        progress='Done'+time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                        tick_x=1
                    else:
                        progress='Done_'+time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
                        tick_x=0
                    x+=1
                    time.sleep(0.1)
                
            #get_sdarot_ck(s['id'],unicode(season),unicode(episode))
            
            
            return all_links
            