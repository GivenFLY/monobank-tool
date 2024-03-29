from monobank.core.client.acquiring import AcquiringAPIClient


class DetailsFacade:
    def __init__(self, client: AcquiringAPIClient):
        self.client = client

    def __call__(self, params=None, data=None):
        """
        Дані мерчанта

        :return: urllib.response
        """
        return self.client.get("merchant/details", params=params, data=data)
