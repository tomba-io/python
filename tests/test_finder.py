import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.finder import Finder


class TestFinder:
    def test_class_exists(self):
        assert Finder is not None

    def test_instantiation(self):
        client = Client()
        finder = Finder(client)
        assert finder is not None

    def test_email_finder_missing_domain(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.email_finder(None, "John", "Doe")

    def test_email_finder_missing_first_name(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.email_finder("example.com", None, "Doe")

    def test_email_finder_missing_last_name(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.email_finder("example.com", "John", None)

    def test_author_finder_missing_param(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.author_finder(None)

    def test_enrichment_missing_param(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.enrichment(None)

    def test_linkedin_finder_missing_param(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.linkedin_finder(None)

    def test_format_missing_param(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.format(None)

    def test_location_missing_param(self):
        client = Client()
        finder = Finder(client)
        with pytest.raises(TombaException):
            finder.location(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_email_finder(self):
        client = make_client()
        finder = Finder(client)
        result = finder.email_finder("tomba.io", "Mohamed", "Ben Rebia")
        assert result is not None
