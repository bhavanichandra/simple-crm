from rest_framework import viewsets

from .models import User, Role, JWTAuthentication
from .serializers import UserSerializer, RoleSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [JWTAuthentication]


class RoleViewSet(viewsets.ModelViewSet):
    model = Role
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [JWTAuthentication]
