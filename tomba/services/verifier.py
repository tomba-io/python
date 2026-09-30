from ..exception import TombaException
from ..service import Service


class Verifier(Service):
    def __init__(self, client):
        super().__init__(client)

    def email_verifier(self, email, enrich_mobile=None, webhook_url=None):
        """Verify the deliverability of an email address.

        See: https://docs.tomba.io/api/verifier#email-verifier

        Args:
            email: The email address to verify.
            enrich_mobile: True to get the phone number too.
            webhook_url: Webhook URL for async notifications.

        Returns:
            dict: API response containing verification results.
        """

        if email is None:
            raise TombaException('Missing required parameter: "email"')

        params = {}
        path = "/email-verifier"

        if email is not None:
            params["email"] = email
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
