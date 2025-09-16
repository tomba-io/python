from ..service import Service
from ..exception import TombaException


class Similar(Service):

    def __init__(self, client):
        super(Similar, self).__init__(client)

    def websites(self, domain):
        """retrieve similar domains based by a specific domain"""

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/similar'

        if domain is not None:
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
