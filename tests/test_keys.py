import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.keys import Keys


class TestKeys:
    def test_class_exists(self):
        assert Keys is not None

    def test_instantiation(self):
        client = Client()
        keys = Keys(client)
        assert keys is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_keys(self):
        client = make_client()
        keys = Keys(client)
        result = keys.get_keys()
        assert result is not None
