from ..exception import TombaException
from ..service import Service


class Similar(Service):
    def __init__(self, client):
        super().__init__(client)

    def websites(self, domain):
        """Retrieve similar domains based on a specific domain.

        See: https://docs.tomba.io/api/similar#similar-websites

        Args:
            domain: The domain name to find similar websites for.

        Returns:
            dict: API response containing similar domains.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/similar"

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
