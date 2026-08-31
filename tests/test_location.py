import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.location import Location


class TestLocation:
    def test_class_exists(self):
        assert Location is not None

    def test_instantiation(self):
        client = Client()
        location = Location(client)
        assert location is not None

    def test_get_location_missing_param(self):
        client = Client()
        location = Location(client)
        with pytest.raises(TombaException):
            location.get_location(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_location(self):
        client = make_client()
        location = Location(client)
        result = location.get_location("tomba.io")
        assert result is not None
