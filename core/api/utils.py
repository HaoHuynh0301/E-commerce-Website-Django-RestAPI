from django.core.mail import EmailMessage
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
import threading

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class Util:
    @staticmethod
    def sendEmail(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()
    @staticmethod
    def registerEmail(request, serializer):
        isValid = False
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            newCustomer = serializer.save()
            token = RefreshToken.for_user(newCustomer).access_token
            currentSite = get_current_site(request).domain
            relativeLink = reverse('email-verify')
            absurl = 'http://' + currentSite + relativeLink + "?token=" + str(token)
            emailBody = 'Hi '+ newCustomer.name + \
            ' Use the link below to verify your email \n' + absurl
            data = {'email_body': emailBody, 'to_email': newCustomer.email,
                'email_subject': 'Verify your email'}
            Util.sendEmail(data)
            isValid = True
        return isValid
    
    def 