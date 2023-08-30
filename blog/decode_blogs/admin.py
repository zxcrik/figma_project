from django.contrib import admin
from .models import Category, Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','category','image','description','date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)