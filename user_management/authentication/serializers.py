from rest_framework import serializers

from core.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=32)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return validated_data

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            return user.get_dict()
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid Credentials')


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=32)
    confirm_password = serializers.CharField(max_length=32, write_only=True)
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Password and Confirm Password does not match')
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError('Email already exists')
        except User.DoesNotExist:
            return User(name=data.get('name'), email=data.get('email'), password=data.get('password'))
