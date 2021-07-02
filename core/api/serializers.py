from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['category', 'name', 'get_absolute_url', 'description',
                  'price', 'imgURL', 'thumbnailURL']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']