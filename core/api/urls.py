from django.contrib import admin
from django.urls import path, include 
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.schemas import get_schema_view

app_name = 'api'

Router = DefaultRouter()
Router.register('product', views.ProductViewSet, basename = 'product')
Router.register('category', views.CategoryViewSet, basename = 'category')
Router.register('order', views.OrderViewSet, basename = 'order')

urlpatterns = [
    path('', include(Router.urls)),
    path('signin/', views.CustomerSignIn.as_view(), name = 'signin'),
    path('register/', views.RegisterCustomer.as_view(), name = 'register'),
    path('update/', views.UpdatePassword.as_view(), name = 'update')
]
