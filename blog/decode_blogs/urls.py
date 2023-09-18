from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'', views.BlogViewSet, basename='blog')


app_name = 'decode_blogs'

urlpatterns = [
    path('', views.Home, name="home"),
    path('blogs/desc/<int:category_id>/', views.ShowBlog.as_view(), name='description'),
    path('blogs/<int:category_id>/', views.site_category, name='category'),
    path('add/', views.AddBlog.as_view(), name='add'),

    path('cmadd/', views.AddComment.as_view(), name='cmadd'),
    path('commentadd/<int:blog_id>/',views.AddComment.as_view(), name='comments-add'),    # Возможно удалить #
    path('testcommentview/<int:blog_id>/', views.BlogDetail.as_view(), name='comments-category'),
    
    path('', include(router.urls)),
]
