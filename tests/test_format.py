import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.format import Format


class TestFormat:
    def test_class_exists(self):
        assert Format is not None

    def test_instantiation(self):
        client = Client()
        fmt = Format(client)
        assert fmt is not None

    def test_email_format_missing_param(self):
        client = Client()
        fmt = Format(client)
        with pytest.raises(TombaException):
            fmt.email_format(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_email_format(self):
        client = make_client()
        fmt = Format(client)
        result = fmt.email_format("tomba.io")
        assert result is not None
