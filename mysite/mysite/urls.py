from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead
from books.views import display_meta, search, contact,register, account
from django.contrib.auth.views import login, logout
from phonebook.views import PhoneBok, PhoneBookView
from terminals.views import keyonline, keyoffline,agreegate,get_ssh, agreegate_log, agreegate_stop,mass_effects, get_info

from calculation.views import calc_get, calc_get_transparent
import settings
import os
#from load_averange.views import LoadAv #, LoadAv2
from reestrs.views import reestr_form, reestr_cash, cash_validation, reestr_save_req, reestr_spasibo, reestr_otc
templa={'template_name':os.path.join(settings.TEMPLATE_DIRS[0], "login.html")}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^static/', include(settings.STATICFILES_DIRS)),
    url(r"^hello/$", hello),
    url(r"^time/$", current_datetime),
    url(r"^time/(\d{1,2})/$", hours_ahead),
    url(r"^display/$", display_meta),
    url(r"^books/search/$", search),
    url(r"^contact/$", contact),
    url(r"^accounts/login/$", login, templa),
    url(r"^accounts/logout/$", logout),
    url(r"^accounts/account/$", account),
    url(r"^accounts/profile/$", account),
    url(r"^$", keyoffline),
    url(r"^register/$", register),
    url(r"^pb/$", PhoneBok.as_view()),
    url(r"^pb/view$", PhoneBookView.as_view()),
    url(r"^rtc/$", keyonline),
    url(r"^rtc/test/$", keyoffline),
    url(r"^rtc/info/(?P<id>\w+)/$", get_info),
    url(r"^rtc/info/(?P<id>\w+)/(?P<version>\d+)/$", get_info),

    url(r"^rtc/masseffect/$", mass_effects),
    url(r"^rtc/get_key/$", get_ssh),
    url(r"^agree/$", agreegate),
    url(r"^agree/log/$", agreegate_log),
    url(r"^agree/stop/$", agreegate_stop),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r"^calculate/$", calc_get),
    url(r"^calctrans/$", calc_get_transparent),
    #url(r"^la/$", LoadAv),
    url(r"^reestr/form/$", reestr_form),
    url(r"^reestr/form/cash/$", reestr_cash),
    url(r"^reestr/form/valid/$", cash_validation),
    url(r"^reestr/form/submit/$", reestr_save_req),
    url(r"^reestr/form/thank/(?P<id>\d+)/$", reestr_spasibo),
    url(r"^reestr/otc/$", reestr_otc),
    #url(r"^loav/$", LoadAv2),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
