from ..service import Service
from ..exception import TombaException

class Logs(Service):

    def __init__(self, client):
        super(Logs, self).__init__(client)

    def get_logs(self):
        """get Logs"""

        params = {}
        path = '/logs'

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
