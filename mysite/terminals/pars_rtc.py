# -*- coding: utf-8 -*-
__author__ = 'user'
import urllib2
from urllib import urlencode
import lxml.html as html
import threading
import logging, os
def Get_project_path(project_name="mysite"):
    APP_DIR = os.path.dirname(__file__)
    #print(APP_DIR)
    list_dir = APP_DIR.split("/")
    index = list_dir.index(project_name)
    lgbt = list_dir[0:index + 1]
    patch = "/".join(lgbt)
    project_path = os.path.normpath(patch)
    return project_path
filename=os.path.join(Get_project_path(), "pars.log")

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.ERROR, filename = filename)
def start(username, password ,url):
    actvers=""
    pass_man=urllib2.HTTPPasswordMgrWithDefaultRealm()
    pass_man.add_password(None, url, username, password)
    auth_handler=urllib2.HTTPBasicAuthHandler(pass_man)
    opener=urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

    ret={}
    ret_key=[]
    ret_test=[]
    r=urllib2.urlopen(url)
    text=r.read()
    #print(text)
    page=html.document_fromstring(text)
    li=page.xpath("/html/body/div")
    for i in xrange(len(li)):
	mashine_id=page.xpath("/html/body/div[%s]" % str(i+1))[0].attrib["id"]
        key=page.xpath("/html/body/div[%s]/span[1]" % str(i+1))[0].text
        if key=="n/a":
    	    key=key+"_"+mashine_id
        vers=page.xpath("/html/body/div[%s]/span[2]" % str(i+1))[0].text
        ip=page.xpath("/html/body/div[%s]/span[3]" % str(i+1))[0].text
        try:
	    cmd=page.xpath("/html/body/div[%s]/a[1]" % str(i+1))[0].attrib["href"]
    	    ssh=page.xpath("/html/body/div[%s]/a[2]" % str(i+1))[0].attrib["href"]
    	    vnc=page.xpath("/html/body/div[%s]/a[3]" % str(i+1))[0].attrib["href"]
    	    x=page.xpath("/html/body/div[%s]/a[4]" % str(i+1))[0].attrib["href"]
    	except IndexError:
    	    cmd=""
    	    ssh=""
    	    vnc=""
    	    x=""
    	try:
    	    up=page.xpath("/html/body/div[%s]/a[5]" % str(i+1))[0].attrib["href"]
    	except:
    	    up=""
        #print(up)
        ret_key.append(key)
        ret[key]={"key":key,"version":vers,"ip":ip,"cmd":cmd,"ssh":ssh,"vnc":vnc,"x":x, "mid":mashine_id, "up":up}
        ret_test.append({"key":key,"version":vers,"ip":ip,"cmd":cmd,"ssh":ssh,"vnc":vnc,"x":x, "mid":mashine_id, "up":up})
    return ret, ret_key,ret_test

def get_cmd(url,username, password):
    pass_man=urllib2.HTTPPasswordMgrWithDefaultRealm()
    pass_man.add_password(None, url, username, password)
    auth_handler=urllib2.HTTPBasicAuthHandler(pass_man)
    opener=urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

    r=urllib2.urlopen(url)

    text=r.read()
    #print("get_cmd Print r: "+text)
    page=html.document_fromstring(text)
    #print(page)
    li=page.xpath("/html/body/pre")[0].text
    #print(li)
    return li
def get_x(url, username, password):
    logging.debug(url)
    pass_man=urllib2.HTTPPasswordMgrWithDefaultRealm()
    #logging.debug("X1 Done")
    pass_man.add_password(None, url, username, password)
    auth_handler=urllib2.HTTPBasicAuthHandler(pass_man)
    opener=urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    logging.debug("X2 Done")
    try:
	r=urllib2.urlopen(url)
    except urllib2.HTTPError as e:
	logging.info(e.code)
	#logging.info(e.read())
    logging.debug("x3 Done")
    #text=r.getcode()
    #logging.debug(text)
    #print(text)
    #print(li)
    #return li

if __name__ == "__main__":
    pass
