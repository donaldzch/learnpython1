__author__ = 'DonaldZhu'

from __init__ import *


class LongParser(BasicParser):
    parserKey = 'LongParser'

    def parse(self):
        try:
            long(self.var)
        except ValueError:
            raise self.error