from django.urls import path, include
from . import views


app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home"),
    path('blogs/desc/<int:category_id>/', views.ShowBlog.as_view(), name='description'),
    path('blogs/<int:category_id>/', views.site_category, name='category'),
    path('add/', views.AddBlog.as_view(), name='add'),
    path('commentadd/<int:blog_id>/',views.AddComment.as_view(), name='comments-add'),
    path('comment/', views.ShowComment.as_view(), name='comments-category'),
    path('commentview/<int:blog_id>/<int:comment_id>/', views.comments_category, name='comments-review'),

]
