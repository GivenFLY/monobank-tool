from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class WebhookFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def set(self, params=None, data=None):
        """Set or update webhook."""
        return self.client.post("personal/corp/webhook", params=params, data=data)
