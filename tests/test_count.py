import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.count import Count


class TestCount:
    def test_class_exists(self):
        assert Count is not None

    def test_instantiation(self):
        client = Client()
        count = Count(client)
        assert count is not None

    def test_email_count_missing_param(self):
        client = Client()
        count = Count(client)
        with pytest.raises(TombaException):
            count.email_count(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_email_count(self):
        client = make_client()
        count = Count(client)
        result = count.email_count("tomba.io")
        assert result is not None
