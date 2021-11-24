from uuid import uuid4
def generate_id():
    """
    Generate a random id of 15 characters.
    """
    uuid = uuid4().__str__().replace("-", "")
    return uuid.strip()[0:15].upper()


def response_wrapper(is_success: bool = False, message: str = "", data=None):
    """
    Wrapper for the response.
    """
    if data is None:
        data = {}
    return {
        "success": is_success,
        "message": message or None,
        "data": data or None
    }


