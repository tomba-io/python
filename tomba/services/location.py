from ..exception import TombaException
from ..service import Service


class Location(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_location(self, domain):
        """Get the location of a domain.

        See: https://docs.tomba.io/api/finder#location#location

        Args:
            domain: The domain name to get location for.

        Returns:
            dict: API response containing the domain location.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/location"

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
