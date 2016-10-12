__author__ = 'user'
from social.backends.google import GoogleOAuth2
from pprint import pprint
from social.pipeline.partial import partial
from social.exceptions import AuthException,AuthFailed
from django.shortcuts import render_to_response,redirect,render
from django.http import Http404
from django.contrib.auth.views import login

@partial
def pick_email_valide(backend, details, response, is_new=False, *args, **kwargs):
    #print(request.META.HTTP_HOST)
    wite_email_list=['firstgaming.com', 'firstgam.com']
    if backend.name == 'google-oauth2':
        data = backend.get_user_details(response)
        email_domen=data.get('email').split('@')[1]
        if email_domen not in wite_email_list:
            wite_email_string=" or ".join(wite_email_list)
            auth_errore='This email is not registered in %s! Try to enter again with another email.' % wite_email_string
            return render_to_response('login.html',{'auth_errore':auth_errore, "next":'/'})
        else:
            return

