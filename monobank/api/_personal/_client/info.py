from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.personal import PersonalAPIClient


class InfoFacade:
    def __init__(self, client: "PersonalAPIClient"):
        self.client = client

    def __call__(self, params=None, data=None):
        """Return information about client and list of accounts."""
        return self.client.get("personal/client-info", params=params, data=data)
