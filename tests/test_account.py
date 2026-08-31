import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.account import Account


class TestAccount:
    def test_class_exists(self):
        assert Account is not None

    def test_instantiation(self):
        client = Client()
        account = Account(client)
        assert account is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_account(self):
        client = make_client()
        account = Account(client)
        result = account.get_account()
        assert result is not None
