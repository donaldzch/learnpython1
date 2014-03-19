__author__ = 'DonaldZhu'

from __init__ import *


class LongParser(object):
    error = ConfigError('longAttribute', 'invalid')

    def __init__(self, variable, error):
        self.var = variable
        self.error = error

    def parse(self):
        try:
            long(self.var)
        except ValueError:
            raise self.error