from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.personal import PersonalAPIClient

from .info import InfoFacade
from .statement import StatementFacade
from .webhook import WebhookFacade


class ClientFacade:
    def __init__(self, client: "PersonalAPIClient"):
        self.client = client
        self.info = InfoFacade(client)
        self.statement = StatementFacade(client)
        self.webhook = WebhookFacade(client)
