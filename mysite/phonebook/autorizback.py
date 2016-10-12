# -*- coding: utf-8 -*-
__author__ = 'user'
import urllib2
import urllib
import cookielib,re
import json
import socket
import time
import urlparse
class Opener(object):
    def __init__(self, object_user):
	user=object_user.username
	password=object_user.userpass
        proxy=urllib2.ProxyHandler({'http':object_user.pars_proxy, "https":object_user.pars_proxy})
        #print(proxy)
        url=object_user.parsurl
        scheme, netloc, path, query, fragment=urlparse.urlsplit(url)
        path=""
        query=""
        fragment=""
        self.host=(urlparse.urlunsplit((scheme, netloc, path, query, fragment )))
        slov={"signin[username]":user, "back":"", "signin[password]":password}
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), proxy)
        urllib2.install_opener(opener)
        data_to_request = slov
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
        params_auth = urllib.urlencode(data_to_request)
        request_auth = urllib2.Request(url, params_auth, headers)
        page=opener.open(request_auth).read()
        #print(page)
        reg="window.localStorage.+"
        p=re.compile(reg)
        tok=p.findall(page)
        dkt=tok[0].split(" = '")[1].replace("';","")
        self.token={"token":dkt}
        self.opener=opener
        #return self
    def open(self, url,data=None):
        if type(data)==dict:
            data=urllib.urlencode(data)
        try:
            page=self.opener.open(url, data)
        except (urllib2.HTTPError), e:
            print("Close autoryti opener")
            self.__init__()
            page=self.opener.open(url, data)
        except (urllib2.URLError), e:
            print(e.args, e.message)
            time.sleep(20)
            page=self.open(url,data)
        return page

if __name__=="__main__":
    opener=Opener()