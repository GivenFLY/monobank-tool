from monobank.api.acquiring.merchant.details import DetailsFacade
from monobank.api.acquiring.merchant.invoice import InvoiceFacade
from monobank.api.acquiring.merchant.pubkey import PubkeyFacade
from monobank.api.acquiring.merchant.qr import QRFacade
from monobank.api.acquiring.merchant.statement import StatementFacade
from monobank.api.acquiring.merchant.wallet import WalletFacade
from monobank.core.client.acquiring import AcquiringAPIClient


class MerchantFacade:
    def __init__(self, client: AcquiringAPIClient):
        self.client = client
        self.invoice = InvoiceFacade(client=client)
        self.details = DetailsFacade(client=client)
        self.pubkey = PubkeyFacade(client=client)
        self.qr = QRFacade(client=client)
        self.statement = StatementFacade(client=client)
        self.wallet = WalletFacade(client=client)
