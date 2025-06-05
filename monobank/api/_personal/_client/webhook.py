from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.personal import PersonalAPIClient


class WebhookFacade:
    def __init__(self, client: "PersonalAPIClient"):
        self.client = client

    def set(self, data=None, params=None):
        """Set webhook URL."""
        return self.client.post("personal/webhook", params=params, data=data)

    def remove(self, params=None):
        """Remove webhook."""
        return self.client.delete("personal/webhook", params=params)
