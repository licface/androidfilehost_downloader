#!/usr/bin/env python
#coding:utf-8
"""
  Author:  LICFACE --<licface@yahoo.com>
  Purpose: Download from Androidfilehost helper
  Created: 7/18/2018
"""

import sys
import os
import requests
from bs4 import BeautifulSoup as bs
from urlparse import urlparse
from debug import *
import re
#import cfscrape
import argparse
import json
import idm
import wget
import traceback

class AFH(object):
    def __init__(self):
        super(AFH, self)
        self.URL = 'https://androidfilehost.com/'
        self.Sess = requests.Session()
        self.STATUS_CODE = ''
        
    def setCookies(self, url = None, cookies = None):
        '''
            ``params:``
            
                    * cookies => dict
        '''
        if not cookies:
            cookies = self.getCookies(url)
        if not cookies:
            return {}, '', {}
        debug(cookies = cookies)
        cookies_dict = {}
        cookies_str = ''
        if cookies.keys():
            for i in cookies.keys():
                cookies_dict.update({str(i): cookies.get(i),})
                cookies_str = cookies_str + str(i) + "=" + str(cookies.get(i)) + ";"
        debug(cookies_str = cookies_str)
        debug(cookies_dict = cookies_dict)
        return cookies, cookies_str, cookies_dict        
        
    def getCookies(self, url = None, cookies = None):
        if not url:
            return False
        debug(url = url)
        req = self.Sess.get(url)
        if not cookies:
            cookies = req.cookies
        return cookies
        
    def setHeaders(self, accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', connection = '', content_length = '', cache_control = '', upgrade_insecure_requests = '', referer = '', x_mod_sbb_ctype = '', x_requested_with = '', headers_response = None, url = None, cookies = None):
        if not url:
            url = self.URL
        debug(url = url)
        debug(cookies0 = cookies)
        cookies, cookies_str, cookies_dict = self.setCookies(url, cookies)
        host = urlparse(self.URL).netloc
        headers = {}
        headers.update({'Accept': accept,})
        headers.update({'Accept-Encoding': 'gzip, deflate, br',})
        headers.update({'Accept-Language': 'en-US,en;q=0.5',})
        if connection:
            headers.update({'Connection': connection,})
        if content_length:
            headers.update({'Content-Length': content_length,})  #62
        if cache_control:
            headers.update({'Cache-Control': cache_control,})  #max-age=3600
        headers.update({'Cookie': cookies_str,})
        headers.update({'Host': host,})
        if referer:
            headers.update({'Referer': referer,})
        if upgrade_insecure_requests:
            headers.update({'Upgrade-Insecure-Requests': upgrade_insecure_requests,})
        headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',})
        if x_mod_sbb_ctype:
            headers.update({'X_MOD_SBB_CTYPE': x_mod_sbb_ctype,})        
        if x_requested_with:
            headers.update({'X-Requested-With': x_requested_with,})
            
        if headers_response:
            cookies_add_for_header = headers_response.get('Set-Cookie')
            debug(cookies_add_for_header = cookies_add_for_header)
            cookies_add_for_header_list = re.split(", |; |", cookies_add_for_header)
            debug(cookies_add_for_header_list = cookies_add_for_header_list)
            cookies_add_for_header_dict = {}
            for i in cookies_add_for_header_list:
                data = re.split("=", str(i), 1)
                if len(data) == 2:
                    key, value = data
                    cookies_add_for_header_dict.update({key: value,})

            debug(cookies_add_for_header_dict = cookies_add_for_header_dict)
            if cookies_add_for_header_dict.get('UTGv2'):
                cookies_dict.update({'UTGv2': cookies_add_for_header_dict.get('UTGv2'),})
            if cookies_add_for_header_dict.get('SPSI'):
                cookies_dict.update({'SPSI': cookies_add_for_header_dict.get('SPSI'),})
            if cookies_add_for_header_dict.get('spcsrf'):
                cookies_dict.update({'spcsrf': cookies_add_for_header_dict.get('spcsrf'),})
            if cookies_add_for_header_dict.get('sp_lit'):
                cookies_dict.update({'sp_lit': cookies_add_for_header_dict.get('sp_lit'),})
            debug(cookies_dict = cookies_dict)
            cookies, cookies_str, cookies_dict = self.setCookies(cookies = cookies)
            headers.update({'Cookie': cookies_str,})
            
        debug(headers = headers)
        debug(cookies_str = cookies_str)
        debug(cookies_dict = cookies_dict)

        return headers, cookies, cookies_str, cookies_dict
    
    def getContent(self, url, headers = None):
        if '/' in url[0]:
            url = url[1:]
        url = self.URL + url
        debug(url = url)
        if not headers:
            headers, cookies, cookies_str, cookies_dict = self.setHeaders(cache_control= 'max-age=3600', upgrade_insecure_requests = '1')
        debug(headers = headers)
        req = self.Sess.get(url, cookies = cookies_dict, headers = headers)
        #print "Content:"
        #print req.content
        print "STATUS: {0}[{1}]".format(str(req.status_code), str(req.ok))
        return req.cookies, req.headers
        
    def getDownloadLink(self, url = 'https://androidfilehost.com/?fid=890129502657592740'):
        cookies, headers = self.getContent(url)  #example: https://androidfilehost.com/?fid=890129502657592740
        debug(cookies0= cookies)
        debug(headers0 = headers)
        cookies, cookies_str, cookies_dict = self.setCookies(cookies= cookies)
        debug(cookies_0 = cookies)
        debug(cookies_str_0 = cookies_str)
        debug(cookies_dict_0 = cookies_dict)
        headers, cookies, cookies_str, cookies_dict = self.setHeaders(accept= '*/*', connection= 'keep-alive', content_length= '62', cookies = cookies, headers_response= headers)
        debug(headers1 = headers)
        debug(cookies_1 = cookies)
        debug(cookies_str_1 = cookies_str)
        debug(cookies_dict_1 = cookies_dict)        

        url1 = self.URL + "libs/otf/mirrors.otf.php"
        headers.update({'X-MOD-SBB-CTYPE': 'xhr',})
        headers.update({'X-Requested-With': 'XMLHttpRequest',})
        debug(headers_x = headers)
        data = {
            'action': 'getdownloadmirrors',
            'fid': re.split("=", str(urlparse(url).query), 1)[1], 
            'submit': 'submit',
        }
        debug(data = data)
        debug(url1 = url1)
        req = self.Sess.post(url1, cookies = cookies, headers = headers, data = data)
        #cf = cfscrape.create_scraper()
        #req = cf.get(url1, cookies = cookies, headers = headers, data = data)
        contents = req.content
        debug(STATUS_CODE = req.status_code)
        debug(OK = req.ok)
        debug(req_content = contents)
        if req.status_code < 350:
            self.STATUS_CODE = req.status_code
            return json.loads(contents)
        else:
            self.STATUS_CODE = req.status_code
            return {}
        
    def usage(self):
        parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parser.add_argument('URL', action = 'store', help = 'androidfilehost url, example: https://androidfilehost.com/?fid=890129502657592740')
        parser.add_argument('-c', '--clip', action = 'store_true', help = "Download url from clipboard")
        parser.add_argument('-d', '--download', action = 'store_true', help = 'it will download directly, for windows default using IDM if installed and wget (build in) if not exists and for *nix')
        parser.add_argument('-p', '--path', action = 'store', help =\
                            'directory of downloaded', default = os.path.abspath( os.getcwd()))
        parser.add_argument('-n', '--name', action = 'store', help = 'Option name it')
        parser.add_argument('-i', '--wget', action = 'store_true', help = 'Use wget (build in) download manager instead')
        parser.add_argument('-D', '--debug', action = 'store_true', help = 'Debugging Process')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            if args.debug:
                os.environ.update({'DEBUG': '1',})
            else:
                os.environ.update({'DEBUG': '',})
            if args.clip:
                try:
                    import clipboard
                except ImportError:
                    print "Module Clipboard not installed, please install before or don't use clip arguments"
                    sys.exit(0)
            data = self.getDownloadLink(args.URL)
            if not data:
                print "Error [%s]: Can't download, please contact support <licface@yahoo.com>" % (str(self.STATUS_CODE))
                sys.exit(0)
            debug(data_message = data.get('MESSAGE'))
            if 'success' in data.get('MESSAGE'):
                mirrors = data.get('MIRRORS')
                if len(mirrors) > 1:
                    n = 1
                    for i in mirrors:
                        print str(n) + ". " + str(i.get('name'))
                    q = raw_input('Select Server downloading: ')
                    if str(q).isdigit() and not int(q) > len(mirrors):
                        URL = mirrors[int(q)-1].get('url').replace('\\', '')
                        debug(URL_SELECTED = URL)
                        if args.download:
                            if args.wget:
                                if args.name:
                                    OUT = os.path.join(args.path, args.name)
                                else:
                                    OUT = args.path
                                name = wget.download(str(URL), OUT)
                                print "FILE DOWNLOADED (WGET):", str(name)
                            else:
                                try:
                                    #download(self, link, path_to_save=None, output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
                                    dm = idm.IDMan()
                                    dm.download(str(URL), args.path, args.name)
                                    print "FILE DOWNLOADING (IDM):",\
                                          os.path.join( args.path,\
                                                        os.path.basename(url))
                                except:
                                    if os.getenv('DEBUG') == 1:
                                        traceback.format_exc()
                                    if args.name:
                                        OUT = os.path.join(args.path, args.name)
                                    else:
                                        OUT = args.path
                                    debug(URL = URL)
                                    name = wget.download(str(URL), OUT)
                                    print "FILE DOWNLOADED (WGET ~ Exception):", str(name)
                else:
                    URL = mirrors[0].get('url').replace('\\', '')
                    debug(URL_SELECTED = URL)
                    if args.download:
                        if args.wget:
                            if args.name:
                                OUT = os.path.join(args.path, args.name)
                            else:
                                OUT = args.path
                            name = wget.download(URL, OUT)
                            print "FILE DOWNLOADED (WGET):", str(name)
                        else:
                            try:
                                #download(self, link, path_to_save=None, output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
                                dm = idm.IDMan()
                                dm.download(str(URL), args.path, args.name)
                                print "FILE DOWNLOADING (IDM):",\
                                      os.path.join( args.path,\
                                                    os.path.basename(url))
                            except:
                                if args.name:
                                    OUT = os.path.join(args.path, args.name)
                                else:
                                    OUT = args.path
                                name = wget.download(URL, OUT)
                                print "FILE DOWNLOADED (WGET ~ Exception):", str(name)                    
            else:
                print "Can't downloading ... !, please contact support (licface@yahoo.com)"
if __name__ == '__main__':
    c = AFH()
    c.usage()
    #url = c.URL
    #cookies, cookies_str, cookies_dict = c.setCookies(url)
    #import pprint
    #pprint.pprint(cookies)
    #headers = c.setHeaders()
    #pprint.pprint(headers)
    #url_content = '?fid=890129502657592740'
    #cookies1, headers1 = c.getContent(url_content)
    #print "cookies1 =", cookies1
    #print "headers1 =", headers1
    #c.getDownloadLink()