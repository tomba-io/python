from ..service import Service


class Account(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_account(self):
        """Get information about the current account.

        See: https://docs.tomba.io/api/account#get-account

        Returns:
            dict: API response containing account details.
        """

        params = {}
        path = "/me"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
