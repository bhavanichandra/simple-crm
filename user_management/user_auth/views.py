# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from user_auth.serializers import LoginSerializer, RegisterSerializer
from utility.core import response_wrapper, generate_jwt_token


class LoginViewSet(ViewSet):

    def create(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            jwt_token = generate_jwt_token(valid_data)
            response_data = response_wrapper(is_success=True, data={'token': jwt_token}, message='Login Successful')
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            errors = list(serializer.errors.values())[0]
            response_data = response_wrapper(is_success=False, message='Login Failed', data=errors)
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(ViewSet):

    def create(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            saved_user = serializer.save(validated_data=serializer.validated_data)
            response_data = response_wrapper(is_success=True, data=saved_user, message='User Created Successfully')
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            errors = list(serializer.errors.values())[0]
            response_data = response_wrapper(is_success=False, message='User Creation Failed', data=errors)
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
