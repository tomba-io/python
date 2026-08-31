import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.enrichment import Enrichment


class TestEnrichment:
    def test_class_exists(self):
        assert Enrichment is not None

    def test_instantiation(self):
        client = Client()
        enrichment = Enrichment(client)
        assert enrichment is not None

    def test_person_missing_param(self):
        client = Client()
        enrichment = Enrichment(client)
        with pytest.raises(TombaException):
            enrichment.person(None)

    def test_company_missing_param(self):
        client = Client()
        enrichment = Enrichment(client)
        with pytest.raises(TombaException):
            enrichment.company(None)

    def test_combined_missing_param(self):
        client = Client()
        enrichment = Enrichment(client)
        with pytest.raises(TombaException):
            enrichment.combined(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_person(self):
        client = make_client()
        enrichment = Enrichment(client)
        result = enrichment.person("b.mohamed@tomba.io")
        assert result is not None
