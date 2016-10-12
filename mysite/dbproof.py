# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.conf import settings
django.setup()
from terminals.models import Keys
from phonebook.models import Partner, Club

def save(key):
    try:
        keys=Keys.objects.get(key=key["key"])
        print(u"Уже создан ключ '"+keys.key+u"'")
    except:
        try:
            obj=Keys()
            obj.create_in_dict(key)
            #print(obj)
            obj.save()
            #print(u"Создан ключ '"+obj.key+u"'")
        except Exception:
            print(u"Ключ не создан из за ошибки")

if __name__ == "__main__":
    key={
    'admin': "",
    'part': 'Тест3',
    "club":"теструc2",
    'pas': "",
    'name': 'T-478',
    'key': 'Badkey36'}
    save(key)
