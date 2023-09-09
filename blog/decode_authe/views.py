from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
menu = [
    {'title':'Home', 'url':'decode_blogs:home'},
    {'title':'Description', 'url':'decode_blogs:category'},
    {'title':'Регистрация', 'url':'decode_authe:signup'},
    {'title':'Вход', 'url':'decode_authe:signin'}
]

class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'decode_authe/signup.html'
    success_url = reverse_lazy('decode_blogs:home')     # Переход после создания продукта #

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context
    
class SignInUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'decode_authe/signin.html'


    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Авторизация'
        context['menu'] = menu

        return context
    
    def get_success_url(self):
        return reverse_lazy('decode_blogs:home')

def signout_user(request):             # Выход из аккаунта  #
    logout(request)   
    return redirect('decode_authe:signin')     

def profile(request):
    if not request.user.is_authenticated:
        return redirect('decode_authe:signin')
    
    data = {
        'title':'Профиль',
        'menu':menu
    }
    return render(request, 'decode_authe/profile.html', context=data)