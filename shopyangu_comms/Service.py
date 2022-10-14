import requests
import json
import phonenumbers

class ShopyanguCommunicationsException(Exception):
    pass



class BaseService(object):
    baseUrl = "https://comms-api.shopyangu.com"

    def __init__(self, api_key, logger=None):

        if type(api_key) is not str:
            raise RuntimeError('api-key has to be of type str.')

        if not logger:
            import logging
            logger = logging.getLogger(__name__)

        self._api_key = api_key
        self.headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'User-Agent': 'shopyangu-comms-python/1.0.0',
            'api-key': self._api_key
        }
        self._baseUrl = self.__class__.baseUrl

        self._init_service()

    def _init_service(self):
        raise NotImplementedError


    def _make_url(self, path):
        return self._baseUrl + path

    def is_phone_number_valid(self, phone_number):
        """
        Given a phone number make sure that it is valid.
        Arguments:
        ---------
            Phonenumber: --> The phone number we want to validate.

            Example: is_phone_number_valid(phone_number="+254748348947")

        Returns a boolean that indicates whether the number is of a valid pattern.
        """
        try:
            phone_num_to_validate = phonenumbers.parse(phone_number, None)
            is_a_valid_phone_number = phonenumbers.is_valid_number(phone_num_to_validate)
            if is_a_valid_phone_number:
                return True
        except Exception:
            return False
        
        return False

    @staticmethod
    def __make_get_request(url, headers, data,params):
        respose = requests.get(
            url=url,
            headers=headers,
            params=params,
            data=data
        )
        return respose

    @staticmethod
    def __make_post_request(url, headers, data, params):
        respose = requests.post(
            url=url,
            headers=headers,
            params=params,
            data=data,
        )
        return respose

    def _make_request(self, url, method, headers, data, params):
        method = method.upper()
        data = json.dumps(data)

        if method == 'POST':
            res = self.__make_post_request(url=url, headers=headers, data=data, params=params)
        
        elif method == 'GET':
            res = self.__make_get_request(url=url, headers=headers, data=data, params=params)
        
        else:
            raise ShopyanguCommunicationsException('Unexpected HTTP method: ' + method)

        if 200 <= res.status_code < 300:
            if res.headers.get('content-type') == 'application/json':
                response = json.loads(res.content)
                return response
            else:
                response = json.loads(res.text)
                return response
        
        else:
            raise ShopyanguCommunicationsException(res.text)



class APIService(BaseService):

    def __init__(self, api_key):
        super(APIService, self).__init__(api_key)

    def _init_service(self):
        self._baseUrl = self._baseUrl + '/api/v1/comms'
    
