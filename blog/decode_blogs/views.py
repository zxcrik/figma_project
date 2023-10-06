from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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
from .serializer import *
from django.http import Http404


menu = [
    {'title':'Home', 'url':'decode_blogs:home'},
    {'title':'Description', 'url':'decode_blogs:category'},   # Определение заголовков страницы #
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

    return render(request, 'decode_blogs/Home.html',  data)


class CategoriesBlog(ListView):
    model = Blog
    template_name = 'decode_blogs/Home.html'
    context_object_name = 'categories'
    

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        
        # Передача контекстных данных  #
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
    success_url = reverse_lazy('decode_blogs:home.html')     # Переход после создания блога #

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)

        context['title'] = 'Новый блог'
        context['menu'] = menu

        return context

def delete_blog(request, blog_id):           
    try:
        blog = Blog.objects.get(pk=blog_id)
        blog.delete()
        return redirect('decode_authe:profile')    # Переход после удаления #
    except Blog.DoesNotExist:
        return HttpResponse("Blog DoesNotExist") 

class EditBlog(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'decode_blogs/Edit-blog.html'  
    success_url = reverse_lazy('decode_blogs:home')
    
    def get_object(self):
        blog_id = self.kwargs['blog_id']
        return Blog.objects.get(pk=blog_id)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
def profile(request):
    user = request.user
    user_blogs = Blog.objects.filter(author=user)

    return render(request, 'profile.html', {'user_blogs': user_blogs})


class BlogSearchView(View):
    template_name = 'decode_blogs/Home.html'

    def post(self, request):
        form = BlogSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search']    # Получение данных введенных в форму #
            blogs = Blog.objects.filter(name__icontains=search_query)  # Поиск записей в Blog  #
            return render(request, 'decode_blogs/Home.html', {'blogs':blogs, 'query':search_query})
        return render(request, self.template_name, {'form':form})

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
    
def delete_comment(request, blog_id):           
    try:
        comment = Comment.objects.get(pk=blog_id)
        comment.delete()
        return redirect('decode_blogs:home')   
    except Comment.DoesNotExist:
        return HttpResponse("Comment DoesNotExist") 


class ShowComment(DetailView):
    model = Comment                     # Изменено на модель Comment, чтобы отображать комментарии
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
        context['comments'] = Comment.objects.filter(blog_id=self.kwargs['blog_id'])  # Комментарии относящиеся к этому блогу #
        context['categories'] = Category.objects.all()
        context['menu'] = menu
        return context


                # API #


class BlogListAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAdminOrReadOnly,)    # Класс для предоставления  доступа #


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,) 



class CommentListAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminOrReadOnly,)

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminOrReadOnly,) 


