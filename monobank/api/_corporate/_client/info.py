from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class InfoFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def __call__(self, params=None):
        """Return information about client and accounts."""
        return self.client.get("personal/client-info", params=params)
