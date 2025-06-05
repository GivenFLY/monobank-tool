from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.personal import PersonalAPIClient

from .currency import CurrencyFacade


class BankFacade:
    def __init__(self, client: "PersonalAPIClient"):
        self.client = client
        self.currency = CurrencyFacade(client)
