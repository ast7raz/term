__author__ = 'user'
from django import forms
from models import Sport,Calculate

class Calc(forms.Form):
    spo=Sport.objects.all()
    foo=[]
    for i in spo:
        foo.append(tuple((i.id,i.sport)))
    sport=forms.ChoiceField(choices=foo)