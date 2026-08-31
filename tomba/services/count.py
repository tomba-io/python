from ..exception import TombaException
from ..service import Service


class Count(Service):
    def __init__(self, client):
        super().__init__(client)

    def email_count(self, domain):
        """Get the number of email addresses found for a domain.

        See: https://docs.tomba.io/api/finder#email-count#email-count

        Args:
            domain: The domain name to count emails for (e.g., "example.com").

        Returns:
            dict: API response containing the email count.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/email-count"

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
