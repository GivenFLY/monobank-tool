from monobank.api.acquiring.merchant.invoice import InvoiceFacade
from monobank.core.client.acquiring import AcquiringAPIClient


class MerchantFacade:
    def __init__(self, client: AcquiringAPIClient):
        self.client = client
        self.invoice = InvoiceFacade(client=client)
