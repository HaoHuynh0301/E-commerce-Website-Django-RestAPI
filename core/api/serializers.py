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
        
class SignInCustomerSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255, required = True)
    password = serializers.CharField()
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['email', 'user_name', 'name', 'date_of_birth', 'password']
        
class UpdateCustomerPassword(serializers.Serializer):
    email = serializers.EmailField(max_length = 255, required = True)
    password = serializers.CharField()
            
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['customer']

class TotalProductsOrderSerializer(serializers.Serializer):
    totalProduct = serializers.IntegerField()
    
class TotalProductsPriceOrderSerializer(serializers.Serializer):
    totalProductPrice = serializers.DecimalField(max_digits = 6, decimal_places = 2)

class TotalCategoryProductsSerializer(serializers.Serializer):
    totalProduct = serializers.IntegerField()
