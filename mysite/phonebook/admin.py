from django.contrib import admin
from phonebook.models import Phone,Partner,Club,Cash,Roll

class PhoneAdmin(admin.ModelAdmin):
    list_display=('phone_number','coment','rol','partner','cash')
    search_fields=('phone_number','coment')

# Register your models here.
admin.site.register(Phone,PhoneAdmin)
admin.site.register(Partner)
admin.site.register(Club)
admin.site.register(Cash)
admin.site.register(Roll)
