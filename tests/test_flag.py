import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.flag import Flag


class TestFlag:
    def test_class_exists(self):
        assert Flag is not None

    def test_instantiation(self):
        client = Client()
        flag = Flag(client)
        assert flag is not None

    def test_create_flag_missing_param(self):
        client = Client()
        flag = Flag(client)
        with pytest.raises(TombaException):
            flag.create_flag(None, "test@example.com", "spam")

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_list_flags(self):
        client = make_client()
        flag = Flag(client)
        result = flag.list_flags()
        assert result is not None
