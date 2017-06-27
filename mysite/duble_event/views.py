from django.shortcuts import render
from django.template import RequestContext
from django.core import serializers
from django.shortcuts import render_to_response
from duble_event.models import Found_duplicates, Logging_duplicates, Exceptions, Audio_file, Image_file, User_config
from django.http import Http404, HttpResponse
from duble_event.runer_lib import proccess_status,proccess_kill, proccess_started
from duble_event.starter import st
from django.contrib.auth.models import User
from mysite import settings
from django.core.serializers import serialize
import os
from datetime import datetime

import json
# Create your views here.
def page(request):
     stat=True
     find_dubles=Found_duplicates.objects.all()
     log_duplicates=Logging_duplicates.objects.all()
     exceptions=Exceptions.objects.all()
     return render_to_response("duble_event.html", locals(),context_instance=RequestContext(request))
def proc(request):
    if request.method == "POST":
        request_body=json.loads(request.body)
        #print(request_body["command"])
        if request_body["command"]=="Start":
            #proccess_started()
            loging_event=Logging_duplicates()
            loging_event.event1_id=0
            loging_event.event2_id = 0
            loging_event.event1_date=datetime.utcnow()
            loging_event.event2_date = datetime.utcnow()
            loging_event.event1_team1="Parser"
            loging_event.event1_team2="Start"
            loging_event.event2_team1 = "User"
            loging_event.event2_team2 = request.user
            loging_event.event1_sport="Info"
            loging_event.event2_sport = "Info"
            #print(loging_event)
            loging_event.save()
            st()
            #print(st())
        elif request_body["command"]=="Stop":
            loging_event = Logging_duplicates()
            loging_event.event1_id = 0
            loging_event.event2_id = 0
            loging_event.event1_date = datetime.utcnow()
            loging_event.event2_date = datetime.utcnow()
            loging_event.event1_team1 = "Parser"
            loging_event.event1_team2 = "Stop"
            loging_event.event2_team1 = "User"
            loging_event.event2_team2 = request.user
            loging_event.event1_sport = "Warning"
            loging_event.event2_sport = "Warning"
            # print(loging_event)
            loging_event.save()
            proccess_kill()
        return HttpResponse("done")
    elif request.method == "GET":
        stat=proccess_status()
        #print()
        return HttpResponse(stat)
    else:
        raise Http404

def data(request):
    if request.method=="GET":
        find_dubles = serializers.serialize("json",Found_duplicates.objects.all())
        log_duplicates = serializers.serialize("json", Logging_duplicates.objects.all())
        exceptions = serializers.serialize("json",Exceptions.objects.all())

        body={"dubles":find_dubles,"log":log_duplicates, "exception":exceptions}
        return HttpResponse(json.dumps(body))
def logdata(request):

    if request.method == "GET":
        log_dulecates=Logging_duplicates.objects.all()
        if request.GET["all"]!="true":
            log_dulecates=log_dulecates.order_by("-date_started_duble")[0:10]
        return HttpResponse(serializers.serialize("json", log_dulecates))
def dublesdata(request):
    if request.method=="GET":
        return HttpResponse(serializers.serialize("json", Found_duplicates.objects.all()))
def exceptdata(request):
    if request.method=="GET":
        req_list={
            "users":serializers.serialize("json",[User.objects.get(id=request.user.id)]),
            "exceptions":serializers.serialize("json", Exceptions.objects.all(), use_natural_foreign_keys=True, use_natural_primary_keys=True)

        }
        #print(req_list)
        return HttpResponse(json.dumps(req_list))
    elif request.method=="POST":
        request_body = json.loads(request.body)
        if request_body["command"]=="remove":
            obj=Exceptions.objects.get(id=request_body["id"])
            obj.delete()
            #print(obj)
        elif request_body["command"]=="add":
            obj=Exceptions()
            obj.Symptom = request_body["symptom"]
            obj.text = request_body["text"]
            #print(request.user.username)
            obj.user=request.user
            #print((obj.Symptom, obj.text))
            obj.save()

        return HttpResponse("Done")

def handle_uploaded_file(f, simptom):
    path=os.path.join(settings.STATIC_ROOT, simptom, f.name)
    #print(path)
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return path

def audiofile(request):
    if request.method=="POST":
        path=handle_uploaded_file(request.FILES[u"file"], "audio")
        try:
            Audio_file.objects.get(file_name=request.FILES[u"file"].name)
        except Audio_file.DoesNotExist:
            base_file=Audio_file()
            base_file.file_name=request.FILES[u"file"].name
            base_file.file_path=path
            base_file.save()
        return HttpResponse("Done")
    else:
        return HttpResponse(serializers.serialize("json", Audio_file.objects.all()))


def imagefile(request):
    if request.method=="POST":
        #print(request.FILES[u"file"])
        path=handle_uploaded_file(request.FILES[u"file"], "image")
        try:
            Image_file.objects.get(file_name=request.FILES[u"file"].name)
        except Image_file.DoesNotExist:
            base_file=Image_file()
            base_file.file_name=request.FILES[u"file"].name
            base_file.file_path=path
            base_file.save()
        return HttpResponse("Done")
    else:
        return HttpResponse(serializers.serialize("json", Image_file.objects.all()))

def User_Config(request):
    if request.method=="POST":
        body=json.loads(request.body)
        config=User_config.objects.select_related().get(user=request.user)
        config.audio_file=Audio_file.objects.get(file_name=body["fields"]["audio_file"]["fields"]["file_name"])
        config.image_file=Image_file.objects.get(file_name=body["fields"]["image_file"]["fields"]["file_name"])
        config.volume=body["fields"]["volume"]
        config.transparent=body["fields"]["transparent"]
        config.hex_color=body["fields"]["hex_color"]
        config.save()
        #print(body["fields"])
        return HttpResponse("Done")
    elif request.method=="GET":
        try:
            config=User_config.objects.select_related().get(user=request.user)
            #config.delete()
        except User_config.DoesNotExist:
            config=User_config()
            config.user=request.user
            try:
                audio=Audio_file.objects.get(file_name="alarm.mp3")
                config.audio_file = audio
            except:
                pass
            try:
                image=Image_file.objects.get(file_name="logo.png")
                config.image_file = image
            except:
                pass
            #print(audio)

            #print(config.audio_file.file_name)
            config.save()
        return  HttpResponse(serializers.serialize("json", [config], use_natural_keys=True, use_natural_primary_keys=True))