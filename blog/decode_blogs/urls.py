from django.urls import path, include
from . import views

app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home"),
    path('blogs/<int:category_id>/', views.site_category, name='category'),
    path('add/', views.AddBlog.as_view(), name='add'),
    path('search/', views.BlogSearchView.as_view(), name='blog-search'), # ! #
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete'), 
    path('edit_blog/<int:blog_id>/', views.EditBlog.as_view(), name='edit'),


    path('cmadd/', views.AddComment.as_view(), name='cmadd'),
    path('testcommentview/<int:blog_id>/', views.BlogDetail.as_view(), name='comments-category'),
    path('delete_comment/<int:blog_id>/', views.delete_comment, name='delete-comment'), 

    
    path('', include('rest_framework.urls')),
    path('', views.BlogListAPIView.as_view()),
    path('<int:pk>/',views.BlogDetailAPIView.as_view()),
]

