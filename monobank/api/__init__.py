from monobank.api._acquiring._merchant import MerchantFacade
from monobank._core.client.acquiring import AcquiringAPIClient
from monobank._core.client.personal import PersonalAPIClient
from monobank._core.client.corporate import CorporateAPIClient
from monobank._core import serializers
from monobank.api._personal import ClientFacade as PersonalClientFacade, BankFacade as PersonalBankFacade
from monobank.api._corporate import AuthFacade as CorporateAuthFacade
from monobank.api._corporate import CorpFacade as CorporateCorpFacade
from monobank.api._corporate import ClientFacade as CorporateClientFacade
from monobank.api._corporate import BankFacade as CorporateBankFacade

class AcquiringAPI:
    def __init__(self, api_key, response_serializer=serializers.get_json):
        self._api_key = api_key
        self._client = AcquiringAPIClient(token=self._api_key, response_serializer=response_serializer)
        self.merchant = MerchantFacade(client=self._client)

class PersonalAPI:
    def __init__(self, api_key, response_serializer=serializers.get_json):
        self._api_key = api_key
        self._client = PersonalAPIClient(token=self._api_key, response_serializer=response_serializer)
        self.client = PersonalClientFacade(client=self._client)
        self.bank = PersonalBankFacade(client=self._client)

class CorporateAPI:
    def __init__(self, key_id=None, token=None, response_serializer=serializers.get_json):
        self._client = CorporateAPIClient(key_id=key_id, token=token, response_serializer=response_serializer)
        self.auth = CorporateAuthFacade(client=self._client)
        self.corp = CorporateCorpFacade(client=self._client)
        self.client = CorporateClientFacade(client=self._client)
        self.bank = CorporateBankFacade(client=self._client)
