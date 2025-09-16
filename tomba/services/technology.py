from ..service import Service
from ..exception import TombaException


class Technology(Service):

    def __init__(self, client):
        super(Technology, self).__init__(client)

    def list(self, domain):
        """retrieve the technologies used by a specific domain"""

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/technology'

        if domain is not None:
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
