from monobank._core.client.base import BaseAPIClient
from monobank._core import serializers

class CorporateAPIClient(BaseAPIClient):
    def __init__(self, key_id: str | None = None, token: str | None = None, response_serializer=serializers.get_json):
        super().__init__(base_url="https://api.monobank.ua/", response_serializer=response_serializer)
        if key_id:
            self.headers |= {"X-Key-Id": key_id}
        if token:
            self.headers |= {"X-Token": token}
