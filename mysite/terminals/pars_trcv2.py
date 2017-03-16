# -*- coding: utf-8 -*-
__author__ = 'ast7raz'
import logging, os
if __name__=="__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    #from mysite import settings
import urllib2
import datetime

from urllib import urlencode
import lxml.html as html
from mysite.settings import DIR_SPLITTER
from terminals.models import Keys



if __name__!="__main__":
    def Get_project_path(project_name="mysite"):
        APP_DIR = os.path.dirname(__file__)
        #print(APP_DIR)
        list_dir = APP_DIR.split(DIR_SPLITTER)
        index = list_dir.index(project_name)
        lgbt = list_dir[0:index + 1]
        patch = "/".join(lgbt)
        project_path = os.path.normpath(patch)
        return project_path
    filename=os.path.join(Get_project_path(), "pars.log")

    logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = filename)



class Key():
    TESTING = "%(url)supgrade/%(mashinid)s?release=testing"
    STABLE = "%(url)supgrade/%(mashinid)s?release=stable"
    BINGO_BOOM = "%(url)supgrade/%(mashinid)s?white_label=bingo-boom"
    RUB90 = "%(url)supgrade/%(mashinid)s?white_label=rub90"
    UPGRADE = "%(url)supgrade/%(mashinid)s"
    INFO = "%(url)supgrade/%(mashinid)s"
    COMMAND = "%(url)scommand/%(mashinid)s"
    def __init__(self, url, tr, timer):
        #self.url=url

        self.mashinid=tr.xpath("td[1]/a")[0].attrib["href"].split("/")[-1]
        if tr.xpath("td[1]/a")[0].text=="n/a":
            self.key="n/a"+"_"+self.mashinid
        else:
            self.key = tr.xpath("td[1]/a")[0].text

        self.name=tr.xpath("td[2]")[0].text
        self.part_name = tr.xpath("td[3]")[0].text
        self.club_name=tr.xpath("td[4]")[0].text
        if tr.xpath("td[5]")[0].text=="True":
            self.activ=True
        else:
            self.activ = False
        if tr.xpath("td[6]")[0].text == "True":
            self.blocked = True
        else:
            self.blocked = False
        #self.blocked=tr.xpath("td[6]")[0].text
        self.version=tr.xpath("td[7]")[0].text
        self.white_label=tr.xpath("td[8]")[0].text
        self.ip=tr.xpath("td[9]")[0].text
        self.date_time_last_online=timer
        try:
            self.upgrade=tr.xpath("td[11]/a")[0].attrib["href"]
        except IndexError:
            self.upgrade=tr.xpath("td[11]")[0].text
        self.TESTING_URL= self.TESTING %{"url":url, "mashinid":self.mashinid}
        self.STABLE_URL = self.STABLE % {"url": url, "mashinid": self.mashinid}
        self.BINGO_BOOM_URL = self.BINGO_BOOM % {"url": url, "mashinid": self.mashinid}
        self.RUB90_URL = self.RUB90 % {"url": url, "mashinid": self.mashinid}
        self.UPGRADE_URL = self.UPGRADE % {"url": url, "mashinid": self.mashinid}
        self.INFO_URL = self.INFO % {"url": url, "mashinid": self.mashinid}
        self.COMMAND_URL = self.COMMAND % {"url": url, "mashinid": self.mashinid}
        #print(self.blocked,self.key)

    def __unicode__(self):
        return self.key
    def __str__(self):
        return self.key
    def save_in_db(self):
        try:
            obj = Keys.objects.get(key=self.key)

        except Keys.DoesNotExist:
            print(self.key + " - DoesNotExist")
            logging.error(self.key + u" - DoesNotExist")
        else:
            obj.ip = self.ip
            obj.version = self.version
            obj.machine_id = self.mashinid
            obj.active=bool(self.activ)
            obj.blocked=bool(self.blocked)
            obj.date_time_last_online = self.date_time_last_online
            obj.white_label=self.white_label
            obj.save()
            #print(obj.key, obj.blocked)
            print("Done")

            logging.info(self.key+u" - Done")

class TRC_Parser():
    keys=[]

    def __init__(self,username, password ,url):
        self.url=url
        self.opener=self.__autorization(username,password,url)
        self.pars_keys()
        #return self.keys
    def __unicode__(self):
        return u"[%u]" % u", ".join(u"'" + unicode(i) + u"'" for i in self.keys)
    def __str__(self):
        #print(self.keys)
        return "[%s]" % ", ".join("'"+str(i)+"'" for i in self.keys)
    def get_page(self):
        r = urllib2.urlopen(self.url)
        page = html.document_fromstring(r.read())
        return page
    def get_list_keys(self):
        return self.keys
    def pars_keys(self):
        list = self.get_page().xpath("/html/body/table/tr")
        timer = datetime.datetime.utcnow()
        self.keys=[]
        for tr in list[1:]:
            key = Key(self.url, tr, timer)
            self.keys.append(key)
            # print(key)
    def __get_index(self, key_string):
        for i in range(len(self.keys)):
            if self.keys[i].key==key_string:
                return i
    def get_key(self, key_string):
        for i in self.keys:
            if i.key==key_string:
                return i
    def pop_key(self, key_string):
        index=self.__get_index(key_string)
        elem=self.keys.pop(index)
        #print(elem)
        return elem
    def __autorization(self, username, password ,url):
        #actvers=""
        pass_man=urllib2.HTTPPasswordMgrWithDefaultRealm()
        pass_man.add_password(None, url, username, password)
        auth_handler=urllib2.HTTPBasicAuthHandler(pass_man)
        opener=urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        return opener

if __name__=="__main__":

    parser=TRC_Parser("support", "6cc19eda65a973a2", "https://rub90.com/trcv2/")
    print("done")
    #print(parser.TESTING %{"mashinid":"teteteet"})
    print(parser.get_key("358321-080866-538985-122726-052937-529107").version)
