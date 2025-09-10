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
        path = '/email-finder'

        if domain is not None:
            params['domain'] = domain

        if first_name is not None:
            params['first_name'] = first_name

        if last_name is not None:
            params['last_name'] = last_name

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def author_finder(self, url):
        """Author Finder"""

        if url is None:
            raise TombaException('Missing required parameter: "url"')

        params = {}
        path = '/email-finder'

        if url is not None:
            params['url'] = url

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def enrichment(self, email):
        """Enrichment"""

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = '/enrich'

        if email is not None:
            params['email'] = email

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def linkedin_finder(self, url):
        """Linkedin Finder"""

        if url is None:
            raise TombaException('Missing required parameter: "url"')

        params = {}
        path = '/linkedin'

        if url is not None:
            params['url'] = url

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def format(self, domain):
        """Email Format"""

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/format'

        if domain is not None:
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def location(self, domain):
        """Domain Location"""

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = '/location'

        if domain is not None:
            params['domain'] = domain

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
