from monobank.core.client.acquiring import AcquiringAPIClient


class SubmerchantFacade:
    def __init__(self, client: AcquiringAPIClient):
        self.client = client

    def list(self, params=None, data=None):
        """
        Дане апі потрібне обмеженому колу осіб, яким при створенні рахунку треба явно вказувати термінал

        :param params: параметри запиту
        :param data: дані запиту
        :return: urllib.response
        """
        return self.client.get("merchant/submerchant/list", params=params, data=data)
