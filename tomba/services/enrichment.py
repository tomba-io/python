from ..service import Service
from ..exception import TombaException


class Enrichment(Service):

    def __init__(self, client):
        super(Enrichment, self).__init__(client)

    def person(self, email):
        """Person API"""

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = '/people/find'

        if email is not None:
            params['email'] = email

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def company(self, domain):
        """Company API"""

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/companies/find'

        if domain is not None:
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def combined(self, email):
        """Combined Person & Company API"""

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = '/combined/find'

        if email is not None:
            params['email'] = email

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
