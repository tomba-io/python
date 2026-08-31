from ..exception import TombaException
from ..service import Service


class Finder(Service):
    def __init__(self, client):
        super().__init__(client)

    def email_finder(self, domain, first_name, last_name, webhook_url=None):
        """Find the email address of a person using their name and domain.

        See: https://docs.tomba.io/api/finder#email-finder#email-finder

        Args:
            domain: The domain name of the company (e.g., "example.com").
            first_name: The first name of the person.
            last_name: The last name of the person.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing the found email address.
        """

        if domain is None:
            raise TombaException('Missing required parameter: "domain"')

        if first_name is None:
            raise TombaException('Missing required parameter: "first_name"')

        if last_name is None:
            raise TombaException('Missing required parameter: "last_name"')

        params = {}
        path = "/email-finder"

        if domain is not None:
            params["domain"] = domain

        if first_name is not None:
            params["first_name"] = first_name

        if last_name is not None:
            params["last_name"] = last_name

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

    def author_finder(self, url, webhook_url=None):
        """Find the email address of the author of an article.

        See: https://docs.tomba.io/api/author-finder#author-finder

        Args:
            url: The URL of the article.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing the author's email address.
        """

        if url is None:
            raise TombaException('Missing required parameter: "url"')

        params = {}
        path = "/author-finder"

        if url is not None:
            params["url"] = url

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

    def enrichment(self, email, webhook_url=None):
        """Enrich data for an email address.

        See: https://docs.tomba.io/api/enrichment#enrichment

        Args:
            email: The email address to enrich.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing enriched data.
        """

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = "/enrich"

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

    def linkedin_finder(self, url):
        """Find the email address associated with a LinkedIn profile.

        See: https://docs.tomba.io/api/linkedin-finder#linkedin-finder

        Args:
            url: The LinkedIn profile URL.

        Returns:
            dict: API response containing the email address.
        """

        if url is None:
            raise TombaException('Missing required parameter: "url"')

        params = {}
        path = "/linkedin"

        if url is not None:
            params["url"] = url

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def format(self, domain):
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

    def location(self, domain):
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
