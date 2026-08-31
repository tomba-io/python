from ..exception import TombaException
from ..service import Service


class Format(Service):
    def __init__(self, client):
        super().__init__(client)

    def email_format(self, domain):
        """Get the email format used by a domain.

        See: https://docs.tomba.io/api/finder#email-format#email-format

        Args:
            domain: The domain name to find the email format for.

        Returns:
            dict: API response containing the email format.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/email-format"

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
