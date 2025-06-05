from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class CurrencyFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def __call__(self, params=None, data=None):
        """Public currency rates."""
        return self.client.get("bank/currency", params=params, data=data)
