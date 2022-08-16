from dataclasses import field
from django import forms

from django.contrib.auth.forms import UserCreationForm

from account.models import User


class LoginForms (forms.Form):
    username = forms.CharField (max_length=50)
    password = forms.CharField (max_length=50, widget=forms.PasswordInput)

class SignUpForms (UserCreationForm):
    pass
    # class Meta:
    #     model = User
    #     field = 
