from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class SettingsFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def __call__(self, params=None):
        """Get company settings."""
        return self.client.get("personal/corp/settings", params=params)
