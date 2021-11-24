class Login:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def __str__(self):
        return self.email

    def __dict__(self):
        return {
            'email': self.email,
            'password': self.password
        }


class Register:
    def __init__(self, email: str, password: str, confirm_password: str, name: str):
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.name = name

    def is_valid(self):
        return self.password == self.confirm_password

    def __str__(self):
        return self.email

    def __dict__(self):
        return {
            'email': self.email,
            'name': self.name,
            'password': self.password,
            'confirm_password': self.confirm_password
        }
