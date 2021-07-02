from django.shortcuts import render, get_object_or_404
from . import models
from . import serializers
from .backend import SignInBackEnd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes
from rest_framework import viewsets 
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics

class ProductViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ProductSerializer
    
    def get_queryset(self):
        return models.Product.objects.all()
    
    def get_object(self, queryset = None, **kwargs):
        productID = self.kwargs.get('pk')
        return get_object_or_404(models.Product, pk = productID)
    
class CategoryViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializers_class = serializers.CategorySerializer
    
    def get_queryset(self):
        return models.Category.objects.all()
    
    def get_object(self, queryset = None, **kwargs):
        categoryID = self.kwargs.get('pk')
        return get_object_or_404(models.Category, id = categoryID)
    
class CustomerSignIn(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        print(request.data)
        try:
            customerInstance = SignInBackEnd.authenticate(
                                                        request.data.get('email'), 
                                                        request.data.get('password'))
            if customerInstance == None:
                return Response("EMAIL OR PASSWORD IS INVALID", status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response("BAD REQUEST", status = status.HTTP_400_BAD_REQUEST)
        serializer = serializers.SignInCustomerSerializer(customerInstance)
        return Response(serializer.data, status = status.HTTP_200_OK)