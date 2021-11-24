from rest_framework.serializers import ModelSerializer

from .models import User, Role


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        queryset = User.objects.all()
        exclude = ('password',)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class RoleSerializer(ModelSerializer):

    def create(self, validated_data):
        return Role.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Role
        fields = '__all__'
