from ..service import Service


class Logs(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_logs(self, page=None, limit=None):
        """Get your account logs.

        See: https://docs.tomba.io/api/account#retrieve-api-logs#get-logs

        Args:
            page: The page number for pagination.
            limit: The number of results per page.

        Returns:
            dict: API response containing account logs.
        """

        params = {}
        path = "/logs"

        if page is not None:
            params["page"] = page

        if limit is not None:
            params["limit"] = limit

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
