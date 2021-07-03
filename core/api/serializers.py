from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
        
class SignInCustomerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        return False
    class Meta:
        model = models.Customer
        fields = ['email', 'password']
        validators = []
        extra_kwargs = {'password': {'write_only': True}}   
