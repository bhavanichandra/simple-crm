from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from .utils import generate_id

# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data['id'] = generate_id
        return super().create(request, *args, **kwargs)


# class LoginViewSet(ViewSet):
#     def


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
