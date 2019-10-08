from .abstract_api import AbstractApi

class Muthofun(AbstractApi):

    def __init__(self, config):
        self.config = config
        self.sms = []
        self.debug = False
        self.mobiles = []
        self.template = True
        self._auto_parse = False
        self._sending_parameters = {}

        super().__init__()

    # All Public methonds

    def message(self, message = '', to = None):
        # self.sms = message
        self.sms.append(message)
        if to is not None:
            self.mobiles.append(to)

        return self
    
    def to(self, to = ''):
        self.mobiles.append(to)
        
        return self

    def debug(self, debug = False):
        self.debug = debug

        return self
    
    def auto_parse(self, _auto_parse = True):
        self._auto_parse = auto_parse

        return self
    
    def template(self, template = True):
        self.template = True

        return self
    
    def send(self, opts = []):
        if len(opts) > 0:
            self.__set_message_and_mobiles(opts)
            pass

        self.__distribute_sms()

    # All Protected Methods 

    def _set_base_url(self):
        return 'http://clients.muthofun.com:8901/'
 
    def _set_sending_url(self):
        return 'esmsgw/sendsms.jsp'

    # All Private Methods 

    def __set_parameters(self, sms, mobile):
        self._sending_parameters = {
            'user' : self.config['username'],
            'password': self.config['password'],
            'sms' : sms,
            'mobiles' : mobile,
            'unicode': 1
        }
        
        return self

    def __distribute_sms(self):
        total_sms = len(self.sms)
        total_receiver = len(self.mobiles)

        i = 0
        while i < total_sms:
            if isinstance(self.mobiles[i], list):
                self.__distribute_to_many(self.sms[i], self.mobiles[i])
            else:
                self.__distribute_to_one(self.sms[i], self.mobiles[i])    
            i += 1
        pass

    def __distribute_to_one(self, sms, to):
        self.__set_parameters(sms, to)
        self._set_query(self._sending_parameters)._send_to_server()
        pass

    def __distribute_to_many(self, sms, to):
        for receiver in to:
            self.__distribute_to_one(sms, receiver)
        pass

    def __set_message_and_mobiles(self, opts = []):

        for item in opts:
            if isinstance(item, dict):
                self.sms.append(item['sms'])
                self.mobiles.append(item['to'])
            
        pass