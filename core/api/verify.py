import jwt
from . import serializers, models
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class UpdatePasswordVerifyEmail(APIView):
    serializer_class = serializers.EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_ = openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            CustomerInstance = models.Customer.objects.get(id = payload['user_id'])
            CustomerInstance.is_active = True
            CustomerInstance.save()
            return Response({'email': 'Successfully updated'}, status = status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': str(identifier)}, status = status.HTTP_400_BAD_REQUEST)
        

class DeactivationCustomerVerifyEmail(APIView):
    serializer_class = serializers.EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_ = openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            CustomerInstance = models.Customer.objects.get(id = payload['user_id'])
            CustomerInstance.is_active = False
            CustomerInstance.save()
            return Response({'email': 'Successfully daactivated!'}, status = status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': str(identifier)}, status = status.HTTP_400_BAD_REQUEST)
        
        
class VerifyEmail(APIView):
    serializer_class = serializers.EmailVerificationSerializer
    token_param_config = openapi.Parameter(
        'token', in_ = openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(payload)
            CustomerInstance = models.Customer.objects.get(id = payload['user_id'])
            print(CustomerInstance)
            if not CustomerInstance.is_active:
                CustomerInstance.is_active = True
                CustomerInstance.save()
            return Response({'email': 'Successfully activated'}, status = status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': str(identifier)}, status = status.HTTP_400_BAD_REQUEST)
