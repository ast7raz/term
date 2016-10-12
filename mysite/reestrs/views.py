# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponse, redirect
from django.template import RequestContext
from django.core import serializers
import json
from social.apps.django_app.default.models import UserSocialAuth
from models import Request_Instrument
from phonebook.models import Cash, Club, Partner, Roll
from reestrs.models import Request_Instrument, Request_type, Request_subject, Request_Reestr

# Create your views here.
def reestr_form(request):
    instruments=Request_Instrument.objects.all()
    position=Roll.objects.all()
    requesttype=Request_type.objects.all()
    requestsubj=Request_subject.objects.all()
    return render_to_response('reestr.html', locals(),context_instance=RequestContext(request), )

def reestr_cash(request):
    if request.method=="POST":

        zapr=request.POST['value']
        if u"ББ" in zapr:
            zapr=zapr.replace(u"ББ",u"Бинго Бум")
        elif zapr==u"ПП":
            zapr=u"Потенциальный партнёр"
        elif zapr==u"ПО":
            zapr=u"Партнёрский Отдел"
        #print(zapr)
        cashs=Cash.objects.filter(cash_name__icontains=zapr).order_by("cash_name")
        #print(cashs)
        li=[]
        for cash in  cashs:
            li.append({'name':cash.cash_name, 'id':cash.id, 'pr':'cash', 'dop':[]})

        '''clubs=Club.objects.filter(club_name__contains=zapr)
        for club in clubs:
            li.append({'name':club.club_name, 'id':club.id, 'pr':'club'})
        '''
        partners=Partner.objects.filter(part_name__icontains=zapr).order_by("part_name")
        for partner in partners:
            cashs=Cash.objects.filter(partner=partner.id).order_by("cash_name")
            lis=[]
            for cash in cashs:
                lis.append({'name':cash.cash_name, 'id':cash.id, 'pr':'cash'})
            li.append({'name':partner.part_name, 'id':partner.id, 'pr':'part', 'dop':lis})

        return HttpResponse(json.dumps(li))
    else:
        return redirect('/reestr/form/')
def cash_validation(request):
    if request.method=="POST":
        val=request.POST["value"]
        try:
            otv=Cash.objects.get(cash_name=val)
        except Cash.DoesNotExist:
            try:
                otv=Partner.objects.get(part_name=val)
            except Partner.DoesNotExist:
                otv=[]
            except Partner.MultipleObjectsReturned:
                otv=[]
        except Cash.MultipleObjectsReturned:
            try:
                otv=Partner.objects.get(part_name=val)
            except Partner.DoesNotExist:
                otv=[]
            except Partner.MultipleObjectsReturned:
                otv=[]
        if type(otv)=="list":
            li={"error":"True", "priznak":"", "value":"", "text":""}
        else:
            try:
                print(otv.cash_name)
                li={"error":"False", "priznak":"cash", "value":otv.id, "text":otv.cash_name}
            except AttributeError:
                try:
                    print(otv.part_name)
                    li={"error":"False", "priznak":"part", "value":otv.id, "text":otv.part_name}
                except AttributeError:
                    li={"error":"True", "priznak":"", "value":"", "text":""}
        return HttpResponse(json.dumps(li))
    else:
        return redirect('/reestr/form/')
def reestr_save_req(request):
    obj=Request_Reestr().Create_In_Form(request.POST)
    #obj.Create_In_Form(request.POST)
    print(obj)
    #print(request.POST["coment"])

    """li={"time":obj.time,
        "user":obj.user.user.username,
        "partname":obj.partname,
        "clubname":obj.clubname,
        "instrument":obj.instrument.instrument,
        "state":obj.state.name,
        "error":"False"}"""

    li=[]
    li.append(obj)

    obj.save()
    #obj.refresh_from_db()
    data=serializers.serialize("json",li)
    print(obj.id)
    return HttpResponse(data)
def reestr_spasibo(request, id):
    obj=Request_Reestr.objects.get(id=id)
    print(id)
    return render_to_response('reestr_thank.html', locals(),context_instance=RequestContext(request), )
def reestr_otc(request):
    partners=Partner.objects.all()
    cashs=Cash.objects.all()
    """'reestr_otc.html'"""
    return render_to_response('Test.html', locals(),context_instance=RequestContext(request), )