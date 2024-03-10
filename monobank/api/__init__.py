from monobank.api.acquiring.merchant import MerchantFacade
from monobank.core.client.acquiring import AcquiringAPIClient


class AcquiringAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = AcquiringAPIClient(token=self.api_key)
        self.merchant = MerchantFacade(client=self.client)
