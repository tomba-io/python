from ..exception import TombaException
from ..service import Service

VALID_BULK_TYPES = [
    "search",
    "similar",
    "company",
    "finder",
    "enrich",
    "linkedin",
    "author",
    "verifier",
    "phone-finder",
    "phone-validator",
]


class Bulk(Service):
    def __init__(self, client):
        super().__init__(client)

    def _validate_bulk_type(self, bulk_type):
        """Validate the bulk type parameter.

        Args:
            bulk_type: The type of bulk operation.

        Raises:
            TombaException: If the bulk type is invalid.
        """

        if bulk_type is None:
            raise TombaException('Missing required parameter: "bulk_type"')

        if bulk_type not in VALID_BULK_TYPES:
            raise TombaException(
                f'Invalid bulk_type: "{bulk_type}". '
                f'Must be one of: {", ".join(VALID_BULK_TYPES)}'
            )

    def list_bulks(self, bulk_type, page=None, limit=None):
        """List all bulk operations of a given type.

        See: https://docs.tomba.io/api/bulks

        Args:
            bulk_type: The type of bulk operation (e.g., "search", "finder").
            page: The page number for pagination.
            limit: The number of results per page.

        Returns:
            dict: API response containing bulk operations.
        """

        self._validate_bulk_type(bulk_type)

        params = {}
        path = f"/bulk/{bulk_type}"

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

    def get_bulk(self, bulk_type, bulk_id):
        """Get a specific bulk operation by type and ID.

        See: https://docs.tomba.io/api/bulk#get-bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation.

        Returns:
            dict: API response containing bulk operation details.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        params = {}
        path = f"/bulk/{bulk_type}/{bulk_id}"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def create_bulk(self, bulk_type, **params):
        """Create a new bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            **params: Keyword arguments for the bulk operation data.

        Returns:
            dict: API response containing the created bulk operation.
        """

        self._validate_bulk_type(bulk_type)

        path = f"/bulk/{bulk_type}"

        return self.client.call(
            "post",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def launch_bulk(self, bulk_type, bulk_id):
        """Launch a bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation to launch.

        Returns:
            dict: API response confirming the launch.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        params = {}
        path = f"/bulk/{bulk_type}/{bulk_id}"

        return self.client.call(
            "put",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def delete_bulk(self, bulk_type, bulk_id):
        """Delete a bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation to delete.

        Returns:
            dict: API response confirming deletion.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        params = {}
        path = f"/bulk/{bulk_type}/{bulk_id}/delete"

        return self.client.call(
            "delete",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def archive_bulk(self, bulk_type, bulk_id):
        """Archive a bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation to archive.

        Returns:
            dict: API response confirming the archive.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        params = {}
        path = f"/bulk/{bulk_type}/{bulk_id}/archive"

        return self.client.call(
            "delete",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def rename_bulk(self, bulk_type, bulk_id, name):
        """Rename a bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation to rename.
            name: The new name for the bulk operation.

        Returns:
            dict: API response confirming the rename.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        if name is None:
            raise TombaException('Missing required parameter: "name"')

        params = {"name": name}
        path = f"/bulk/{bulk_type}/{bulk_id}/rename"

        return self.client.call(
            "put",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def bulk_progress(self, bulk_type, bulk_id):
        """Get the progress of a bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation.

        Returns:
            dict: API response containing progress information.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        params = {}
        path = f"/bulk/{bulk_type}/{bulk_id}/progress"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )

    def download_bulk(self, bulk_type, bulk_id):
        """Download the results of a bulk operation.

        See: https://docs.tomba.io/api/bulk

        Args:
            bulk_type: The type of bulk operation.
            bulk_id: The ID of the bulk operation to download.

        Returns:
            dict: API response containing the download URL or data.
        """

        self._validate_bulk_type(bulk_type)

        if bulk_id is None:
            raise TombaException('Missing required parameter: "bulk_id"')

        params = {}
        path = f"/bulk/{bulk_type}/{bulk_id}/download"

        return self.client.call(
            "get",
            path,
            {
                "content-type": "application/json",
            },
            params,
        )
