# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
import json
#import runscript
from Lib import get_pid_of_log, test_procces, kill_proc
import pars_rtc
import json, os, subprocess
from mysite import settings
from terminals.models import Keys, Parser_users
#import pars_doc
from phonebook.save_Base import main
@permission_required('terminals.add_keys')
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
                "blocked":f.blocked,
                "ssh":on_keys[f.key]["ssh"],
                "vnc":on_keys[f.key]["vnc"],
                "x":on_keys[f.key]["x"],
                "upgrade":on_keys[f.key]["up"],
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
                        "upgrade":on_keys[f]["up"]
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
def get_ssh(request):
    if request.method=="POST":
	PU=Parser_users.objects.get(parser="trc")
        page=request.POST["page"].replace("./",PU.parsurl)
        #arg=request.arguments
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
def agreegate(request):
    if request.method == "POST":
        ls=request.POST.keys()
        """
        for key in ls:
            print(key, request.POST[key])
        """
        sub=[]
        #sub.append("sudo")
        #sub.append("-u")
        #sub.append("asorokin")
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
def agreegate_log(request):
    file_path=os.path.join(settings.LOG_DIR, "Agree.log")
    #li=file_path

    #print(file_path)
    try:
	f=open(file_path, "r")
    except Exception as (errno, strerror):
	li="I/O error({0}): {1}".format(errno, strerror)
    #li="Files open!"
    else:
    
	li=f.read().split("\n")
    
	#print(li)
	li="<br>".join(li)
	#print(li)
	f.close()
	#li="DONE"
    
    return HttpResponse(li)
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