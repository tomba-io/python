from ..exception import TombaException
from ..service import Service


class Status(Service):
    def __init__(self, client):
        super().__init__(client)

    def domain_status(self, domain):
        """Get the status of a domain (webmail, disposable, etc.).

        See: https://docs.tomba.io/api/domain#domain-status#domain-status

        Args:
            domain: The domain name to check status for.

        Returns:
            dict: API response containing domain status information.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/domain-status"

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

    def auto_complete(self, query):
        """Get company autocomplete suggestions.

        See: https://docs.tomba.io/api/domain#domain-status#company-autocomplete

        Args:
            query: The search query for autocomplete suggestions.

        Returns:
            dict: API response containing domain suggestions.
        """

        if query is None:
            raise TombaException('Missing required parameter: "query"')

        params = {}
        path = "/domain-suggestions"

        if query is not None:
            params["query"] = query

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
