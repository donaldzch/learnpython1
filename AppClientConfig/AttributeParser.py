__author__ = 'Donald'

from CollectionParser import CollectionParser
from Utils import Utils


class AttributeParser(CollectionParser):
    parserKey = "AttributeParser"

    def __init__(self, configure, attributes, parserKey=None):
        self.parserKey = parserKey and parserKey or self.parserKey
        self.configure = configure
        CollectionParser.__init__(self, collection=Utils.getDictKeys(configure),
                                  collections=attributes, parserKey=self.parserKey, errorMsg='invalid attribute')