import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.leads_lists import LeadsLists


class TestLeadsLists:
    def test_class_exists(self):
        assert LeadsLists is not None

    def test_instantiation(self):
        client = Client()
        leads_lists = LeadsLists(client)
        assert leads_lists is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_get_lists(self):
        client = make_client()
        leads_lists = LeadsLists(client)
        result = leads_lists.get_lists()
        assert result is not None
