from django.contrib.auth.hashers import check_password 
from django.contrib.auth.backends import BaseBackend
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from . import models

class SignInBackEnd:
    def authenticate(self, email = None, password = None):
        try:
            customer = models.Customer.objects.filter(email = email)
            if check_password(password, customer.get('password')):
                return customer
            print("Hello")
            return None
        except models.Customer.DoesNotExist:
            return None
            