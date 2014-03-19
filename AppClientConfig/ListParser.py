__author__ = 'DonaldZhu'

from __init__ import *


class ListParser(AttributeParser):
    parserKey = 'ListParser'

    def __init__(self, listConfig, attributes, parser):
        AttributeParser.__init__(self, listConfig, attributes, self.parserKey)
        self.listConfig = listConfig.get(attributes[0])
        self.parser = parser

    def parse(self):
        AttributeParser.parse(self)
        items = isinstance(self.listConfig, list) and self.listConfig or [self.listConfig]
        for item in items:
            self.parser(item).parse()