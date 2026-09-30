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

    def create_flag(self, flag_type, value, reason, comment=None):
        """Flag an email address.

        See: https://docs.tomba.io/api/flag#create-flag

        Args:
            flag_type: The type of flag (e.g. "email", "domain").
            value: The value to flag (e.g. an email address or domain).
            reason: The reason for flagging.
            comment: Optional comment for additional context.

        Returns:
            dict: API response confirming the flag creation.
        """

        if flag_type is None:
            raise TombaException('Missing required parameter: "flag_type"')

        if value is None:
            raise TombaException('Missing required parameter: "value"')

        if reason is None:
            raise TombaException('Missing required parameter: "reason"')

        params = {}
        path = "/flag"

        params["flag_type"] = flag_type
        params["value"] = value
        params["reason"] = reason

        if comment is not None:
            params["comment"] = comment

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
