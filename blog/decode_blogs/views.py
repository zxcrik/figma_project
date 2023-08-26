from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponse
# from .models import 
from .forms import *

# Create your views here.

menu = [
    {'title':'Home', 'url':'decode_blogs:Decode'},

]

def Home(request):
    data = {
        'title':'Главная',
        'menu': menu,
    }

    return render(request, 'decode_blogs/Home.html', data)