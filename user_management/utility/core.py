import os
import time
from uuid import uuid4

import jwt


def generate_id() -> str:
    """
    Generate a random id of 15 characters.
    """
    uuid = uuid4().__str__().replace("-", "")
    return uuid.strip()[0:15].upper()


def response_wrapper(is_success: bool = False, message: str = "", data=None) -> dict[str, any]:
    """
    Wrapper for the response.
    :param is_success: True if the request was successful, False otherwise
    :param message: Message to be returned
    :param data: Data to be returned
    :return: Dict of the parameters
    """
    if data is None:
        data = {}
    return {
        "success": is_success,
        "message": message or "Unexpected error occurred.",
        "data": data or None
    }


def generate_jwt_token(data: dict) -> str:
    """
    Generate a JWT token.
    :param data: Contains, id, email, and role of the loggedIn user
    :argument: test_token: If True, generate a test token
    :return: JWT token
    """
    jwt_str = jwt.encode({
        'id': data['id'],
        'email': data['email'],
        'exp': int(time.time()) + 3600,
        'role': data['role']
    }, str(os.getenv('JWT_SECRET_KEY')), algorithm='HS256')
    return jwt_str


def decode_jwt_token(token: str) -> dict[str, any]:
    """
    Decode a JWT token.
    :param token: JWT token
    :return: Dict of the parameters
    :raises:
        - ExpiredSignatureError: If the token is expired
        - InvalidTokenError: If the token is invalid
    """
    try:
        decoded_jwt = jwt.decode(token, str(os.getenv('JWT_SECRET_KEY')), algorithms=['HS256'])
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token.")
