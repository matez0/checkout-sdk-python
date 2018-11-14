from checkout_sdk.common import RequestDTO


class Customer(RequestDTO):
    def __init__(self, id=None, email=None, name=None):
        self.id = id
        self.email = email
        self.name = name
