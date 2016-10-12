# -*- coding: utf-8 -*-
from django.shortcuts import render
from phonebook.forms import PhoneForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from phonebook.models import Phone, Partner, Club, Cash, Roll
from django.http import HttpResponse
import json

class PhoneBok(TemplateView):
    template_name ="phonebook.html"
    temp="phonebook1.html"
    model=Phone
    def get(self,request):

        if len(request.GET)>0:
            partners={}
            clubs={}
            cashs={}
            otvet={}
            select={}
            selpart=request.GET["partner"]
            selclub=request.GET["club"]
            selcash=request.GET["cash"]
            pa=Partner.objects.all()
            cl=Club.objects.all()
            ca=Cash.objects.all()
            if selpart!="":
                cl=Club.objects.filter(partner=selpart)
                ca=Cash.objects.filter(partner=selpart)
                selpart=int(selpart)
            if selclub!="":
                ca=Cash.objects.filter(club=selclub)
                clubobj=Club.objects.filter(id=selclub)[0]
                selpart=int(Partner.objects.filter(part_name=clubobj.partner)[0].id)
            if selcash!="":
                casobj=Cash.objects.filter(id=selcash)[0]
                selclub=int(Club.objects.filter(club_name=casobj.club)[0].id)
                selpart=int(Partner.objects.filter(part_name=casobj.partner)[0].id)
            for i in pa:
                partners[i.id]=i.part_name
            for i in cl:
                clubs[i.id]=i.club_name
            for i in ca:
                cashs[i.id]=i.cash_name
            select['partner']=selpart
            select["club"]=selclub
            select["cash"]=selcash
            otvet["partner"]=partners
            otvet["club"]=clubs
            otvet["cash"]=cashs
            otvet["select"]=select
            return HttpResponse(json.dumps(otvet))
        else:
            form=PhoneForm()
            return render_to_response(self.template_name,locals(),context_instance=RequestContext(request))
    def post(self,request):
        form=PhoneForm(request.POST)
        blago=""
        if form.is_valid():
            form.save()

            return render_to_response(self.temp,locals(),context_instance=RequestContext(request))

        else:
            return render_to_response(self.template_name,locals(),context_instance=RequestContext(request))


class PhoneBookView(TemplateView):
    temlate="phones.html"
    def get(self, request):
        phones=Phone.objects.all()
        return render_to_response(self.temlate, locals(),context_instance=RequestContext(request))