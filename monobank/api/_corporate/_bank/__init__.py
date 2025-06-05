from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

from .currency import CurrencyFacade

class BankFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client
        self.currency = CurrencyFacade(client)
