# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from Lib import get_pid_of_log, test_procces, kill_proc
import pars_rtc
import json, os, subprocess, datetime
from mysite import settings
from terminals.models import Keys, Parser_users
from onliner.decorators import set_user_online
from logger.decorators import Added_action_terminal, Added_action_of_post
from logger.models import Logger_Action
from Lib import get_part_on_version_term
from terminals.pars_trcv2 import TRC_Parser
from phonebook.models import Partner
#import pars_doc
from phonebook.save_Base import main
@permission_required('terminals.add_keys')
@set_user_online
def keyonline(request):
        tizer={"key":"", "name":"", "part":"", "club":"", "adm":""}
        goll=[]
        goll2=[]
        new=0
        old=0
        PU=Parser_users.objects.get(parser="trc")
        on_keys, keys, ret_test=pars_rtc.start(username=PU.username, password=PU.userpass, url=PU.parsurl)
        #print()
        fi=Keys.objects.filter(key__in=keys).order_by("club","part")
        if len(request.GET)>0:

            if len(request.GET["key"])>0 :
                tizer["key"]=request.GET["key"]
                fi=fi.filter(key=request.GET["key"])
            if len(request.GET["name"])>0 :
                tizer["name"]=request.GET["name"]
                fi=fi.filter(name=request.GET["name"])
            if len(request.GET["part"])>0 :
                tizer["part"]=request.GET["part"]
                #print(tizer["part"])
                fi=fi.filter(part__part_name=request.GET["part"])
            if len(request.GET["club"])>0 :
                tizer["club"]=request.GET["club"]
                fi=fi.filter(club__club_name=request.GET["club"])
            if len(request.GET["admin"])>0 :
                tizer["adm"]=request.GET["admin"]
                fi=fi.filter(admin=request.GET["admin"])

        for f in fi:
            goll.append({
                "key":f.key,
                "name":f.name,
                "part":f.part,
                "club":f.club,
                "version":on_keys[f.key]["version"],
                "ip":on_keys[f.key]["ip"],
                "admin":f.admin,
                "pas":f.pas,
                "active":f.active,
                "blocked":f.in_blocked,
                "ssh":on_keys[f.key]["ssh"],
                "vnc":on_keys[f.key]["vnc"],
                "x":on_keys[f.key]["x"],
                "upgrade":on_keys[f.key]["up"],
                "mashine_id":on_keys[f.key]["mid"],
                })
            if "~" in on_keys[f.key]["version"]:
        	new +=1
    	    else:
    		old +=1
            goll2.append(f.key)

        if len(request.GET)==0:
            for f in keys:
                if on_keys[f]["key"] not in goll2:
                    #print(on_keys[f]["key"])
                    goll.append({
                        "key":on_keys[f]["key"],
                        "version":on_keys[f]["version"],
                        "ip":on_keys[f]["ip"],
                        "ssh":on_keys[f]["ssh"],
                        "vnc":on_keys[f]["vnc"],
                        "x":on_keys[f]["x"],
                        "upgrade":on_keys[f]["up"],
                        "mashine_id":on_keys[f]["mid"],
                        })
                    if "~" in on_keys[f]["version"]:
                	new+=1
            	    else:
            		old+=1
        lenfi=len(fi)
        lenkey=len(goll)
        #print(fi)
        #print(on_keys)
        return render_to_response("keys_onlyne.html",locals(),context_instance=RequestContext(request))
@permission_required('terminals.add_keys')
@Added_action_of_post
def get_ssh(request):
    if request.method=="POST":
        version=1
        if "V2" in  request.POST["fun"]:
            version=2

        #print(version)
        if version==1:
            PU=Parser_users.objects.get(parser="trc")
            page=request.POST["page"].replace("./",PU.parsurl)
            #arg=request.arguments
        else:
            PU = Parser_users.objects.get(parser="trcv2")
            page = request.POST["page"].replace("./", PU.parsurl)
            #print(page)
        #print(request.POST["fun"])
        if request.POST["fun"]!="X":
            li=pars_rtc.get_cmd(str(page), username=PU.username, password=PU.userpass).replace("$ ","")
        else:
            #print(page)
            pars_rtc.get_x(str(page), username=PU.username, password=PU.userpass)
            li="DONE"
        #print(li)
        #print(page)
        return HttpResponse(li)
@permission_required('terminals.add_keys')
@set_user_online
def keyoffline(request):
        goll=Keys.objects.all()
        tizer={"key":"", "name":"", "part":"", "club":"", "version":"", "ip":"", "mid":""}
        #key=''
        #name=''
        #part=''
        #club=''
        #version=''
        #ip=''
        if len(request.GET)>0:

            if len(request.GET["key"])>0 :
                goll=goll.filter(key__icontains=request.GET["key"])
                tizer["key"]=request.GET["key"]
            if len(request.GET["name"])>0 :
                goll=goll.filter(name__icontains=request.GET["name"])
                tizer["name"]=request.GET["name"]
            if len(request.GET["part"])>0 :
                goll=goll.filter(part__part_name__icontains=request.GET["part"])
                tizer["part"]=request.GET["part"]
            if len(request.GET["club"])>0 :
                goll=goll.filter(club__club_name__icontains=request.GET["club"])
                tizer["club"]=request.GET["club"]
            if len(request.GET["version"])>0 :
                goll=goll.filter(version__icontains=request.GET["version"])
                tizer["version"]=request.GET["version"]
            if len(request.GET["ip"])>0:
                goll=goll.filter(ip__icontains=request.GET["ip"])
                tizer["ip"]=request.GET["ip"]
            if len(request.GET["mid"])>0:
        	goll=goll.filter(machine_id=request.GET["mid"])
        	tizer["mid"]=request.GET["mid"]
        goll=goll.order_by("part", "club", "name")
        lenfi=len(goll)
        
        return render_to_response("keys_offline.html",locals(),context_instance=RequestContext(request))
@permission_required('terminals.change_keys')
@set_user_online
def agreegate(request):
    if request.method == "POST":
        ls=request.POST.keys()
        """
        for key in ls:
            print(key, request.POST[key])
        """
        sub=[]
        sub.append(settings.PYTHON)
        sub.append(os.path.join(settings.BASE_DIR, "manage.py"))
        sub.append("agree_base")
        if "part" not in request.POST:
            sub.append("-p")
        if "clubs" not in request.POST:
            sub.append("-c")
        if "Term" not in request.POST:
            sub.append("-t")
        else:
            if len(request.POST["last_page"])>0:
                sub.append("-l")
                sub.append(request.POST["last_page"])
        #print (sub)
        pid=get_pid_of_log(os.path.join(settings.LOG_DIR, "Agree.log"))
        proc=test_procces(pid, "agree_base")
        #print(pid, proc)
        if (len(pid)>0):
            if proc==False:
                subprocess.Popen(sub)
                le="Агрегация базы данных запущена. Информация о процессе агрегации будет отображаться ниже."
            elif proc=="":
                subprocess.Popen(sub)
                le="Агрегация"
            else:
                le = "Агрегация не была запущена потому чо процесс агрегации уже был запущен ранее!"
        else:
            le="Агрегация не была запущена по пречине ошибок!"
        return render_to_response("agreegate.html", locals(), context_instance=RequestContext(request))
    else:
        return render_to_response("agreegate.html",locals(),context_instance=RequestContext(request))
@permission_required('terminals.change_keys')
@set_user_online
def agreegate_log(request):
    file_path=os.path.join(settings.LOG_DIR, "Agree.log")
    #print(file_path)
    f=open(file_path, "r")
    li=f.read().split("\n")
    li="<br>".join(li)
    #print(li)
    f.close()
    #li="DONE"
    return HttpResponse(li)
@permission_required('terminals.change_keys')
def agreegate_stop(request):
    pid = get_pid_of_log(os.path.join(settings.LOG_DIR, "Agree.log"))
    proc = test_procces(pid, "agree_base")
    if (len(pid) > 0):
        if proc == True:
            if kill_proc(pid):

                li="Агрегация остановленна пользователем!"
            else:
                li = "Агрегация не была начата либо была завершена!"
        else:
            li = "Агрегация не была начата либо была завершена!"
    else:
        li = "Ошибка получения данных! Попробуйте ещё раз."
    return HttpResponse(li)
@permission_required('terminals.delete_keys')
@set_user_online
@Added_action_terminal
def mass_effects(request):
    if request.method=="POST":
        req=json.loads(request.body)
        #print(req)
        if req["command"]=="X"\
                or req["command"]=="block" \
                or req["command"] == "unblock"\
                or req["command"]=="update" \
                or req["command"]=="reboot" \
                or req["command"]=="restore_key" \
                or req["command"]=="soft_reboot"\
                or req["command"]=="swap_monitor"\
                or req["command"] == "kiosk"\
                or req["command"] == "run vnc"\
                or req["command"] == "disable gpu" \
                or req["command"] == "enable gpu":
            PU = Parser_users.objects.get(parser="trc")
        elif req["command"]=="white label BB"\
                or req["command"]=="white label Rub90"\
                or req["command"]=="update_V2"\
                or req["command"] == "reboot_V2" \
                or req["command"] == "restore_key_V2" \
                or req["command"] == "soft_reboot_V2" \
                or req["command"] == "swap_monitor_V2" \
                or req["command"] == "kiosk_V2" \
                or req["command"] == "run vnc_V2" \
                or req["command"] == "disable gpu_V2"\
                or req["command"]=="enable gpu_V2":
            PU = Parser_users.objects.get(parser="trcv2")
        else:
            PU=False
        if PU!=False:
            pars_rtc.begin_mass(req, PU.parsurl, PU.username, PU.userpass)
            li="done"
        else:
            li="Autoryz token not response"
        return HttpResponse(li)
    else:
        return HttpResponse("Not connect")
@permission_required('terminals.add_keys')

def get_info(request, id, version=1):
    if request.method == "POST":
        PU = Parser_users.objects.get(parser="trcv2")

        url=PU.parsurl+"info/"+id
        log=pars_rtc.get_term_info(url,PU.username, PU.userpass)
        return HttpResponse(log)
    else:
        PU = Parser_users.objects.get(parser="trc")
        dpkg=pars_rtc.send_cmd(PU.parsurl + id + "/cmd", PU.username, PU.userpass, "dpkg -l | grep white-label | grep ii")
        if dpkg!=None:
            wl=dpkg.split("          ")[-1]
        title = id + " log"
        actions=Logger_Action.objects.filter(object_name="Terminal", object=id).order_by("time").reverse()[:20]
        #print(actions)
        keys = Keys.objects.filter(machine_id=id)

        version=int(version)
        #print(version)

        return render_to_response("log_term.html", locals(), context_instance=RequestContext(request))

def get_part(request):
    if request.method != "POST":
        filt={"version":"", "number_of_days":365}
        if len(request.GET)>0:
            filt["version"]=request.GET["version"]
            filt["number_of_days"]=request.GET["Number_of_days"]
        date=datetime.datetime.utcnow()-datetime.timedelta(days=int(filt["number_of_days"]))
        partners = get_part_on_version_term(filt["version"], date)
        terms_on_part=[]
        for i in partners:
            keys = Keys.objects.filter(part=i)
            keys_new = keys.filter(version__icontains="~", date_time_last_online__gte=date)
            keys_old = keys.filter(version__icontains=".", date_time_last_online__gte=date)
            terms_on_part.append({"part_name":i.part_name, "coment":i.term_coment, "keys":len(keys), "new_term":len(keys_new), "old_term":len(keys_old)})
        return render_to_response("part_term.html", locals(), context_instance=RequestContext(request))
    else:
        body=json.loads(request.body)
        part=Partner.objects.get(part_name=body["partner"])
        part.term_coment=body["coment"]
        part.save()
        return HttpResponse("Done")

def keyonline_v2(request):
    tizer = {"key": "", "name": "", "part": "", "club": "", "adm": ""}
    goll = []
    goll2 = []
    lenkey=0
    old = 0
    online_keys=""
    PU = Parser_users.objects.get(parser="trcv2")
    online_keys=TRC_Parser(username=PU.username, password=PU.userpass, url=PU.parsurl)
    # print()
    fi = Keys.objects.filter(key__in=online_keys.get_list_keys()).order_by("club", "part")
    #print(fi)
    keys_online = []
    if len(request.GET) > 0:

        if len(request.GET["key"]) > 0:
            tizer["key"] = request.GET["key"]
            fi = fi.filter(key=request.GET["key"])
        if len(request.GET["name"]) > 0:
            tizer["name"] = request.GET["name"]
            fi = fi.filter(name=request.GET["name"])
        if len(request.GET["part"]) > 0:
            tizer["part"] = unicode(request.GET["part"])
            # print(tizer["part"])
            fi = fi.filter(part__part_name=unicode(request.GET["part"]))
        if len(request.GET["club"]) > 0:
            tizer["club"] = request.GET["club"]
            fi = fi.filter(club__club_name=request.GET["club"])
        if len(request.GET["admin"]) > 0:
            tizer["adm"] = request.GET["admin"]
            fi = fi.filter(admin=request.GET["admin"])
        #print(online_keys)
        if len(fi)>0:
            for i in fi:
                print(i)
                key=online_keys.get_key(str(i))
                key.part_name=i.part
                key.club_name=i.club
                key.name=i.name
                keys_online.append(key)

    else:
        if len(fi)>0:
            for i in fi:
                #print(i)
                key = online_keys.pop_key(str(i))
                key.part_name = i.part
                key.club_name = i.club
                key.name = i.name
                keys_online.append(key)

        for i in online_keys.get_list_keys():
            keys_online.append(i)
    lenfi=len(fi)
    lenkey = len(keys_online)
        #keys_online.extend(online_keys.keys)
        #keys_online=online_keys.get_list_keys()
    '''
    for f in fi:
        goll.append({
            "key": f.key,
            "name": f.name,
            "part": f.part,
            "club": f.club,
            "version": on_keys[f.key]["version"],
            "ip": on_keys[f.key]["ip"],
            "admin": f.admin,
            "pas": f.pas,
            "active": f.active,
            "blocked": f.blocked,
            "ssh": on_keys[f.key]["ssh"],
            "vnc": on_keys[f.key]["vnc"],
            "x": on_keys[f.key]["x"],
            "upgrade": on_keys[f.key]["up"],
            "mashine_id": on_keys[f.key]["mid"],
        })
        if "~" in on_keys[f.key]["version"]:
            new += 1
        else:
            old += 1


    goll2.append(f.key)

    if len(request.GET) == 0:
        for f in keys:
            if on_keys[f]["key"] not in goll2:
            # print(on_keys[f]["key"])
                goll.append({
                    "key": on_keys[f]["key"],
                    "version": on_keys[f]["version"],
                    "ip": on_keys[f]["ip"],
                    "ssh": on_keys[f]["ssh"],
                    "vnc": on_keys[f]["vnc"],
                    "x": on_keys[f]["x"],
                    "upgrade": on_keys[f]["up"],
                    "mashine_id": on_keys[f]["mid"],
                })
                if "~" in on_keys[f]["version"]:
                    new += 1
                else:
                    old += 1
    lenfi = len(fi)
    lenkey = len(goll)
    # print(fi)
    # print(on_keys)'''

    return render_to_response("keys_onlyne2.html", locals(), context_instance=RequestContext(request))


def Terminal_blocked(request, id=''):
    if request.method=="GET":
        if id=="":
            name=''
            mesage=''
        else:
            keys = Keys.objects.filter(machine_id=id)
            name=keys[0].name
            mesage=keys[0].mesage

        return render_to_response("term_first.html", locals(), context_instance=RequestContext(request))
    else:
        if id=="":
            return HttpResponse(True)
        else:
            keys = Keys.objects.filter(machine_id=id)
            blok=keys[0].in_blocked
            return HttpResponse(blok)

