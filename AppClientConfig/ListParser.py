__author__ = 'DonaldZhu'

from __init__ import *


class ListParser(AttributeParser):
    parserKey = 'ListParser'

    def __init__(self, listConfig, attributes, parser, parserAttr):
        AttributeParser.__init__(self, listConfig, attributes, ConfigError(self.parserKey))
        self.listConfig = listConfig
        self.parser = parser
        self.parserAttr = parserAttr

    def parse(self):
        AttributeParser.parse(self)
        items = isinstance(self.listConfig, list) and self.listConfig or [self.listConfig]
        for item in items:
            self.parser(item, self.parserAttr).parse()