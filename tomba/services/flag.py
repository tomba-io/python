from ..exception import TombaException
from ..service import Service


class Flag(Service):
    def __init__(self, client):
        super().__init__(client)

    def list_flags(self, page=None, limit=None):
        """Get all flagged email addresses.

        See: https://docs.tomba.io/api/flag#list-flags

        Args:
            page: The page number for pagination.
            limit: The number of results per page.

        Returns:
            dict: API response containing flagged emails.
        """

        params = {}
        path = "/flag"

        if page is not None:
            params["page"] = page

        if limit is not None:
            params["limit"] = limit

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def create_flag(self, email, reason=None):
        """Flag an email address.

        See: https://docs.tomba.io/api/flag#create-flag

        Args:
            email: The email address to flag.
            reason: Optional reason for flagging the email.

        Returns:
            dict: API response confirming the flag creation.
        """

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = "/flag"

        params["email"] = email

        if reason is not None:
            params["reason"] = reason

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
