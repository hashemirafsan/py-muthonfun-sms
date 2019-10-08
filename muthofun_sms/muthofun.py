from abstract_api import AbstractApi

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


    def set_base_url(self):
        return 'http://clients.muthofun.com:8901/'
 
    def set_sending_url(self):
        return 'esmsgw/sendsms.jsp'

    def message(self, message = '', to = None):
        self.sms.append(message)
        return self
    
    def to(self, to):
        pass

    def __get_parameters(self, sms, mobiles):
        self._sending_parameters = {
            'username' : self.config['username'],
            'password': self.config['password'],
            'sms' : sms,
            'mobiles' : mobiles,
            'unicode': 1
        }
        
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

    def get_config(self):
        return self.config



r = Muthofun({
    'username': 'hashemirafsan',
    'password': 'rafsan'
})

print(r.get_config())