__author__ = 'DonaldZhu'

from __init__ import *


class StringParser(BasicParser):
    parserKey = 'StringParser'

    def parse(self):
        if isinstance(self.var, str) or isinstance(self.var, unicode):
            pass
        else:
            raise self.error
