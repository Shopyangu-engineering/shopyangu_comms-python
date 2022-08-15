from .Service import APIService


class SMSService(APIService):

    def __init__(self, api_key):
        super(SMSService, self).__init__(api_key)

    def _init_service(self):
        super(SMSService, self)._init_service()
        self._baseUrl = self._baseUrl + '/messaging'

    def check_balance(self):
        url = self._make_url(path='/account_balance/')
        return self._make_request(url=url, method='GET',headers=self.headers, data=None, params=None)


    def fetch_messages(self):
        url = self._make_url(path='/fetch_messages/')
        return self._make_request(url, 'GET', headers=self.headers, params=None, data=None)

    def send(self, message, recipient, sender_id=None):
        if not self.is_phone_number_valid(recipient):
            raise ValueError('Invalid phone number: ' + recipient)

        url = self._make_url('/send_sms/')
        data = {
            "to": recipient,
            "message": message,
        }

        if sender_id is not None:
            data["sender_id"] = sender_id
        
        return self._make_request(url, 'POST', headers=self.headers, params=None, data=data)

    def fetch_delivery_status(self, message_id):
        url = self._make_url('/check_delivery_status/')
        data = {"message_id": message_id}
        return self._make_request(url, 'GET', headers=self.headers, params=None, data=data)
