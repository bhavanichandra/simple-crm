from django.db import models
# Create your models here.
from django.utils import timezone
from rest_framework import authentication, exceptions

from utility.core import generate_id, decode_jwt_token

AUTH_HEADER_TYPES = ('Bearer',)


class Role(models.Model):
    id = models.CharField(max_length=15, primary_key=True, null=False, blank=False, auto_created=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is None or self.id == '':
            self.id = generate_id()
        return super(Role, self).save(*args, **kwargs)


class User(models.Model):
    id = models.CharField(max_length=15, primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_id()
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)


class JWTAuthentication(authentication.BaseAuthentication):
    www_authenticate_realm = 'api'

    def has_permission(self, request, view, obj=None):
        return self.authenticate(request) is not None

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            raise exceptions.AuthenticationFailed("No Authorization header provided.")
        access_token = auth_header.split(' ')[1]
        try:
            decoded_token = decode_jwt_token(access_token)
            user = User.objects.get(id=decoded_token['id'])
            if user.role.code == 'SYSTEM_ADMIN':
                return {'id': user.id, 'role': user.role.code}, decoded_token
            else:
                raise exceptions.AuthenticationFailed("Only admins allowed")

        except Exception as ex:
            msg = ex.__str__()
            raise exceptions.AuthenticationFailed(msg)

    def authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm, )
