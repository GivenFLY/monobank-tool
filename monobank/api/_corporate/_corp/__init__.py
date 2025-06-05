from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

from .webhook import WebhookFacade
from .settings import SettingsFacade

class CorpFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client
        self.webhook = WebhookFacade(client)
        self.settings = SettingsFacade(client)
