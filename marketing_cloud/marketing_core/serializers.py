from datetime import datetime

from rest_framework import serializers

from utility.db_util import DatabaseAdapter
from .models import UserAudit
from .mongo_models import Lead, Address, Account

# This is required to make connection with mongodb
mongo_adapter = DatabaseAdapter()


class UserAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAudit
        fields = '__all__'


class LeadSerializer(serializers.Serializer):
    """
    Serializer for Lead model
    """
    id = serializers.CharField(max_length=100, required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email_address = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)
    address = serializers.RelatedField(allow_null=True, required=False, queryset=Address.objects)
    account_id = serializers.RelatedField(allow_null=True, many=False, required=False, queryset=Account.objects)
    owner = serializers.CharField(max_length=50)
    created_by = serializers.CharField(max_length=50)
    updated_by = serializers.CharField(max_length=50)
    updated_at = serializers.DateTimeField(default=datetime.utcnow())
    created_at = serializers.DateTimeField(default=datetime.utcnow())

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return Lead(**validated_data).save()


class AddressSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100, required=False)
    street = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    zip = serializers.CharField(max_length=50)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        print(validated_data)
        return Address(**validated_data).save()
