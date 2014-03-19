__author__ = 'DonaldZhu'

from __init__ import *


class StringParser(object):
    error = ConfigError('StringParser', 'invalid')

    def __init__(self, variable, error):
        self.var = variable
        self.error = error

    def parse(self):
        if isinstance(self.var, str) or isinstance(self.var, unicode):
            pass
        else:
            raise self.error