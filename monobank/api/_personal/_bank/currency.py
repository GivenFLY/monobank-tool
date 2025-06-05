from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.personal import PersonalAPIClient


class CurrencyFacade:
    def __init__(self, client: "PersonalAPIClient"):
        self.client = client

    def __call__(self, params=None, data=None):
        """Public currency rates."""
        return self.client.get("bank/currency", params=params, data=data)
