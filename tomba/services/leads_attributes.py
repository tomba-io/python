from ..service import Service
from ..exception import TombaException

class LeadsAttributes(Service):

    def __init__(self, client):
        super(LeadsAttributes, self).__init__(client)

    def get_lead_attributes(self):
        """Get Lead Attributes"""

        params = {}
        path = '/leads/attributes/{id}'

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_lead_attribute(self, id):
        """Delete Lead Attribute"""

        if id is None: 
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = '/leads/attributes/{id}'
        path = path.replace('{id}', id)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def create_lead_attribute(self):
        """Create Lead Attribute"""

        params = {}
        path = '/leads/attributes/{id}'

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def update_lead_attribute(self, id):
        """Update Lead Attribute"""

        if id is None: 
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = '/leads/attributes/{id}'
        path = path.replace('{id}', id)                

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)
