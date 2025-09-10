from ..service import Service
from ..exception import TombaException


class Domain(Service):

    def __init__(self, client):
        super(Domain, self).__init__(client)

    def domain_search(self, domain, page=None, limit=None, department=None, country=None):
        """Domain Search"""

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/domain-search'

        if domain is not None:
            params['domain'] = domain

        if page is not None:
            params['page'] = page

        if limit is not None:
            params['limit'] = limit

        if department is not None:
            params['department'] = department

        if country is not None:
            params['country'] = country

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
