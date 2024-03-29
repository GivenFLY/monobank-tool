from monobank.core.client.acquiring import AcquiringAPIClient


class StatementFacade:
    def __init__(self, client: AcquiringAPIClient):
        self.client = client

    def __call__(self, params=None, data=None):
        """
        Виписка за період

        :param params: параметри запиту
        :param data: дані запиту
        :return: urllib.response
        """
        return self.client.get("merchant/statement", params=params, data=data)
