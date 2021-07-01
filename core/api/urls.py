from django.contrib import admin
from django.urls import path, include 
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework.schemas import get_schema_view

app_name = 'api'

Router = DefaultRouter()
Router.register('', views.ProductViewSet, basename = 'product')

urlpatterns = [
    path('', include(Router.urls))
]
