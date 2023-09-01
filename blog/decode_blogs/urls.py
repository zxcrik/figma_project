from django.urls import path, include
from . import views


app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home"),
    path('blogs/desc/<int:category_id>/', views.ShowComment.as_view(), name='description'),
    path('blogs/<int:category_id>/', views.site_category, name='category'),
    path('add/', views.AddComment.as_view(), name='add')
]