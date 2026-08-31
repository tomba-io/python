import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.logs import Logs


class TestLogs:
    def test_class_exists(self):
        assert Logs is not None

    def test_instantiation(self):
        client = Client()
        logs = Logs(client)
        assert logs is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_logs(self):
        client = make_client()
        logs = Logs(client)
        result = logs.get_logs()
        assert result is not None
