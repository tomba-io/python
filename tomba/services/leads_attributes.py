from ..exception import TombaException
from ..service import Service


class LeadsAttributes(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_lead_attributes(self):
        """Get all lead attributes.

        See: https://docs.tomba.io/api/leads-attributes#get-lead-attributes

        Returns:
            dict: API response containing lead attributes.
        """

        params = {}
        path = "/attributes"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def delete_lead_attribute(self, id):
        """Delete a lead attribute by ID.

        See: https://docs.tomba.io/api/leads-attributes#delete-lead-attribute

        Args:
            id: The ID of the lead attribute to delete.

        Returns:
            dict: API response confirming deletion.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = "/attributes/{id}"
        path = path.replace("{id}", id)

        return self.client.call(
            "delete",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def create_lead_attribute(self, **params):
        """Create a new lead attribute.

        See: https://docs.tomba.io/api/leads-attributes#create-lead-attribute

        Args:
            **params: Keyword arguments for the attribute data.

        Returns:
            dict: API response containing the created attribute.
        """

        path = "/attributes"

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def update_lead_attribute(self, id, **params):
        """Update a lead attribute by ID.

        See: https://docs.tomba.io/api/leads-attributes#update-lead-attribute

        Args:
            id: The ID of the lead attribute to update.
            **params: Keyword arguments for the attribute data to update.

        Returns:
            dict: API response containing the updated attribute.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        path = "/attributes/{id}"
        path = path.replace("{id}", id)

        return self.client.call(
            "put",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
