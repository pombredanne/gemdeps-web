from django import forms
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
