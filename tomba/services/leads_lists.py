from ..exception import TombaException
from ..service import Service


class LeadsLists(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_lists(self):
        """Get all leads lists.

        See: https://docs.tomba.io/api/leads-lists#get-leads-lists

        Returns:
            dict: API response containing leads lists.
        """

        params = {}
        path = "/leads_lists"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def delete_list_id(self, id):
        """Delete a leads list by ID.

        See: https://docs.tomba.io/api/lead-lists#delete-leads-list

        Args:
            id: The ID of the leads list to delete.

        Returns:
            dict: API response confirming deletion.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = "/leads_lists/{id}"
        path = path.replace("{id}", id)

        return self.client.call(
            "delete",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def create_list(self, **params):
        """Create a new leads list.

        See: https://docs.tomba.io/api/lead-lists#create-leads-list

        Args:
            **params: Keyword arguments for the list data (e.g., name).

        Returns:
            dict: API response containing the created list.
        """

        path = "/leads_lists"

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def update_list_id(self, id, **params):
        """Update a leads list by ID.

        See: https://docs.tomba.io/api/lead-lists#update-leads-list

        Args:
            id: The ID of the leads list to update.
            **params: Keyword arguments for the list data to update.

        Returns:
            dict: API response containing the updated list.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        path = "/leads_lists/{id}"
        path = path.replace("{id}", id)

        return self.client.call(
            "put",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
