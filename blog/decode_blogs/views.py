from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

menu = [
    {'title':'Home', 'url':'decode_blogs:home'},
    {'title':'Description', 'url':'decode_blogs:category'},
    {'title':'Регистрация', 'url':'decode_authe:signup'},
    {'title':'Вход', 'url':'decode_authe:signin'},

]

def Home(request):
    data = {
        'title':'Главная',
        'menu': menu,
        'categories': Category.objects.all(),
        'blogs': Blog.objects.all(),
    }

    return render(request, 'decode_blogs/home.html', data)


class CategoriesBlog(ListView):
    model = Blog
    template_name = 'decode_blogs/Home.html'
    context_object_name = 'categories'
    

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        
        
        context['title'] = 'Категории'
        context['menu'] = menu
        context['categories'] = Category.objects.all()

        return context
    
def site_category(request, category_id):
    blogs = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    data = {
        'blogs':blogs,
        'categories':categories,
        'menu':menu,
        'title':'Статьи',
        'category_id':category_id
    }

    return render(request, 'decode_blogs/Home.html', context=data) 


class AddBlog(CreateView):
    form_class = BlogForm
    template_name = 'decode_blogs/Add-blogs.html'
    success_url = reverse_lazy('decode_blogs:home.html')     # Переход после создания продукта #

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Новый блог'
        context['menu'] = menu

        return context

class ShowBlog(DetailView):
    model = Blog
    template_name = 'decode_blogs/desc.html'
    pk_url_kwarg = 'product_id'       # Вместо primary key #
    
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Детали Блога'
        context['menu'] = menu

        return context


class AddComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'decode_blogs/Add-comment.html'
    success_url = reverse_lazy('decode_blogs:home.html')     # Переход после создания продукта #
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Привязать комментарий к текущему пользователю #
        blog_id = self.kwargs.get('blog_id')
        if blog_id:                                # Связка комментария с определенным блогом #
            form.instance.blog_id = blog_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новый комментарий'
        context['menu'] = menu

        return context
    

class ShowComment(ListView):
    model = Comment  # Изменено на модель Comment, чтобы отображать комментарии
    template_name = 'decode_blogs/comment.html'
    pk_url_kwarg = 'comment_id'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обзор комментариев'
        context['menu'] = menu
        return context


def comments_category(request, comment_id, blog_id):
    comments = Comment.objects.filter(blog_id=blog_id)

    data = {
        'comments': comments,
        'menu':menu,
        'title':'Статьи',
        'comment_id':comment_id
    }

    return render(request, 'decode_blogs/comment.html', context=data) 
