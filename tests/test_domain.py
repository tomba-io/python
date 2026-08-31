import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.domain import Domain


class TestDomain:
    def test_class_exists(self):
        assert Domain is not None

    def test_instantiation(self):
        client = Client()
        domain = Domain(client)
        assert domain is not None

    def test_domain_search_missing_param(self):
        client = Client()
        domain = Domain(client)
        with pytest.raises(TombaException):
            domain.domain_search(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_domain_search(self):
        client = make_client()
        domain = Domain(client)
        result = domain.domain_search("tomba.io")
        assert result is not None
