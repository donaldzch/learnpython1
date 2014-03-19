__author__ = 'DonaldZhu'

from __init__ import *


class BooleanParser(object):
    error = ConfigError('booleanParser', 'invalid')

    def __init__(self, variable, error):
        self.var = variable
        self.error = error

    def parse(self):
        try:
            if str(self.var).upper() == 'TRUE' or str(self.var).upper() == 'FALSE':
                pass
            else:
                raise self.error
        except ValueError:
            raise self.error