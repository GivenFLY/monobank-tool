from monobank.core.client.acquiring import AcquiringAPIClient


class PubkeyFacade:
    def __init__(self, client: AcquiringAPIClient):
        self.client = client

    def __call__(self, params=None, data=None):
        """
        Отримання відкритого ключа для перевірки підпису, який включено у вебхуки.
        Ключ можна кешувати і робити запит на отримання нового,
        коли верифікація підпису з поточним ключем перестане працювати.
        Кожного разу робити запит на отримання ключа не треба

        :param params: параметри запиту
        :param data: дані запиту
        :return: urllib.response
        """
        return self.client.get("merchant/pubkey", params=params, data=data)
