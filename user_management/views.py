from rest_framework.viewsets import ModelViewSet

from .models import User, Role
from .serializers import UserSerializer, RoleSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
