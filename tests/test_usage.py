import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.usage import Usage


class TestUsage:
    def test_class_exists(self):
        assert Usage is not None

    def test_instantiation(self):
        client = Client()
        usage = Usage(client)
        assert usage is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_usage(self):
        client = make_client()
        usage = Usage(client)
        result = usage.get_usage()
        assert result is not None
