import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.phone import Phone


class TestPhone:
    def test_class_exists(self):
        assert Phone is not None

    def test_instantiation(self):
        client = Client()
        phone = Phone(client)
        assert phone is not None

    def test_finder_missing_param(self):
        client = Client()
        phone = Phone(client)
        with pytest.raises(TombaException):
            phone.finder(None)

    def test_validator_missing_param(self):
        client = Client()
        phone = Phone(client)
        with pytest.raises(TombaException):
            phone.validator(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_finder(self):
        client = make_client()
        phone = Phone(client)
        result = phone.finder("b.mohamed@tomba.io")
        assert result is not None
