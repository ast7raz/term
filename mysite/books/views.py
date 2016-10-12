# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from books.forms import ContactForm
from django.template import RequestContext
from django.http import HttpResponse
from books.forms import UserCreateForm, ChangePasswordForm
from calculation.models import Calculate,Sport
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect, requires_csrf_token, ensure_csrf_cookie, csrf_exempt
from social.backends.google import GoogleOAuth2
@csrf_exempt
@login_required()
def display_meta(request):
    host=request.get_host()
    path=request.get_full_path()
    values=request.META.items()
    values.sort()
    val=list(values)
    if request.method=="POST":
        return HttpResponse(val)
    else:
        return render_to_response("template_book.html", locals(), context_instance=RequestContext(request))
@permission_required('books.add_book')
def search_form(request):
    return render_to_response('search_form.html',context_instance=RequestContext(request))
@permission_required('books.add_book')
def search(request):
    error=False
    if 'q'in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        elif len(q)>20:
            error=True
        else:
            books=Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', locals(), context_instance=RequestContext(request))
    
    return render_to_response('search_form.html',locals(),context_instance=RequestContext(request))

@permission_required('books.add_book')
def contact(request):
    
    request.session['fav_color']='blue'
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            """send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@examle.com'),
                ['siteowner@example.com'],
                )"""
            return HttpResponseRedirect('/contact/')
    else:
        #if not request.user.is_authenticated():
            #return HttpResponseRedirect('/login/?next=%s' % request.path )
        form=ContactForm()
    return render_to_response('contact_form.html', locals(), context_instance=RequestContext(request))

@permission_required('books.add_book')
def register(request):
    if request.method == "POST":

        form = UserCreateForm(request.POST)
        if form.is_valid():
            use=(form.clean_username())
            gr=form.clean_groupers()
            form.save()
            us=User.objects.get(username=use)
            us2=us.groups.add(gr)
            ca=Calculate.objects.create(worker=us, sports=Sport.objects.get(sport="-----"))
            ca.save()
            return HttpResponseRedirect("/contact/")
    else:
        form = UserCreateForm()

    return render_to_response("register.html", locals(), context_instance=RequestContext(request))
@login_required()
def account(request):
    if request.method=="POST":
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            pa=form.cleaned_data.get("password1")
            us=User.objects.get(id=request.session.__getitem__('_auth_user_id'))
            us.set_password(pa)
            us.save()
            done="Ваш пароль сохранен!"
            return HttpResponseRedirect("/accounts/login/")
    else:
        form=ChangePasswordForm()
    return render_to_response("account.html", locals(), context_instance=RequestContext(request))

# Create your views here.

