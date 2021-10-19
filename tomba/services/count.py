from ..service import Service
from ..exception import TombaException

class Count(Service):

    def __init__(self, client):
        super(Count, self).__init__(client)

    def email_count(self, domain):
        """get Email Count"""

        if domain is None: 
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/email-count'

        if domain is not None: 
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
