from abc import ABC, abstractmethod, abstractproperty

class AbstractApi(ABC):

    def __init__(self):
        self._base_url = self.set_base_url()
        self._sending_url = self.set_sending_url()
        self._default_headers = self.set_default_headers()

    @abstractmethod
    def set_base_url(self):
        pass
    
    @abstractmethod
    def set_sending_url(self):
        pass

    def get_access_token(self):
        return ''

    def set_default_headers(self):
        return {}

    def get_base_url(self):
        return self._base_url