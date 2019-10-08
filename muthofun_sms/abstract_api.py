import requests
from abc import ABC, abstractmethod, abstractproperty


class AbstractApi(ABC):

    def __init__(self):
        self._parameters = {}
        self._query = {}
        self._base_url = self._set_base_url()
        self._sending_url = self._set_sending_url()
        self._default_headers = self._set_default_headers()

    @abstractmethod
    def _set_base_url(self):
        pass
    
    @abstractmethod
    def _set_sending_url(self):
        pass

    def _set_default_headers(self):
        return {}

    def _headers(headers = {}):
        if isinstance(headers, dict):
            self._parameters['headers'] = headers
            
            return self

        return False     

    def _query(query = {}):
        if isinstance(query, dict):
            self._parameters['query'] = query

            return self
        
        return False
    
    def _send_to_server(self, parameters):
        r = requests.get(self._base_url + self._sending_url, 
        auth=('hashemirafsa', 'rafsanJ1#'), 
        params={
            'user': 'hashemirafsa', 
            'password': 'rafsanJ1#', 
            'sms': 'I Love you Shipu Vai from python package', 
            'mobiles': '8801707722669', 
            'unicode': 1,
            'senderid': 'Aruhat'
        }
        )
        return r.text