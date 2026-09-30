from ..exception import TombaException
from ..service import Service


class Leads(Service):
    def __init__(self, client):
        super().__init__(client)

    def list_leads(self, page=None, limit=None, domain=None):
        """Get all leads.

        See: https://docs.tomba.io/api/leads

        Args:
            page: The page number for pagination.
            limit: The number of results per page.
            domain: Filter leads by domain.

        Returns:
            dict: API response containing leads.
        """

        params = {}
        path = "/leads"

        if page is not None:
            params["page"] = page

        if limit is not None:
            params["limit"] = limit

        if domain is not None:
            params["domain"] = domain

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def get_lead(self, lead_id):
        """Get a lead by ID.

        See: https://docs.tomba.io/api/leads#retrieve-a-single-lead

        Args:
            lead_id: The ID of the lead to retrieve.

        Returns:
            dict: API response containing lead details.
        """

        if lead_id is None:
            raise TombaException('Missing required parameter: "lead_id"')

        params = {}
        path = "/leads/{lead_id}"
        path = path.replace("{lead_id}", str(lead_id))

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def create_lead(self, **params):
        """Create a new lead.

        See: https://docs.tomba.io/api/leads#create-a-lead

        Args:
            **params: Lead data (email, first_name, etc.).

        Returns:
            dict: API response containing the created lead.
        """

        path = "/leads"

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def update_lead(self, lead_id, **params):
        """Update a lead by ID.

        See: https://docs.tomba.io/api/leads#update-a-lead

        Args:
            lead_id: The ID of the lead to update.
            **params: Keyword arguments for the lead data to update.

        Returns:
            dict: API response containing the updated lead.
        """

        if lead_id is None:
            raise TombaException('Missing required parameter: "lead_id"')

        path = "/leads/{lead_id}"
        path = path.replace("{lead_id}", str(lead_id))

        return self.client.call(
            "put",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def delete_lead(self, lead_id):
        """Delete a lead by ID.

        See: https://docs.tomba.io/api/leads#delete-a-lead

        Args:
            lead_id: The ID of the lead to delete.

        Returns:
            dict: API response confirming deletion.
        """

        if lead_id is None:
            raise TombaException('Missing required parameter: "lead_id"')

        params = {}
        path = "/leads/{lead_id}"
        path = path.replace("{lead_id}", str(lead_id))

        return self.client.call(
            "delete",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
