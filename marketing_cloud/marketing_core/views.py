import json

import rest_framework.status
from bson.json_util import dumps
from django.shortcuts import get_object_or_404
from mongoengine import Document
from rest_framework import viewsets
from rest_framework.response import Response

from utility import db_util
from .mongo_models import Lead, Address
from .serializers import LeadSerializer, AddressSerializer


class LeadView(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving leads.
    """

    def list(self, request):
        try:
            serializer = LeadSerializer(Lead.objects, many=True)
            response_wrapper = db_util.response_wrapper(is_success=True, data=serializer.data,
                                                        message="Leads fetched successfully")
        except Exception as e:
            response_wrapper = db_util.response_wrapper(is_success=False, data=None, message=e.__str__())
        return Response(data=response_wrapper)

    def retrieve(self, request, pk=None):
        try:
            user = get_object_or_404(Lead.objects, pk=pk)
            serializer = LeadSerializer(user)
            response_wrapper = db_util.response_wrapper(is_success=True, data=serializer.data,
                                                        message="Lead by primary key fetched successfully")
        except Exception as e:
            response_wrapper = db_util.response_wrapper(is_success=False, data=None, message=e.__str__())
        return Response(data=response_wrapper)

    def create(self, request):
        data = request.data
        print(data)
        serializer = LeadSerializer(data=data)
        if serializer.is_valid():
            saved_lead: Document = serializer.save()
            response_wrapper = db_util.response_wrapper(is_success=True, data=json.loads(dumps(saved_lead)),
                                                        message="Lead created successfully")
            return Response(data=response_wrapper, status=rest_framework.status.HTTP_201_CREATED)
        else:
            response_wrapper = db_util.response_wrapper(is_success=True, data=serializer.errors,
                                                        message="Lead Failed to create")
            return Response(data=response_wrapper, status=rest_framework.status.HTTP_200_OK)


class AddressViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Address.objects
            serializer = AddressSerializer(queryset, many=True)
            response_wrapper = db_util.response_wrapper(is_success=True, data=serializer.data,
                                                        message="Address fetched successfully")
        except Exception as e:
            response_wrapper = db_util.response_wrapper(is_success=False, data=None, message=e.__str__())
        return Response(data=response_wrapper)

    def retrieve(self, request, pk=None):
        try:
            address = get_object_or_404(Address.objects, pk=pk)
            serializer = AddressSerializer(address)
            response_wrapper = db_util.response_wrapper(is_success=True, data=serializer.data,
                                                        message="Lead by primary key fetched successfully")
        except Exception as e:
            response_wrapper = db_util.response_wrapper(is_success=False, data=None, message=e.__str__())
        return Response(data=response_wrapper)

    def create(self, request):
        data = request.data
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            saved_address: Document = serializer.save()
            response_wrapper = db_util.response_wrapper(is_success=True, data=json.loads(dumps(saved_address)),
                                                        message="Address created successfully")
            status = rest_framework.status.HTTP_201_CREATED
        else:
            response_wrapper = db_util.response_wrapper(is_success=True, data=serializer.errors,
                                                        message="Address Failed to create")
            status = rest_framework.status.HTTP_200_OK
        return Response(data=response_wrapper, status=status)
