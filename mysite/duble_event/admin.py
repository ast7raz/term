from django.contrib import admin
from models import Parser_duble_event, Found_duplicates, Logging_duplicates, Exceptions, Audio_file, User_config, Image_file
class ParserAdmin(admin.ModelAdmin):
    fields = ("site_name", "pars_url", "login", "password","proxy_addr","proxy_port")
admin.site.register(Parser_duble_event,ParserAdmin)
class Logging_Admin(admin.ModelAdmin):
    fields = (("event1_id", "event1_team1","event1_team2", "event1_date", "event1_sport"), ("event2_id", "event2_team1","event2_team2", "event2_date", "event2_sport"),)
    list_display =("id", "date_started_duble","date_ended_duble")
admin.site.register(Logging_duplicates,Logging_Admin)
# Register your models here.
class Found_Admin(admin.ModelAdmin):
    fields = (("event1_id", "event1_team1","event1_team2", "event1_date", "event1_sport"), ("event2_id", "event2_team1","event2_team2", "event2_date", "event2_sport"),)
    list_display = ("id", "event1_id", "event2_id", "event1_sport", "logging_id")
admin.site.register(Found_duplicates, Found_Admin)
class ExceptionsAdmin(admin.ModelAdmin):
    fields = (("Symptom", "text"))
    list_display = ("Symptom","text")
admin.site.register(Exceptions, ExceptionsAdmin)
class AudioFileAdmin(admin.ModelAdmin):
    fields=("file_name", "file_path")
    list_display = ("file_name", "file_path")

admin.site.register(Audio_file, AudioFileAdmin)
class ImageFileAdmin(admin.ModelAdmin):
    fields=("file_name", "file_path")
    list_display=("file_name", "file_path")
admin.site.register(Image_file, ImageFileAdmin)




class UserConfigAdmin(admin.ModelAdmin):
    fields = ("user","audio_file","volume","image_file","transparent","hex_color")
    list_display = ("user","audio_file","volume","image_file","transparent","hex_color")
admin.site.register(User_config, UserConfigAdmin)