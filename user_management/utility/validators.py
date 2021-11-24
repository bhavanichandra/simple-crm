from typing import Union

from rest_framework.exceptions import ErrorDetail
from rest_framework.serializers import ValidationError

Conditions = list[dict[str, Union[str, int, bool]]]


def validate_password(password: str, conditions: Conditions = None):
    """
    Validate the password.
    """
    if not password or not password.strip():
        raise ValidationError("Password is required.")
    for condition in conditions or []:
        condition_name = condition.get('name')
        condition_value = condition.get('value')
        if condition_name == 'min_length' and len(password) < condition_value:
            raise ValidationError(f"Password must be at least {condition_value} characters long.")
        elif condition_name == 'max_length' and len(password) > condition_value:
            raise ValidationError(f"Password must be at most {condition_value} characters long.")
        elif condition_name == 'confirm_password' and password != condition_value:
            raise ValidationError("Passwords do not match.")
    return password


def required_validation(name: str, value: any):
    if value is None or str(value).strip() == '':
        raise ValidationError(detail=ErrorDetail(string=f"{name} is required."))
    return value


ERROR_MESSAGES = {
    'email': {'required': 'Email is required'},
    'password': {
        'required': 'Password is required',
        'max_length': 'Password must be at most 32 characters long',
        'min_length': 'Password must be at least 5 characters long'
    },
    'name': {'required': 'Name is required'},
}
