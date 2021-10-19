from ..service import Service
from ..exception import TombaException

class Finder(Service):

    def __init__(self, client):
        super(Finder, self).__init__(client)

    def email_finder(self, domain, first_name, last_name):
        """Email Finder"""

        if domain is None: 
            raise TombaException('Missing required parameter: "domain"')

        if first_name is None: 
            raise TombaException('Missing required parameter: "first_name"')

        if last_name is None: 
            raise TombaException('Missing required parameter: "last_name"')

        params = {}
        path = '/email-finder/{domain}'
        path = path.replace('{domain}', domain)                

        if first_name is not None: 
            params['first_name'] = first_name

        if last_name is not None: 
            params['last_name'] = last_name

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
