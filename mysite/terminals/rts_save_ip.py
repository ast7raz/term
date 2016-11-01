# -*- coding: utf-8 -*-
import pars_rtc, sys, os, datetime
import django
import logging
logname="/home/asorokin/www-support/mysite/ip.log"
'''
try:
    os.remove(logname)
except:
    print("File not exist: %s"%logname)'''

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',level=logging.DEBUG, filename=logname, filemode="w")
sys.path.append("/var/www-support/mysite")
#print(sys.path)
#os.curdir="Z:\\home\\test.key\\www\\mysite"
#print(os.path.abspath(os.curdir))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.conf import settings
django.setup()
from terminals.models import Keys, Parser_users

def go():
    PU=Parser_users.objects.get(parser="trc")
    k1, k2, k3= pars_rtc.start(username=PU.username, password=PU.userpass, url=PU.parsurl)
    seter_list=[]
    for i in k1.keys():
        if k1[i]["key"]!=None:
            seter_list.append([k1[i]["key"], k1[i]["ip"].split(" / ")[0], k1[i]["version"], k1[i]["mid"]])
            #print(k1[i]["key"])
    return seter_list
def save(seter_ip):
    tz=2
    timer=(datetime.datetime.utcnow()+datetime.timedelta(hours=tz)).strftime("%d.%m.%y %H:%M")
    for set in seter_ip:
        print(set)
        logging.warning(set)
        try:
            key=Keys.objects.get(key=set[0])

        except Keys.DoesNotExist:
            print(set[0]+" - DoesNotExist")
            logging.error(set[0]+u" - DoesNotExist")
        else:
            key.ip = set[1]
            key.version=set[2]
            key.machine_id=set[3]
            key.date_last_online=timer
            key.save()
            print("Done")
            logging.warning("Done")

    print(len(seter_ip))
    logging.info(len(seter_ip))
def saver_go():
    logging.info(u"start")
    # tz=3
    # print((datetime.datetime.utcnow()+datetime.timedelta(hours=tz)).strftime("%d.%m.%y %H:%M"))
    seter_ip = go()
    save(seter_ip)

if __name__=="__main__":
    logging.info(u"start")
    #tz=3
    #print((datetime.datetime.utcnow()+datetime.timedelta(hours=tz)).strftime("%d.%m.%y %H:%M"))
    seter_ip=go()
    save(seter_ip)