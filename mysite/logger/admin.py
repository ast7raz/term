from django.contrib import admin
from models import Logger_Action

class Logger_Admin(admin.ModelAdmin):

    list_display = ("user", "action_name", "action", "object_name", "object", "time")
admin.site.register(Logger_Action, Logger_Admin)
# Register your models here.
