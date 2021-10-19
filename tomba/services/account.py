from ..service import Service
from ..exception import TombaException

class Account(Service):

    def __init__(self, client):
        super(Account, self).__init__(client)

    def get_account(self):
        """Get Account"""

        params = {}
        path = '/me'

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
