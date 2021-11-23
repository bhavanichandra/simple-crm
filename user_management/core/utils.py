

from uuid import uuid4


def generate_id():
    uuid = uuid4().__str__().replace("-", "")
    return uuid.strip()[0:15].upper()