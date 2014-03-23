__author__ = 'DonaldZhu'


from BasicParser import BasicParser
from datetime import datetime


class DateTimeParser(BasicParser):
    parserKey = 'DateTimeParser'

    def parse(self):
        try:
            datetime.strptime(self.var, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            try:
                datetime.strptime(self.var, '%Y-%m-%d')
            except ValueError:
                raise self.error