from monobank._core.client.base import BaseAPIClient


class AcquiringAPIClient(BaseAPIClient):
    def __init__(self, token: str):
        super().__init__(base_url="https://api.monobank.ua/api/")
        self._token = token
        self.headers |= {'X-Token': self._token}
