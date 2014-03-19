__author__ = 'Donald'

from __init__ import *


class AttributeParser(CollectionParser):
    attrError = ConfigError('Attribute', 'Invalid')

    def __init__(self, configure, attributes, attrError=None):
        self.attrError = attrError and attrError or self.attrError
        CollectionParser.__init__(self, attributes, self.attrError)
        self.configure = configure

    def parse(self):
        if isinstance(self.configure, dict):
            keys = Utils.getDictKeys(self.configure)
            if len(keys):
                CollectionParser.parse(self, keys)