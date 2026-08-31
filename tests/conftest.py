import os

from tomba.client import Client

has_credentials = bool(os.environ.get("TOMBA_API_KEY") and os.environ.get("TOMBA_SECRET_KEY"))


def make_client():
    """Create and configure a Tomba API client using environment variables."""

    client = Client()
    client.set_key(os.environ.get("TOMBA_API_KEY", ""))
    client.set_secret(os.environ.get("TOMBA_SECRET_KEY", ""))
    return client
