__author__ = 'DonaldZhu'

from __init__ import *


class BooleanParser(BasicParser):
    parserKey = 'BooleanParser'

    def parse(self):
        try:
            if str(self.var).upper() == 'TRUE' or str(self.var).upper() == 'FALSE':
                pass
            else:
                raise self.error
        except ValueError:
            raise self.error