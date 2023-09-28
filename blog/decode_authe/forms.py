from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from PIL import Image

class SignUpUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class':'from-input'})
        }       

# class SignUpUserForm(forms.Form):
#     image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-input'}))
#     name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
#     first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-input'}))
#     last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))