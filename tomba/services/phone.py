from ..service import Service
from ..exception import TombaException


class Phone(Service):

    def __init__(self, client):
        super(Phone, self).__init__(client)

    def finder(self, email):
        """Phone Finder"""

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = '/phone/'
        if email is not None:
            params['email'] = email

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def validator(self, phone):
        """Phone Validator"""

        if phone is None:
            raise TombaException('Missing required parameter: "phone"')

        params = {}
        path = '/phone-validator'

        if phone is not None:
            params['phone'] = phone

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
