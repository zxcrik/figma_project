from django.urls import path, include
from . import views


app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home")
]