# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from utility.core import response_wrapper
from .serializers import LoginSerializer


class LoginViewSet(ViewSet):

    def create(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data
            print('user_data', user)
            response_data = response_wrapper(is_success=True, data=user, message='Login Success')
            status_code = status.HTTP_200_OK
        else:
            print('login_serializer', serializer.errors)
            response_data = response_wrapper(is_success=False, data=serializer.errors, message='Login Failed')
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        print('final response', response_data)
        return Response(data=response_data, status=status_code)


class RegisterView(ViewSet):
    pass
