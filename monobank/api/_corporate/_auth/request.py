from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class RequestFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def create(self, params=None, data=None):
        """Initialize access request."""
        return self.client.post("personal/auth/request", params=params, data=data)

    def status(self, params=None):
        """Check access request status."""
        return self.client.get("personal/auth/request", params=params)
