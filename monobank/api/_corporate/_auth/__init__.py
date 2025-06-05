from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from monobank._core.client.corporate import CorporateAPIClient

from .registration import RegistrationFacade
from .request import RequestFacade

class AuthFacade:
    def __init__(self, client: "CorporateAPIClient"):
        self.client = client
        self.registration = RegistrationFacade(client)
        self.request = RequestFacade(client)
