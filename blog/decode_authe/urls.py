from django.urls import path, include
from django.contrib import admin
from . import views


app_name = 'decode_authe'

urlpatterns = [
    path('signup/',views.SignUpUser.as_view(), name='signup'),
    path('signin/',views.SignInUser.as_view() ,name='signin'),
    path('signout/',views.signout_user , name='signout'),
    path('profile/', views.profile, name='profile')
]