import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.leads import Leads


class TestLeads:
    def test_class_exists(self):
        assert Leads is not None

    def test_instantiation(self):
        client = Client()
        leads = Leads(client)
        assert leads is not None

    def test_get_lead_missing_param(self):
        client = Client()
        leads = Leads(client)
        with pytest.raises(TombaException):
            leads.get_lead(None)

    def test_update_lead_missing_param(self):
        client = Client()
        leads = Leads(client)
        with pytest.raises(TombaException):
            leads.update_lead(None)

    def test_delete_lead_missing_param(self):
        client = Client()
        leads = Leads(client)
        with pytest.raises(TombaException):
            leads.delete_lead(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_list_leads(self):
        client = make_client()
        leads = Leads(client)
        result = leads.list_leads()
        assert result is not None
