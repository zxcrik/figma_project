from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'category', 'image', 'description', 'date']
        widgets = {
            'description':forms.Textarea(attrs={'rows':5})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['image','user', 'blog','text', 'date']
        widgets = {
            'description':forms.Textarea(attrs={'rows':3})
        }