# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse
import json
from load_averange.parse_rub90 import LoadAverange_p
@login_required
def LoadAv(request):

    r=LoadAverange_p(request.user.username)

    if request.method=="GET":
        #print(request.user.username)
        r.get_all_images()
        list=r.links_img
        return render_to_response("LA.html",locals(),context_instance=RequestContext(request))
    if request.method=="POST":
        name=request.POST["name"]
        #print(name)
        sl=r.get_img_by_name(name)
        return HttpResponse(json.dumps(sl))
"""
def LoadAv2(request):
    MS=request.COOKIES["csrftoken"]
    r=LoadAverange_p(MS[:3])
    if request.method=="GET":

        #r.get_all_images()
        list=r.links_img
        return render_to_response("LoAv.html",locals(),context_instance=RequestContext(request))
    if request.method=="POST":
        name=request.POST["name"]
        #print(name)
        sl=r.get_new_img_by_name(name)
        return HttpResponse(json.dumps(sl))"""