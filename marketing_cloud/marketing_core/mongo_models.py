from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, ReferenceField


class OwnerData(Document):
    """
    OwnerData for all models
    """
    meta = {"allow_inheritance": True, 'abstract': True}

    owner = StringField(max_length=50)
    created_by = StringField(max_length=50)
    updated_by = StringField(max_length=50)
    updated_at = DateTimeField(default=datetime.utcnow(), required=False)
    created_at = DateTimeField(default=datetime.utcnow(), required=False)


class BaseMarketingDocument(OwnerData):
    """
    Base class for all marketing documents.
    """
    meta = {"allow_inheritance": True, 'abstract': True}

    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    email_address = StringField(max_length=50)
    company = StringField(max_length=50)
    status = StringField(max_length=50)
    address = ReferenceField('Address', default=None, required=False)


# Create your models here.
class Prospect(BaseMarketingDocument):
    """
    Prospect model.
    """
    meta = {'collection': 'prospects'}


class Lead(BaseMarketingDocument):
    """
    Lead model.
    """
    account_id = ReferenceField('Account', default=None, required=False)

    meta = {'collection': 'leads'}


class Address(Document):
    """
    Address model.
    """
    street = StringField(max_length=50)
    city = StringField(max_length=50)
    state = StringField(max_length=50)
    country = StringField(max_length=50)
    zip = StringField(max_length=50)

    meta = {'collection': 'addresses'}


class Account(OwnerData):
    name = StringField(max_length=50)
    address = ReferenceField('Address')

    meta = {'collection': 'accounts'}
