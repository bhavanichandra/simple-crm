from rest_framework.viewsets import ViewSet

from .models import User, Role
from .serializers import UserSerializer, RoleSerializer


# Create your views here.


class UserViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(ViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
