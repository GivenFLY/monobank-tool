from monobank._core.client.personal import PersonalAPIClient
from monobank._core import serializers
from ._client import ClientFacade
from ._bank import BankFacade


class PersonalAPI:
    def __init__(self, api_key, response_serializer=serializers.get_json):
        self._api_key = api_key
        self._client = PersonalAPIClient(token=self._api_key, response_serializer=response_serializer)
        self.client = ClientFacade(client=self._client)
        self.bank = BankFacade(client=self._client)
