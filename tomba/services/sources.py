from ..exception import TombaException
from ..service import Service


class Sources(Service):
    def __init__(self, client):
        super().__init__(client)

    def email_sources(self, email):
        """Get the sources where an email address was found on the web.

        See: https://docs.tomba.io/api/email#email-sources#email-sources

        Args:
            email: The email address to find sources for.

        Returns:
            dict: API response containing the email sources.
        """

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = "/email-sources"

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
