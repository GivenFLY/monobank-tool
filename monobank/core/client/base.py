from urllib import request, parse
from urllib.parse import urljoin
import json


class BaseAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self._headers = {'Content-Type': 'application/json'}  # Default header

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    def _request(self, method, path, params=None, data=None):
        url = urljoin(self.base_url, path)

        if params:
            query_string = parse.urlencode(params)
            url += '?' + query_string

        if data:
            data_bytes = json.dumps(data).encode('utf-8')
        else:
            data_bytes = None

        req = request.Request(url, data=data_bytes, method=method)

        for key, value in self.headers.items():
            req.add_header(key, value)

        with request.urlopen(req) as response:
            return response

    def get(self, path, params=None, data=None):
        return self._request('GET', path, params=params, data=data)

    def post(self, path, params=None, data=None):
        return self._request('POST', path, params=params, data=data)

    def put(self, path, params=None, data=None):
        return self._request('PUT', path, params=params, data=data)

    def delete(self, path, params=None, data=None):
        return self._request('DELETE', path, params=params, data=data)
