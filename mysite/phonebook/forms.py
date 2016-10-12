# -*- coding: utf-8 -*-
__author__ = 'user'
from phonebook.models import Phone,Partner,Cash,Club,Roll
from django.forms import ModelForm
from django import forms
class PhoneForm(ModelForm):
    def clean_phone_number(self):
        data=self.cleaned_data['phone_number']
        objphone=Phone.objects.filter(phone_number=data)
        print(objphone)
        if len(str(data))==0:
            raise forms.ValidationError("Поле не может быть пустым!")
        elif len(str(data))!=11:
            raise forms.ValidationError("Не верное количество символов. Должно быть 11")
        elif len(objphone)>0:
            raise forms.ValidationError("Такой номер уже существует")
        return data
    """def clean_partner(self):
        data=self.cleaned_data['partner']
        if len(data)==0:
            raise forms.ValidationError("Поле не может быть пустым!")
        return data
    def clean_club(self):
        data=self.cleaned_data['club']
        if len(data)==0:
            raise forms.ValidationError("Поле не может быть пустым!")
        return data
    def clean_cash(self):
        data=self.cleaned_data['cash']
        if len(data)==0:
            raise forms.ValidationError("Поле не может быть пустым!")
        return data
    def clean_rol(self):
        data=self.cleaned_data['rol']
        if len(data)==0:
            raise forms.ValidationError("Поле не может быть пустым!")
        return data"""


    class Meta:
        model=Phone
        fields=["phone_number","partner","club",'cash','rol',"coment"]

