__author__ = 'DonaldZhu'

from BasicParser import BasicParser


class LongParser(BasicParser):
    parserKey = 'LongParser'

    def parse(self):
        try:
            long(self.var)
        except ValueError:
            raise self.error