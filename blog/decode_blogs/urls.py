from django.urls import path, include
from . import views

app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home"),
    path('blogs/desc/<int:category_id>/', views.ShowBlog.as_view(), name='description'),
    path('blogs/<int:category_id>/', views.site_category, name='category'),
    path('add/', views.AddBlog.as_view(), name='add'),
    path('delete_blog/<int:blog_id>/', views.DeleteBlog.as_view(), name='delete-blog'),

    path('cmadd/', views.AddComment.as_view(), name='cmadd'),
    path('testcommentview/<int:blog_id>/', views.BlogDetail.as_view(), name='comments-category'),
    
    path('', include('rest_framework.urls')),
    path('', views.BlogListAPIView.as_view()),
    path('<int:pk>/',views.BlogDetailAPIView.as_view()),
]
