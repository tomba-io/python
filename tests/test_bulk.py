import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.bulk import VALID_BULK_TYPES, Bulk


class TestBulk:
    def test_class_exists(self):
        assert Bulk is not None

    def test_instantiation(self):
        client = Client()
        bulk = Bulk(client)
        assert bulk is not None

    def test_valid_bulk_types(self):
        assert "search" in VALID_BULK_TYPES
        assert "finder" in VALID_BULK_TYPES
        assert "verifier" in VALID_BULK_TYPES

    def test_list_bulks_invalid_type(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.list_bulks("invalid-type")

    def test_list_bulks_missing_type(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.list_bulks(None)

    def test_get_bulk_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.get_bulk("search", None)

    def test_launch_bulk_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.launch_bulk("search", None)

    def test_delete_bulk_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.delete_bulk("search", None)

    def test_archive_bulk_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.archive_bulk("search", None)

    def test_rename_bulk_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.rename_bulk("search", None, "new-name")

    def test_rename_bulk_missing_name(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.rename_bulk("search", "123", None)

    def test_bulk_progress_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.bulk_progress("search", None)

    def test_download_bulk_missing_id(self):
        client = Client()
        bulk = Bulk(client)
        with pytest.raises(TombaException):
            bulk.download_bulk("search", None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_list_bulks(self):
        client = make_client()
        bulk = Bulk(client)
        result = bulk.list_bulks("search")
        assert result is not None
