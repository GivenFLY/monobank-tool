from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

class StatementFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client

    def __call__(self, account: str, from_time: int, to_time: int | None = None, params=None):
        """Return account statement."""
        path = f"personal/statement/{account}/{from_time}"
        if to_time is not None:
            path += f"/{to_time}"
        return self.client.get(path, params=params)
