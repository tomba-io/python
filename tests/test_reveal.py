import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.services.reveal import Reveal


class TestReveal:
    def test_class_exists(self):
        assert Reveal is not None

    def test_instantiation(self):
        client = Client()
        reveal = Reveal(client)
        assert reveal is not None

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_search_companies(self):
        client = make_client()
        reveal = Reveal(client)
        result = reveal.search_companies(ip="1.1.1.1")
        assert result is not None
