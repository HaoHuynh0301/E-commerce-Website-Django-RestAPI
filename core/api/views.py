from . import models, serializers, utils
from rest_framework import viewsets, permissions, status, generics
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.conf import settings

class ProductViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.ProductSerializer
    
    def get_queryset(self):
        return models.Product.objects.all()
    
    def get_object(self, queryset = None, **kwargs):
        productID = self.kwargs.get('pk')
        return get_object_or_404(models.Product, pk = productID)
    
    @action(detail = True, methods = ['get']):
    
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
        isValied = utils.Util.registerEmail(request, serializer)
        if isValied:
            return Response("YOUR ACCOUNT WAS CREATED!", status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
class DeactivateCustomer(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.DeactivateCustomerSerializer

    def put(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            Customer = authenticate(
                request,
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            if Customer:
                utils.Util.deactivateCustomer(request, Customer)
                return Response("CHECK YOUR EMAIL TO DEACTIVATE ACCOUNT", status = status.HTTP_200_OK)
        return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            Customer = authenticate(
                request,
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )
            try:
                if Customer.is_active:
                    return Response('YOUR ACCOUNT IS ACTIVATED', status = status.HTTP_200_OK)
            except:
                return Response('YOUR ACCOUNT IS NOT ACTIVATED', status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class UpdatePassword(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = serializers.UpdateCustomerPasswordSerializer(data = request.data)
        isValid = utils.Util.updatePassword(request, serializer)
        if isValid:
            return Response("YOUR PASSWORD WAS UPDATED", status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
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