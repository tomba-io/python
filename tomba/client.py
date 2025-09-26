import io
import requests
from .exception import TombaException


class Client:
    def __init__(self):
        self._endpoint = 'https://api.tomba.io/v1'
        self._global_headers = {
            'content-type': '',
            'x-sdk-version': 'tomba:python:v1.0.5',
        }
        self._timeout = 30

    def set_endpoint(self, endpoint):
        self._endpoint = endpoint
        return self

    def add_header(self, key, value):
        self._global_headers[key.lower()] = value
        return self

    def set_key(self, value):
        """Your Key"""

        self._global_headers['x-tomba-key'] = value
        return self

    def set_secret(self, value):
        """Your Secret"""

        self._global_headers['x-tomba-secret'] = value
        return self

    def set_timeout(self, value):
        """Timeout in seconds"""

        self._timeout = value
        return self

    def call(self, method, path='', headers=None, params=None):
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        data = {}
        json = {}
        files = {}

        headers = {**self._global_headers, **headers}

        if method != 'get':
            data = params
            params = {}

        if headers['content-type'].startswith('application/json'):
            json = data
            data = {}

        if headers['content-type'].startswith('multipart/form-data'):
            del headers['content-type']

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
                timeout=self._timeout
            )

            response.raise_for_status()

            content_type = response.headers['Content-Type']

            if content_type.startswith('application/json'):
                return response.json()

            return response._content
        except Exception as e:
            if response != None:
                content_type = response.headers['Content-Type']
                if content_type.startswith('application/json'):
                    raise TombaException(
                        response.json()['errors']['message'], response.status_code, response.json())
                else:
                    raise TombaException(response.text, response.status_code)
            else:
                raise TombaException(e)

    def flatten(self, data, prefix=''):
        output = {}
        i = 0

        for key in data:
            value = data[key] if isinstance(data, dict) else key
            finalKey = prefix + '[' + key + ']' if prefix else key
            finalKey = prefix + \
                '[' + str(i) + ']' if isinstance(data, list) else finalKey
            i += 1

            if isinstance(value, list) or isinstance(value, dict):
                output = {**output, **self.flatten(value, finalKey)}
            else:
                output[finalKey] = value

        return output
