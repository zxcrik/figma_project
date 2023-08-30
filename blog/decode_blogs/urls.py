from django.urls import path, include
from . import views


app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home"),
    path('blogs/<int:category_id>/', views.site_category, name='category'),
]