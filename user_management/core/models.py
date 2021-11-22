from django.db import models


# Create your models here.

class Role(models.Model):
    id = models.CharField(max_length=15, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.CharField(max_length=15, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

