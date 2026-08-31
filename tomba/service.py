from .client import Client


class Service:
    """Base class for all Tomba API service classes.

    Args:
        client: An instance of the Tomba Client.
    """

    def __init__(self, client: Client):
        self.client = client
