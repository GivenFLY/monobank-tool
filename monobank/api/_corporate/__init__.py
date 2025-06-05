from monobank._core.client.corporate import CorporateAPIClient
from monobank._core import serializers
from ._bank import BankFacade
from ._auth import AuthFacade
from ._client import ClientFacade
from ._corp import CorpFacade

class CorporateAPI:
    def __init__(self, key_id=None, token=None, response_serializer=serializers.get_json):
        self._client = CorporateAPIClient(key_id=key_id, token=token, response_serializer=response_serializer)
        self.bank = BankFacade(client=self._client)
        self.auth = AuthFacade(client=self._client)
        self.client = ClientFacade(client=self._client)
        self.corp = CorpFacade(client=self._client)
