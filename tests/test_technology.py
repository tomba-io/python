import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.technology import Technology


class TestTechnology:
    def test_class_exists(self):
        assert Technology is not None

    def test_instantiation(self):
        client = Client()
        technology = Technology(client)
        assert technology is not None

    def test_list_missing_param(self):
        client = Client()
        technology = Technology(client)
        with pytest.raises(TombaException):
            technology.list(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_list(self):
        client = make_client()
        technology = Technology(client)
        result = technology.list("tomba.io")
        assert result is not None
