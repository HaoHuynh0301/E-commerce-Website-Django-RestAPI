from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from io import BytesIO
from PIL import Image
from django.core.files import File

class CustomUserManager(BaseUserManager):
    def create_user(self, user_name, name, email, date_of_birth, password = None):
        if not email:
            raise ValueError("Customer must have email")
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            user_name = user_name,
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, user_name, name, email, date_of_birth, password = None):
        user = self.create_user(
            user_name = user_name,
            email = email,
            name = name,
            date_of_birth = date_of_birth,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

class Customer(AbstractBaseUser):
    email = models.EmailField(max_length = 255, unique = True, blank = False, verbose_name = 'email')
    name = models.CharField(max_length = 255, blank = False)
    user_name = models.CharField(max_length = 50, unique = True, blank = False)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'name', 'date_of_birth']
    
    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
    
    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True    
    
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
    
    @property
    def makeThumbnail(self, image, size = (300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)
        thumbnail = File(thumb_io, name = image.name)
        
        