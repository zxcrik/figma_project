from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'category', 'image', 'description', 'date']
        widgets = {
            'description':forms.Textarea(attrs={'rows':5})
        }
        
    def save(self, commit):
        author = settings.AUTH_USER_MODEL.objects.get(id=self.data['author_id'])
        self.instance.author = author
        return super().save(commit)


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = EditBlog
        fields = ['name', 'image', 'category', 'description']

    def save(self, commit=True):    # Автоматическое сохранение блога #
        blog = super().save(commit=False)
        if commit:
            blog.save()
        return blog



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'blog','text', 'date']
        widgets = {
            'description':forms.Textarea(attrs={'rows':3})
        }

class BlogSearchForm(forms.Form):
    search = forms.CharField(label='Поиск по блогам', max_length=100)    

