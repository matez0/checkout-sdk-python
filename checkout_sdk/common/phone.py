from checkout_sdk.common import RequestDTO


class Phone(RequestDTO):
    def __init__(self, country_code, number):
        self.country_code = country_code
        self.number = number
