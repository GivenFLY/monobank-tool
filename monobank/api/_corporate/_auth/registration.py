from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class RegistrationFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def create(self, params=None, data=None):
        """Create access application."""
        return self.client.post("personal/auth/registration", params=params, data=data)

    def status(self, params=None, data=None):
        """Check application status."""
        return self.client.post("personal/auth/registration/status", params=params, data=data)
