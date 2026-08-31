import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.leads_attributes import LeadsAttributes


class TestLeadsAttributes:
    def test_class_exists(self):
        assert LeadsAttributes is not None

    def test_instantiation(self):
        client = Client()
        leads_attributes = LeadsAttributes(client)
        assert leads_attributes is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_lead_attributes(self):
        client = make_client()
        leads_attributes = LeadsAttributes(client)
        result = leads_attributes.get_lead_attributes()
        assert result is not None
