from ..service import Service


class Usage(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_usage(self):
        """Get your account usage statistics.

        See: https://docs.tomba.io/api/account#retrieve-api-usage#get-usage

        Returns:
            dict: API response containing usage statistics.
        """

        params = {}
        path = "/usage"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
