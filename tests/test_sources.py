import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.sources import Sources


class TestSources:
    def test_class_exists(self):
        assert Sources is not None

    def test_instantiation(self):
        client = Client()
        sources = Sources(client)
        assert sources is not None

    def test_email_sources_missing_param(self):
        client = Client()
        sources = Sources(client)
        with pytest.raises(TombaException):
            sources.email_sources(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_email_sources(self):
        client = make_client()
        sources = Sources(client)
        result = sources.email_sources("b.mohamed@tomba.io")
        assert result is not None
