from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
menu = [
    {'title':'Home', 'url':'decode_blogs:home'},
    {'title':'Description', 'url':'decode_blogs:category'},
    {'title':'Sign up', 'url':'decode_authe:signup'},
    {'title':'Entering', 'url':'decode_authe:entering'}
]

class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'decode_authe/signup.html'
    success_url = reverse_lazy('decode_blogs:Home')     # Переход после создания продукта #

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context
    
class EnterUer():
    pass