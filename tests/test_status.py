import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.status import Status


class TestStatus:
    def test_class_exists(self):
        assert Status is not None

    def test_instantiation(self):
        client = Client()
        status = Status(client)
        assert status is not None

    def test_domain_status_missing_param(self):
        client = Client()
        status = Status(client)
        with pytest.raises(TombaException):
            status.domain_status(None)

    def test_auto_complete_missing_param(self):
        client = Client()
        status = Status(client)
        with pytest.raises(TombaException):
            status.auto_complete(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_domain_status(self):
        client = make_client()
        status = Status(client)
        result = status.domain_status("tomba.io")
        assert result is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_auto_complete(self):
        client = make_client()
        status = Status(client)
        result = status.auto_complete("tomba")
        assert result is not None
