from ..exception import TombaException
from ..service import Service


class Domain(Service):
    def __init__(self, client):
        super().__init__(client)

    def domain_search(
        self,
        domain,
        page=None,
        limit=None,
        department=None,
        country=None,
        enrich_mobile=None,
        webhook_url=None,
    ):
        """Search emails for a given domain.

        See: https://docs.tomba.io/api/finder#domain-search#domain-search

        Args:
            domain: The domain name to search (e.g., "example.com").
            page: The page number for pagination.
            limit: The number of results per page.
            department: Filter by department.
            country: Filter by country.
            enrich_mobile: Whether to enrich with mobile phone data.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing email addresses found for the domain.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        params = {}
        path = "/domain-search"

        if domain is not None:
            params["domain"] = domain

        if page is not None:
            params["page"] = page

        if limit is not None:
            params["limit"] = limit

        if department is not None:
            params["department"] = department

        if country is not None:
            params["country"] = country

        if enrich_mobile is not None:
            params["enrich_mobile"] = enrich_mobile

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
