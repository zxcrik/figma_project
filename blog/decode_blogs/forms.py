from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'category', 'image', 'description', 'date']
        widgets = {
            'description':forms.Textarea(attrs={'rows':5})
        }