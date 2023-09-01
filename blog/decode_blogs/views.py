from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
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
        'comments': Comment.objects.all()
    }

    return render(request, 'decode_blogs/Home.html', data)


class CommentsBlog(ListView):
    model = Comment
    template_name = 'decode_blogs/Home.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        
        context['title'] = 'Комментарии'
        context['menu'] = menu
        context['categories'] = Category.objects.all()

        return context
    
def site_category(request, category_id):
    comments = Comment.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    data = {
        'comments':comments,
        'categories':categories,
        'menu':menu,
        'title':'Статьи',
        'category_id':category_id
    }

    return render(request, 'decode_blogs/Home.html', context=data) 


class AddComment(CreateView):
    form_class = CommentForm
    template_name = 'decode_blogs/Add-comment.html'
    success_url = reverse_lazy('decode_blogs:home.html')     # Переход после создания продукта #

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Новый блог'
        context['menu'] = menu

        return context

class ShowComment(DetailView):
    model = Comment
    template_name = 'decode_blogs/desc.html'
    pk_url_kwarg = 'product_id'       # Вместо primary key #
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Детали Блога'
        context['menu'] = menu

        return context