from ..service import Service
from ..exception import TombaException


class Verifier(Service):

    def __init__(self, client):
        super(Verifier, self).__init__(client)

    def email_verifier(self, email):
        """Email Verifier"""

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = '/email-verifier'

        if email is not None:
            params['email'] = email

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
