from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from PIL import Image


class User(AbstractUser):
    userimage = models.ImageField(_('User Image'), upload_to='user_images/', blank=True, null=True)

    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)              # Обновление в user #
 
        if self.userimage:
            img = Image.open(self.userimage.path)


class SignUpUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('userimage','username', 'email','first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class':'from-input'}),
            'userimage':forms.FileInput(attrs={'class':'from-input'})
        }       

