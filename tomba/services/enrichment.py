from ..exception import TombaException
from ..service import Service


class Enrichment(Service):
    def __init__(self, client):
        super().__init__(client)

    def person(self, email, webhook_url=None):
        """Get person data from an email address.

        See: https://docs.tomba.io/api/enrichment#person

        Args:
            email: The email address to look up.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing person data.
        """

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = "/people/find"

        if email is not None:
            params["email"] = email

        if webhook_url is not None:
            params["webhook_url"] = webhook_url

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def company(self, domain):
        """Get company data from a domain.

        See: https://docs.tomba.io/api/enrichment#company

        Args:
            domain: The domain name to look up (e.g., "example.com").

        Returns:
            dict: API response containing company data.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/companies/find"

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

    def combined(self, email):
        """Get combined person and company data from an email address.

        See: https://docs.tomba.io/api/enrichment#combined

        Args:
            email: The email address to look up.

        Returns:
            dict: API response containing person and company data.
        """

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = "/combined/find"

        if email is not None:
            params["email"] = email

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
