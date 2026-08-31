import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.similar import Similar


class TestSimilar:
    def test_class_exists(self):
        assert Similar is not None

    def test_instantiation(self):
        client = Client()
        similar = Similar(client)
        assert similar is not None

    def test_websites_missing_param(self):
        client = Client()
        similar = Similar(client)
        with pytest.raises(TombaException):
            similar.websites(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_websites(self):
        client = make_client()
        similar = Similar(client)
        result = similar.websites("tomba.io")
        assert result is not None
