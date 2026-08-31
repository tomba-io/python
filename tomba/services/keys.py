from ..exception import TombaException
from ..service import Service


class Keys(Service):
    def __init__(self, client):
        super().__init__(client)

    def get_keys(self):
        """Get all API keys.

        See: https://docs.tomba.io/api/keys#get-keys

        Returns:
            dict: API response containing API keys.
        """

        params = {}
        path = "/keys"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def get_key(self, id):
        """Get a specific API key by ID.

        See: https://docs.tomba.io/api/keys#get-key

        Args:
            id: The ID of the API key.

        Returns:
            dict: API response containing the key details.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        path = "/keys/{id}".replace("{id}", id)

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            {},
        )

    def delete_key(self, id):
        """Delete an API key by ID.

        See: https://docs.tomba.io/api/keys#delete-an-api-key

        Args:
            id: The ID of the API key to delete.

        Returns:
            dict: API response confirming deletion.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = "/keys/{id}"
        path = path.replace("{id}", id)

        return self.client.call(
            "delete",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def create_key(self, **params):
        """Create a new API key.

        See: https://docs.tomba.io/api/keys#create-an-api-key

        Args:
            **params: Keyword arguments for the key data.

        Returns:
            dict: API response containing the created key.
        """

        path = "/keys"

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def reset_key(self, id):
        """Reset an API key by ID.

        See: https://docs.tomba.io/api/keys#reset-an-api-key

        Args:
            id: The ID of the API key to reset.

        Returns:
            dict: API response containing the reset key.
        """

        if id is None:
            raise TombaException('Missing required parameter: "id"')

        params = {}
        path = "/keys/{id}"
        path = path.replace("{id}", id)

        return self.client.call(
            "put",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
