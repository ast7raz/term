from django.contrib import admin
from models import User_Sessions
from django.contrib.sessions.models import Session
# Register your models here.
class User_Session_Admin(admin.ModelAdmin):
    fields=("user", "session")
admin.site.register(User_Sessions,User_Session_Admin)
class Session_Admin(admin.ModelAdmin):
    fields = ("session_key", "session_data", "expire_date")
    list_display = ("session_key", "session_data", "expire_date")
    search_fields = ('session_key',)
admin.site.register(Session, Session_Admin)