from ..service import Service


class Reveal(Service):
    def __init__(self, client):
        super().__init__(client)

    def search_companies(self, **params):
        """Search companies using reverse lookup.

        See: https://docs.tomba.io/api/reveal#companies-search

        Args:
            **params: Keyword arguments for the search (e.g., ip, page, limit).

        Returns:
            dict: API response containing matching companies.
        """

        return self.client.call(
            "post",
            "/reveal/search",
            {
                "content-type": "application/json",
            },
            params,
        )
