from .Service import APIService


class SMSService(APIService):

    def __init__(self, api_key):
        super(SMSService, self).__init__(api_key)

    def _init_service(self):
        super(SMSService, self)._init_service()
        self._baseUrl = self._baseUrl + '/messaging'

    def check_balance(self):
        url = self._make_url(path='/account_balance')
        return self._make_request(url=url, method='GET',headers=self.headers, data=None, params=None)

    def fetch_messages(self):
        url = self._make_url(path='/fetch_messages')
        return self._make_request(url=url, method='GET',headers=self.headers, data=None, params=None)

    def send(self, phone_number, message):
        pass