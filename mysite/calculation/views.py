from django.shortcuts import render
from models import Sport,Calculate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import datetime
from forms import Calc

# Create your views here.
@login_required()
def calc_get(request):
    us=request.session.__getitem__('_auth_user_id')
    ob=Calculate.objects.get(worker__id=us)
    print(ob.date)
    if "sport" in request.GET:

        if "stater" in request.GET:
            if request.GET["stater"]=="true":
                ob.activ=True
                ob.sports=Sport.objects.get(id=request.GET["sport"])
            else:
                ob.activ=False
                ob.sports=Sport.objects.get(id=1)
    ob.save()
    form=Calc()

    date=datetime.datetime.now()
    td=datetime.timedelta(days=0, hours=0, seconds=15)
    te=Calculate.objects.filter(date__gte=date-td)


    te_del=Calculate.objects.exclude(date__gte=date-td)
    #print(te_del)
    for te_update in te_del:
        te_update.activ=False
        te_update.sports=Sport.objects.get(id=1)
        te_update.save
    if len(request.GET)>0:
        json_te=[]
        for qt in te:
            json_te.append({"worker":qt.worker.get_full_name(), "active":qt.activ, "sport":qt.sports.sport})
        return HttpResponse(json.dumps(json_te))
    else:
        return render_to_response("user_online.html",locals(),context_instance=RequestContext(request))



@login_required()
def calc_get_transparent(request):
    """us=request.session.__getitem__('_auth_user_id')
    ob=Calculate.objects.get(worker__id=us)
    print(ob.date)
    if "sport" in request.GET:

        if "stater" in request.GET:
            if request.GET["stater"]=="true":
                ob.activ=True
                ob.sports=Sport.objects.get(id=request.GET["sport"])
            else:
                ob.activ=False
                ob.sports=Sport.objects.get(id=1)
    ob.save()
    form=Calc()
"""
    date=datetime.datetime.now()
    td=datetime.timedelta(days=0, hours=0, seconds=15)
    te=Calculate.objects.filter(date__gte=date-td)


    te_del=Calculate.objects.exclude(date__gte=date-td)
    #print(te_del)
    for te_update in te_del:
        te_update.activ=False
        te_update.sports=Sport.objects.get(id=1)
        te_update.save
    if len(request.GET)>0:
        json_te=[]
        for qt in te:
            json_te.append({"worker":qt.worker.get_full_name(), "active":qt.activ, "sport":qt.sports.sport})
        return HttpResponse(json.dumps(json_te))
    else:
        return render_to_response("user_online_tr.html",locals(),context_instance=RequestContext(request))