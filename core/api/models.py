from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class Category(models.Model):
    name = models.CharField(max_length = 255, blank = True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['name', ]    
        
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE)
    name = models.CharField(max_length = 255, blank = True)
    slug = models.SlugField()
    description = models.CharField(max_length = 255, blank = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    image = models.ImageField(upload_to = 'images/', null = True, blank = True)
    thumbnail = models.ImageField(upload_to = 'image/', null = True, blank = True)
    date_published = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name', ]
        
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    @property
    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def thumbnailURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url