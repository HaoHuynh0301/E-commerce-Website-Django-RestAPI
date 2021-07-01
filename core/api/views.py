from django.shortcuts import render, get_object_or_404
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets 
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics

class ProductViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.AllowAny]
    serializer_class = serializers.ProductSerializer
    
    def get_queryset(self):
        return models.Product.objects.all()
    
    def get_object(self, queryset = None, **kwargs):
        productID = self.kwargs.get('id')
        return get_object_or_404(models.Product, pk = productID)
    
