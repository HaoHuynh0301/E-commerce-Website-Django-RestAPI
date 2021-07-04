from . import models
from . import serializers
from .backends import SignInBackEnd
from rest_framework import viewsets 
from rest_framework import permissions
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage

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
    serializer_class = serializers.CategorySerializer
    
    def get_queryset(self):
        return models.Category.objects.all()
    
    def get_object(self, queryset = None, **kwargs):
        categoryID = self.kwargs.get('pk')
        return get_object_or_404(models.Category, id = categoryID)
    
    @action(detail = True, methods = ['get'], permission_classes = [permissions.AllowAny])
    def getcategoryproduct(self, request, pk = None):
        Category = self.get_object(pk = pk)
        totalProduct = Category.getTotalProduct
        serializer = serializers.TotalCategoryProductsSerializer(data = {'totalProduct': totalProduct})
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class CustomerSignIn(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.SignInCustomerSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            Customer = authenticate(
                request,
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            if Customer:
                refresh = TokenObtainPairSerializer.get_token(Customer)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                return Response(data, status = status.HTTP_200_OK)
            return Response('EMAIL OR PASSWORD IS INCORRECT!', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RegisterCustomer(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.CustomerSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            newCustomer = serializer.save()
            return Response('CUSTOMER CREATED!', status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class UpdatePassword(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = serializers.UpdateCustomerPassword(data = request.data)
        if serializer.is_valid():
            # newPassword = make_password(serializer.validated_data['password'])
            CustomerInstance = models.Customer.objects.get(email = serializer.validated_data['email'])
            CustomerInstance.set_password(serializer.validated_data['password'])
            CustomerInstance.save()
            return Response("YOUR ACCOUNT WAS UPDATED!", status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class Test(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        mail_subject = 'Activate your blog account.'
        message = render_to_string('template.html', {
            'user': 'hao',
            'domain': 'http://127.0.0.1:8000/',
            'uid': 'uid',
            'token': 'token',
        })
        to_email = 'hao152903@gmail.com'
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        try:
            email.send()
            return Response("SEND", status = status.HTTP_200_OK)
        except Exception as err:
            return Response(str(err), status = status.HTTP_400_BAD_REQUEST)
    
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.OrderSerializer
    
    def get_queryset(self):
        return models.Order.objects.all()
    
    def get_object(self, queryset = None, **kwargs):
        orderID = self.kwargs.get('pk')
        return get_object_or_404(models.Order, id = orderID)
    
    @action(detail = True, methods = ['get'], permission_classes = [permissions.AllowAny])
    def totalproduct(self, request, pk = None):
        Order = self.get_object(pk = pk)
        totalProducts = Order.getTotalProducts
        print(totalProducts)
        serializer = serializers.TotalProductsOrderSerializer(data = {'totalProduct': totalProducts})
        if serializer.is_valid():
            context = {
                'totalProduct': str(serializer.validated_data['totalProduct'])
            }
            return Response(context, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    @action(detail = True, methods = ['get'], permission_classes = [permissions.AllowAny])
    def totalproductprice(self, request, pk = None):
        Order = self.get_object(pk = pk)
        totalProductPrice = Order.getTotalProductsPrice
        print(totalProductPrice)
        serializer = serializers.TotalProductsPriceOrderSerializer(data = {'totalProductPrice': totalProductPrice})
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)