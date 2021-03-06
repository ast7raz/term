# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")
def current_datetime(request):
    current_date=datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
def hours_ahead(request, offset):
    try: 
        if len(str(offset))>1:
            if int(str(offset)[1])>4 or int(str(offset)[1])<0:
                ru="часов"
            elif int(str(offset)[1])>1:
                ru="часа"
            elif int(str(offset)[1])==1:
                ru="час"
        else:
            if int(str(offset))>4 or int(str(offset))<1:
                ru="часов"
            elif int(str(offset))>1:
                ru="часа"
            elif int(str(offset))==1:
                ru="час"
    
        hour_offset=int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now()+datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html', locals())
