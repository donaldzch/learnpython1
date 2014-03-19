__author__ = 'DonaldZhu'

from __init__ import *

from datetime import datetime


class DateTimeParser(object):
    error = ConfigError('dateTimeAttribute', 'invalid')

    def __init__(self, variable, error):
        self.var = variable
        self.error = error

    def parse(self):
        try:
            datetime.strptime(self.var, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            try:
                datetime.strptime(self.var, '%Y-%m-%d')
            except ValueError:
                raise self.error