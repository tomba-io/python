from ..service import Service
from ..exception import TombaException

class Usage(Service):

    def __init__(self, client):
        super(Usage, self).__init__(client)

    def get_usage(self):
        """get Usage"""

        params = {}
        path = '/usage'

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
