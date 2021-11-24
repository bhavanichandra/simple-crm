from rest_framework import serializers

from core.models import User
from utility.validators import ERROR_MESSAGES


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages=ERROR_MESSAGES.get('email'))
    password = serializers.CharField(error_messages=ERROR_MESSAGES.get('password'))

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return validated_data

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            return {
                'id': user.id,
                'email': user.email,
                'role': user.role.code,
            }
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid Credentials')


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages=ERROR_MESSAGES.get('email'))
    password = serializers.CharField(max_length=32, min_length=5, error_messages=ERROR_MESSAGES.get('password'))
    confirm_password = serializers.CharField(max_length=32, write_only=True)
    name = serializers.CharField(max_length=150, error_messages=ERROR_MESSAGES.get('name'))
    role = serializers.CharField(max_length=150, required=False)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Password and Confirm Password must match')
        try:
            User.objects.get(email=email)
            raise serializers.ValidationError('User with this email already exists')
        except User.DoesNotExist:
            return data

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        :param validated_data: User Data
        :return: User
        """
        user_dict = {
            'email': validated_data.get('email'),
            'password': validated_data.get('password'),
            'name': validated_data.get('name'),
            'role': validated_data.get('role')
        }
        user = User(**user_dict)
        user.save(using='user_management')
        user_dict['id'] = user.id
        return user_dict

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
