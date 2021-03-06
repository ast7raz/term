# -*- coding: utf-8 -*-
__author__ = 'user'
import urllib2
from urllib import urlencode
import lxml.html as html
from mysite.settings import DIR_SPLITTER
import logging, os
from src_rclua import get_rc
from terminals.models import Keys
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
    #print(text)
    #print("get_cmd Print r: "+text)
    page=html.document_fromstring(text)
    #print(page)
    if "v2" not in url:
        li=page.xpath("/html/body/pre")[0].text
    else:
        #print("v2")
        a=page.xpath("/html/body/pre[3]/a[2]")[0].text
        li=page.xpath("/html/body/pre[3]/text()")[0].split("\n")[3]+a
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
def begin_mass(jso, url, username, password):
    #print(Get_project_path())
    for id in jso["ids"]:
        if jso["command"]=="X":
            get_x(url+id+"/"+"x", username, password)
        elif jso["command"]=="update":
            get_x(url + id + "/" + "upgrade", username, password)
        elif jso["command"] == "update_V2":
            get_x(url + "/upgrade/"+id, username, password)
        elif jso["command"] == "reboot":
            send_cmd(url + id + "/cmd", username, password, jso["command"])
            get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "reboot_V2":
            send_cmd(url + "/command/"+ id, username, password, "reboot")
            #get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "restore_key":
            send_cmd(url + id + "/cmd", username, password, """wget --method=PUT --body-data='%s' http://localhost/key && wget -t 1 -o- --post-data='' http://localhost/shutdown/soft""" %jso["key"])
            get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "block":
            try:
                term=Keys.objects.get(machine_id=id)
                term.in_blocked=True
                term.save()
            except:
                print("ERRORE")
            patch=os.path.dirname(Get_project_path())
            patch=os.path.join(patch, "static", "termfiles")
            #print(patch)
            file_name=os.path.join(patch, "rc.lua_%s_rub90" %(id))
            #print(file_name)
            #print(get_rc(id))
            fi=open(file_name, "w")
            #print(fi)
            fi.write(get_rc(id))
            #print(fi)
            fi.close()
            send_cmd(url + id + "/cmd", username, password,
                     """wget http://support.firstgaming.com/static/termfiles/rc.lua_%s_rub90 && cp rc.lua_%s_rub90 /usr/share/rub90/config/awesome/rc.lua && rm rc.lua_%s_rub90 && wget -t 1 -o- --post-data="" http://localhost/shutdown/soft""" %(id, id, id))
            get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "unblock":
            try:
                term = Keys.objects.get(machine_id=id)
                print(term)
                term.in_blocked = False
                term.save()
            except:
                print("ERRORE")
            send_cmd(url + id + "/cmd", username, password,
                     """wget http://support.firstgaming.com/static/termfiles/rc.lua_default_rub90 && cp rc.lua_default_rub90 /usr/share/rub90/config/awesome/rc.lua && rm rc.lua_default_rub90 && wget -t 1 -o- --post-data="" http://localhost/shutdown/soft""")
            get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "soft_reboot":
            send_cmd(url + id + "/cmd", username, password,
                     "wget -t 1 -o- --post-data='' http://localhost/shutdown/soft")
            get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "soft_reboot_V2":
            send_cmd(url + "/command/"+id, username, password,
                     "wget -t 1 -o- --post-data='' http://localhost/shutdown/soft")
            #get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "swap_monitor":
            send_cmd(url + id + "/cmd", username, password, "wget -t 1 -o- --post-data="" http://localhost/swap")
        elif jso["command"] == "swap_monitor_V2":
            send_cmd(url + "/command/"+id, username, password, "wget -t 1 -o- --post-data="" http://localhost/swap")
        elif jso["command"] == "kiosk":
            send_cmd(url + id + "/cmd", username, password, "wget -t 1 -o- --post-data="" http://localhost/toggle_kiosk")
            #get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "kiosk_V2":
            send_cmd(url + "/command/"+id, username, password,
                     "wget -t 1 -o- --post-data="" http://localhost/toggle_kiosk")
            # get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "enable gpu":
            send_cmd(url + id + "/cmd", username, password,
                     "wget  http://support.firstgaming.com/static/en_kiosk.sh && rm /etc/skelconfig/awesome/kiosk.sh && cp en_kiosk.sh /etc/skelconfig/awesome/kiosk.sh && chmod 755 /etc/skelconfig/awesome/kiosk.sh && rm en_kiosk.sh && service slim restart")
            # get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "enable gpu_V2":
            send_cmd(url + "/command/"+id, username, password,
                     "wget  http://support.firstgaming.com/static/en_kiosk.sh && rm /etc/skelconfig/awesome/kiosk.sh && cp en_kiosk.sh /etc/skelconfig/awesome/kiosk.sh && chmod 755 /etc/skelconfig/awesome/kiosk.sh && rm en_kiosk.sh && service slim restart")
            # get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "disable gpu":
            send_cmd(url + id + "/cmd", username, password,
                     "wget  http://support.firstgaming.com/static/di_kiosk.sh && rm /etc/skelconfig/awesome/kiosk.sh && cp di_kiosk.sh /etc/skelconfig/awesome/kiosk.sh && chmod 755 /etc/skelconfig/awesome/kiosk.sh && rm di_kiosk.sh && service slim restart")
            # get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "disable gpu_V2":
            send_cmd(url + "/command/"+id, username, password,
                     "wget  http://support.firstgaming.com/static/di_kiosk.sh && rm /etc/skelconfig/awesome/kiosk.sh && cp di_kiosk.sh /etc/skelconfig/awesome/kiosk.sh && chmod 755 /etc/skelconfig/awesome/kiosk.sh && rm di_kiosk.sh && service slim restart")
            # get_x(url + id + "/" + "x", username, password)
        elif jso["command"] == "run vnc":
            run_vnc(url + id + "/cmd", username, password)
        elif jso["command"] == "run vnc_V2":
            run_vnc(url + "/command/"+id, username, password)
        elif jso["command"]=="white label Rub90":
            get_x(url +"/upgrade/"+id+"?white_label=rub90", username, password)
        elif jso["command"] == "white label BB":
            get_x(url + "/upgrade/" + id + "?white_label=bingo-boom", username, password)
        else:

            pass
    return True
def get_term_info(url, username, password):
    logging.debug(url)
    pass_man = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # logging.debug("X1 Done")
    pass_man.add_password(None, url, username, password)
    auth_handler = urllib2.HTTPBasicAuthHandler(pass_man)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    logging.debug("X2 Done")
    
    try:
        r = urllib2.urlopen(url).read()
        body2=r.split("<p>Last upgrade log:</p>")
        #print(len(body2))
        log=body2[-1].replace("\n</p>\n\n</body>\n</html>\n","")
        if len(body2)>1:
            return log
        else:
            return "На данный момент действий с этим терминалом не производилось."
    except Exception as e:
        # print(e)
        logging.info(e)
        return "Извените в данный момент лог не доступен."

def send_cmd(url, username, password, command):
    logging.debug(url)
    pass_man = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # logging.debug("X1 Done")
    pass_man.add_password(None, url, username, password)
    auth_handler = urllib2.HTTPBasicAuthHandler(pass_man)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    logging.debug("X2 Done")
    req=urllib2.Request(url, urlencode({"command":command},))
    r="test"
    try:
        r = urllib2.urlopen(req,timeout=0.5)

    except Exception as e:
        #print(e)
        logging.info(e)
    # logging.info(e.read())
    #print(r)
    if isinstance(r, object):
        try:
            text=r.read()
            #print(text)
            page = html.document_fromstring(text)
            # print(page)
            li = page.xpath("/html/body/pre")[0].text
            # print(li)
            return li
        except:
            pass

    logging.debug("x3 Done")
def test_proc(url, username, password, proc):
    command="su rub90 -c 'pgrep %s'" %proc
    otv=send_cmd(url,username,password, command)
    if otv!=None and otv!="":
        return True
    else:
        return False
def run_vnc(url, username, password):
    if not test_proc(url, username, password, "x11vnc"):
       send_cmd(url, username, password, "su rub90 -c 'while true; do x11vnc -usepw -display :0 -q -forever; done;'")
if __name__ == "__main__":

    pass
