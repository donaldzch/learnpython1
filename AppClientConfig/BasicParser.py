__author__ = 'DonaldZhu'

from __init__ import *


class BasicParser(object):
    parserKey = 'BasicParser'

    def __init__(self, variable, parserKey=None):
        self.var = variable
        self.parserKey = parserKey and parserKey or self.parserKey
        self.error = ConfigError(self.parserKey)
