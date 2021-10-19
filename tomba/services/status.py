from ..service import Service
from ..exception import TombaException

class Status(Service):

    def __init__(self, client):
        super(Status, self).__init__(client)

    def domain_status(self, domain):
        """Domain status"""

        if domain is None: 
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/domain-status'

        if domain is not None: 
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def auto_complete(self, query):
        """get Company Autocomplete"""

        if query is None: 
            raise TombaException('Missing required parameter: "query"')

        params = {}
        path = '/domains-suggestion'

        if query is not None: 
            params['query'] = query

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
