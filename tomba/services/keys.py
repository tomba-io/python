from ..service import Service
from ..exception import TombaException

class Keys(Service):

    def __init__(self, client):
        super(Keys, self).__init__(client)

    def get_keys(self):
        """Get your keys."""

        params = {}
        path = '/keys/{id}'

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_key(self, id):
        """Delete key"""

        if id is None: 
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = '/keys/{id}'
        path = path.replace('{id}', id)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def create_key(self):
        """Create Key"""

        params = {}
        path = '/keys/{id}'

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def reset_key(self, id):
        """Reset a key"""

        if id is None: 
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = '/keys/{id}'
        path = path.replace('{id}', id)                

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)
