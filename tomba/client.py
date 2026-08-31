import io

import requests

from .exception import TombaException


class Client:
    """Tomba API HTTP client.

    Handles authentication, request building, and response parsing
    for the Tomba REST API.

    See: https://docs.tomba.io/api/introduction
    """

    def __init__(self):
        self._endpoint = "https://api.tomba.io/v1"
        self._global_headers = {
            "content-type": "",
            "x-sdk-version": "tomba:python:v1.1.0",
        }
        self._timeout = 120

    def set_endpoint(self, endpoint):
        """Set the API endpoint URL.

        Args:
            endpoint: The base URL for the API.

        Returns:
            Client: The client instance for chaining.
        """

        self._endpoint = endpoint
        return self

    def add_header(self, key, value):
        """Add a custom header to all requests.

        Args:
            key: The header name.
            value: The header value.

        Returns:
            Client: The client instance for chaining.
        """

        self._global_headers[key.lower()] = value
        return self

    def set_key(self, value):
        """Set the API key for authentication.

        Args:
            value: Your Tomba API key (starts with "ta_").

        Returns:
            Client: The client instance for chaining.
        """

        self._global_headers["x-tomba-key"] = value
        return self

    def set_secret(self, value):
        """Set the API secret for authentication.

        Args:
            value: Your Tomba API secret (starts with "ts_").

        Returns:
            Client: The client instance for chaining.
        """

        self._global_headers["x-tomba-secret"] = value
        return self

    def set_timeout(self, value):
        """Set the request timeout.

        Args:
            value: Timeout in seconds.

        Returns:
            Client: The client instance for chaining.
        """

        self._timeout = value
        return self

    def call(self, method, path="", headers=None, params=None):
        """Make an HTTP request to the Tomba API.

        Handles GET, POST, PUT, and DELETE methods. For GET requests,
        params are sent as query parameters. For POST/PUT requests,
        params are sent as a JSON body. DELETE requests send no body.

        Args:
            method: HTTP method (get, post, put, delete).
            path: API endpoint path.
            headers: Additional headers for this request.
            params: Request parameters (query params for GET, JSON body for POST/PUT).

        Returns:
            dict: Parsed JSON response from the API.

        Raises:
            TombaException: If the API returns an error response.
        """

        if headers is None:
            headers = {}

        if params is None:
            params = {}

        data = {}
        json = {}
        files = {}

        headers = {**self._global_headers, **headers}

        if method != "get":
            data = params
            params = {}

        if headers["content-type"].startswith("application/json"):
            json = data
            data = {}

        if headers["content-type"].startswith("multipart/form-data"):
            del headers["content-type"]

            for key in data.copy():
                if isinstance(data[key], io.BufferedIOBase):
                    files[key] = data[key]
                    del data[key]
        response = None
        try:
            response = requests.request(
                method=method,
                url=self._endpoint + path,
                params=self.flatten(params),
                data=self.flatten(data),
                json=json,
                files=files,
                headers=headers,
                timeout=self._timeout,
            )

            response.raise_for_status()

            rate_limit = {
                "second_limit": int(response.headers.get("x-second-rate-limit", 0)) or None,
                "minute_limit": int(response.headers.get("x-minute-rate-limit", 0)) or None,
                "daily_limit": int(response.headers.get("x-daily-rate-limit", 0)) or None,
                "minute_remaining": int(response.headers.get("x-minute-request-left", 0)) or None,
                "daily_remaining": int(response.headers.get("x-daily-request-left", 0)) or None,
                "minute_reset": int(response.headers.get("x-minute-reset-seconds", 0)) or None,
                "daily_reset": int(response.headers.get("x-daily-reset-seconds", 0)) or None,
                "retry_after": int(response.headers.get("retry-after", 0)) or None,
                "policy": response.headers.get("ratelimit-policy") or None,
                "rate_limit": response.headers.get("ratelimit") or None,
            }

            content_type = response.headers["Content-Type"]

            if content_type.startswith("application/json"):
                return {"data": response.json(), "rate_limit": rate_limit}

            return {"data": response._content, "rate_limit": rate_limit}
        except Exception as e:
            if response is not None:
                content_type = response.headers["Content-Type"]
                if content_type.startswith("application/json"):
                    raise TombaException(
                        response.json()["errors"]["message"], response.status_code, response.json()
                    ) from e
                else:
                    raise TombaException(response.text, response.status_code) from e
            else:
                raise TombaException(e) from e

    def flatten(self, data, prefix=""):
        """Flatten nested dictionaries and lists for form encoding.

        Args:
            data: The data to flatten (dict or list).
            prefix: Key prefix for nested values.

        Returns:
            dict: Flattened key-value pairs.
        """

        output = {}

        for i, key in enumerate(data):
            value = data[key] if isinstance(data, dict) else key
            finalKey = prefix + "[" + key + "]" if prefix else key
            finalKey = prefix + "[" + str(i) + "]" if isinstance(data, list) else finalKey

            if isinstance(value, (list, dict)):
                output = {**output, **self.flatten(value, finalKey)}
            else:
                output[finalKey] = value

        return output
