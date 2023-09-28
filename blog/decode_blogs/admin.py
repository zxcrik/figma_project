from django.contrib import admin
from .models import Category, Blog, Comment

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name','category','image','description','date')
    list_filter = ('category',)

     
    actions = ['delete_selected']
    
  
    def has_delete_permission(self, request, obj=None):
        return True

  
    def delete_selected(self, request, queryset):
        queryset.delete()

    delete_selected.short_description = "Удалить выбранные блоги"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','text', 'date')