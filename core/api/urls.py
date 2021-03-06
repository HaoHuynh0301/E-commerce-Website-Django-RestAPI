from django.contrib import admin
from django.urls import path, include 
from . import views, verify
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.schemas import get_schema_view

Router = DefaultRouter()
Router.register('product', views.ProductViewSet, basename = 'product')
Router.register('category', views.CategoryViewSet, basename = 'category')
Router.register('order', views.OrderViewSet, basename = 'order')

urlpatterns = [
    path('', include(Router.urls)),
    path('email-verify/', verify.VerifyEmail.as_view(), name="email-verify"),
    path('updatepass-verify/', verify.UpdatePasswordVerifyEmail.as_view(), name = 'update-password-verify'),
    path('deactivate-verify/', verify.DeactivationCustomerVerifyEmail.as_view(), name = 'deactivate-verify'),
    path('deactivate/', views.DeactivateCustomer.as_view(), name = 'deactivate'),
    path('signin/', views.CustomerSignIn.as_view(), name = 'signin'),
    path('register/', views.RegisterCustomer.as_view(), name = 'register'),
    path('update/', views.UpdatePassword.as_view(), name = 'update'),
]
