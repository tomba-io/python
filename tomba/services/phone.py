from ..exception import TombaException
from ..service import Service


class Phone(Service):
    def __init__(self, client):
        super().__init__(client)

    def finder(self, email=None, domain=None, linkedin=None, full=None, webhook_url=None):
        """Find a phone number for an email, domain, or LinkedIn URL.

        See: https://docs.tomba.io/api/phone#phone-finder

        Args:
            email: The email address to find a phone number for.
            domain: The domain name to search.
            linkedin: The LinkedIn URL to search.
            full: Set to True to get all results.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing the phone number.
        """

        if email is None and domain is None and linkedin is None:
            raise TombaException('At least one of "email", "domain", or "linkedin" is required')

        params = {}
        path = "/phone-finder"
        if email is not None:
            params["email"] = email
        if domain is not None:
            params["domain"] = domain
        if linkedin is not None:
            params["linkedin"] = linkedin
        if full is not None:
            params["full"] = full
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

    def validator(self, phone):
        """Validate a phone number.

        See: https://docs.tomba.io/api/phone#phone-validator

        Args:
            phone: The phone number to validate.

        Returns:
            dict: API response containing validation results.
        """

        if phone is None:
            raise TombaException('Missing required parameter: "phone"')

        params = {}
        path = "/phone-validator"

        if phone is not None:
            params["phone"] = phone

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
