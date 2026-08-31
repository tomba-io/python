import pytest

from tests.conftest import has_credentials, make_client
from tomba.client import Client
from tomba.exception import TombaException
from tomba.services.verifier import Verifier


class TestVerifier:
    def test_class_exists(self):
        assert Verifier is not None

    def test_instantiation(self):
        client = Client()
        verifier = Verifier(client)
        assert verifier is not None

    def test_email_verifier_missing_param(self):
        client = Client()
        verifier = Verifier(client)
        with pytest.raises(TombaException):
            verifier.email_verifier(None)

    @pytest.mark.skipif(not has_credentials, reason="No API credentials")
    def test_email_verifier(self):
        client = make_client()
        verifier = Verifier(client)
        result = verifier.email_verifier("b.mohamed@tomba.io")
        assert result is not None
