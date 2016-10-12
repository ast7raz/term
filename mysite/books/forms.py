# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission, Group
class ContactForm(forms.Form):
    subject=forms.CharField(label="Тема письма:")
    message=forms.CharField(widget=forms.Textarea, label='Текст письма:')
    email=forms.EmailField(label='Ваш e-mail адрес:')

    def clean_message(self):
            message=self.cleaned_data['message']
            num_words=len(message.split())
            if num_words<4:
                raise forms.ValidationError("Слишком мало слов!")
            return message
# Create your tests here.
class UserCreateForm(UserCreationForm):
    ch=Group.objects.all()
    foo=[]
    for i in ch:
        foo.append(tuple((i.id,i.name)))
    #print(foo)

    email = forms.EmailField(required = True, error_messages = {'invalid': 'Введите корректный адрес электронной почты'})
    groupers= forms.ChoiceField(required=True, widget=forms.Select, choices=foo, label="Группы")

    class Meta:
        model = User


        fields = ( "username","first_name", "last_name", "email", "groupers")
    def clean_groupers(self):
        grouper=self.cleaned_data.get("groupers")
        return grouper
class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(),label="Новый пароль")
    password2 = forms.CharField(widget=forms.PasswordInput(),label="Подтверждение пароля")

    def clean(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")


        if password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        else:
            return cleaned_data