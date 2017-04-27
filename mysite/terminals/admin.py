from django.contrib import admin
from models import Keys, Parser_users
class KeysAdmin(admin.ModelAdmin):
    fields = ("key", "name", "part", "club", "active", "blocked", "ip", "mesage", "in_blocked")
    list_display=('key', 'ip', 'name','part','club','version')
    search_fields=('key','name', "ip", "version")
admin.site.register(Keys,KeysAdmin)
class Parser_Users_Admin(admin.ModelAdmin):
    fields = ("username", "userpass", "parser", "parsurl", "pars_proxy")
admin.site.register(Parser_users, Parser_Users_Admin)
# Register your models here.
