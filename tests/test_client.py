from tomba.client import Client


class TestClient:
    def test_class_exists(self):
        assert Client is not None

    def test_default_endpoint(self):
        client = Client()
        assert client._endpoint == "https://api.tomba.io/v1"

    def test_set_endpoint(self):
        client = Client()
        result = client.set_endpoint("https://custom.api.com")
        assert client._endpoint == "https://custom.api.com"
        assert result is client

    def test_set_key(self):
        client = Client()
        result = client.set_key("ta_test123")
        assert client._global_headers["x-tomba-key"] == "ta_test123"
        assert result is client

    def test_set_secret(self):
        client = Client()
        result = client.set_secret("ts_test123")
        assert client._global_headers["x-tomba-secret"] == "ts_test123"
        assert result is client

    def test_set_timeout(self):
        client = Client()
        result = client.set_timeout(60)
        assert client._timeout == 60
        assert result is client

    def test_add_header(self):
        client = Client()
        result = client.add_header("X-Custom", "value")
        assert client._global_headers["x-custom"] == "value"
        assert result is client

    def test_chaining(self):
        client = Client()
        result = client.set_key("ta_test").set_secret("ts_test").set_timeout(60)
        assert result is client
        assert client._global_headers["x-tomba-key"] == "ta_test"
        assert client._global_headers["x-tomba-secret"] == "ts_test"
        assert client._timeout == 60

    def test_flatten_dict(self):
        client = Client()
        data = {"key1": "value1", "key2": "value2"}
        result = client.flatten(data)
        assert result == {"key1": "value1", "key2": "value2"}

    def test_flatten_empty(self):
        client = Client()
        result = client.flatten({})
        assert result == {}
