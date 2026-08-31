from ..exception import TombaException
from ..service import Service


class Technology(Service):
    def __init__(self, client):
        super().__init__(client)

    def list(self, domain):
        """Retrieve the technologies used by a specific domain.

        See: https://docs.tomba.io/api/domain#technology#technology

        Args:
            domain: The domain name to find technologies for.

        Returns:
            dict: API response containing technologies used by the domain.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/technology"

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
