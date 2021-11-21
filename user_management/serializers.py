from rest_framework.serializers import HyperlinkedModelSerializer

from .models import User, Role


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class RoleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
