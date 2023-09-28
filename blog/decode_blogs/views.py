from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView     
from rest_framework.viewsets import ModelViewSet  
from rest_framework.decorators import action 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy 
from django.http import HttpResponse
from rest_framework.views import APIView     
from rest_framework.response import Response 
from django.views.generic import View
from .permissions import *
from .models import *
from .forms import *
from .models import *
from .serializer import *

# Create your views here.

menu = [
    {'title':'Home', 'url':'decode_blogs:home'},
    {'title':'Description', 'url':'decode_blogs:category'},
    {'title':'Регистрация', 'url':'decode_authe:signup'},
    {'title':'Вход', 'url':'decode_authe:signin'},

]

def Home(request):
    data = {
        'title':'Главная',
        'menu': menu,
        'categories': Category.objects.all(),
        'blogs': Blog.objects.all(),
    }

    return render(request, 'decode_blogs/Home.html', data)


class CategoriesBlog(ListView):
    model = Blog
    template_name = 'decode_blogs/Home.html'
    context_object_name = 'categories'
    

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        
        
        context['title'] = 'Категории'
        context['menu'] = menu
        context['categories'] = Category.objects.all()

        return context
    
def site_category(request, category_id):
    blogs = Blog.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    data = {
        'blogs':blogs,
        'categories':categories,
        'menu':menu,
        'title':'Статьи',
        'category_id':category_id
    }

    return render(request, 'decode_blogs/Home.html', context=data) 


class AddBlog(CreateView):
    form_class = BlogForm
    template_name = 'decode_blogs/Add-blogs.html'
    success_url = reverse_lazy('decode_blogs:home.html')     # Переход после создания продукта #

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Новый блог'
        context['menu'] = menu

        return context

class DeleteBlog(View):
    def get(self,request, blog_id):
        try:
            blog = Blog.objects.get(pk=blog_id)
            blog.delete()
        except Blog.DoesNotExist:
            return(f"{blog.name} not found")
        
        return redirect(f"{blog.name} was delete ")

class ShowBlog(DetailView):
    model = Blog
    template_name = 'decode_blogs/desc.html'
    pk_url_kwarg = 'blog_id'       # Вместо primary key #
    
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Детали Блога'
        context['menu'] = menu

        return context

        # Comments #

class AddComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'decode_blogs/Add-comment.html'
    success_url = reverse_lazy('decode_blogs:home')     # Переход после создания продукта #
    
    def form_valid(self, form):
        form.instance.user = self.request.user  # Привязать комментарий к текущему пользователю #
        blog_id = self.kwargs.get('blog_id')

        if blog_id:                                # Связка комментария с определенным блогом #
            form.instance.blog_id = blog_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новый комментарий'
        context['menu'] = menu

        return context
    

class ShowComment(DetailView):
    model = Comment  # Изменено на модель Comment, чтобы отображать комментарии
    template_name = 'decode_blogs/comment.html'
    pk_url_kwarg = 'comment_id'

    

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            return queryset.none()
        return queryset.filter(blog_id=self.blog_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обзор комментариев'
        context['blog'] = Blog.objects.get(id=self.blog_id)
        context['menu'] = menu
        return context
    

class BlogDetail(DetailView):
    model = Blog
    template_name = 'decode_blogs/comment.html'
    pk_url_kwarg = 'blog_id'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обзор блога'
        context['comments'] = Comment.objects.filter(blog_id=self.kwargs['blog_id'])
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


        # API ################################


class BlogListAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAdminOrReadOnly,)    # Класс для пред доступа #


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,) 

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,) 



# class BlogListAPIView(ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer        # Передача пареметров #


# class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# class BlogApiView(APIView):           
#     def get(self,request):
#         blog = Blog.objects.all()
#         return Response({'blog': BlogSerializer(blog, many=True).data})
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)       
#         serializer.save()

#         return Response({'blog':serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if not pk:
#             return Response({'error':'method "Put" not allowed'})
        
#         try:
#             instance = Blog.objects.get(pk=pk)

#         except:
#             return Response({'error':'Object does not exist'})
        
#         serializer = BlogSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)        
#         serializer.save()

#         return Response({'blog': serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)

#         if not pk:
#             return Response({'error':'method "delete" not allowed'})

#         try:
#             instance = Blog.objects.get(pk=pk)
#             instance.delete()

#         except:
#             return Response({'error':'Object does not exist'})

#         return Response({'status': 'blog was deleted'})



