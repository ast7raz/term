from django.contrib import admin
from reestrs.models import Request_Instrument, Request_type, Request_subject, Request_Reestr,Request_state
# Register your models here.
admin.site.register(Request_Instrument)
admin.site.register(Request_type)
admin.site.register(Request_subject)
admin.site.register(Request_Reestr)
admin.site.register(Request_state)
