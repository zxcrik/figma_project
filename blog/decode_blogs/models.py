from django.db import models
import datetime
import uuid

# Create your models here.

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'images/{new_file_name}'


class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, upload_to=uniq_name_upload)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.today())
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self) -> str:
        return self.name