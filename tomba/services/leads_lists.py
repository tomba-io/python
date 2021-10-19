from ..service import Service
from ..exception import TombaException

class LeadsLists(Service):

    def __init__(self, client):
        super(LeadsLists, self).__init__(client)

    def get_lists(self):
        """Get Leads Lists"""

        params = {}
        path = '/leads_lists/{id}'

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_list_id(self, id):
        """Delete List ID"""

        if id is None: 
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = '/leads_lists/{id}'
        path = path.replace('{id}', id)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def create_list(self):
        """Create new List"""

        params = {}
        path = '/leads_lists/{id}'

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def update_list_id(self, id):
        """Update List ID"""

        if id is None: 
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = '/leads_lists/{id}'
        path = path.replace('{id}', id)                

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)
