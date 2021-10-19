from ..service import Service
from ..exception import TombaException

class Sources(Service):

    def __init__(self, client):
        super(Sources, self).__init__(client)

    def email_sources(self, email):
        """Email Sources"""

        if email is None: 
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = '/email-sources/{email}'
        path = path.replace('{email}', email)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
