'''
Created on 11 dic. 2017

@author: franklin
'''
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class cedulaWidget(forms.IntegerField):
    class Media:
        js = ('/scripts/validar.js')


class LoginAutenticationForm (AuthenticationForm):
    username = forms.CharField(max_length=100, 
                               widget = forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"), 
                               widget = forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))