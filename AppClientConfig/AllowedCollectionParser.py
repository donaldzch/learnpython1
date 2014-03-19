__author__ = 'Donald'

from __init__ import *


class AllowedCollectionParser(AttributeParser):
    allowedCollection = {}
    currentCollection = {}
    parserKey = 'AllowedCollection'
    attrName = 'AttributeName'
    notAllowedMessage = 'notAllowed'
    defaultCollectionParser = None

    def __init__(self, currentCollection, allowedCollection={},
                 parserKey=None, attrName=None, defaultAttrName=None, defaultCollection={}):
        self.currentCollection = currentCollection
        self.allowedCollection = allowedCollection and allowedCollection or self.allowedCollection
        self.parserKey = parserKey and parserKey or self.parserKey
        self.attrName = attrName and attrName or self.attrName
        self.attrError = ConfigError(self.parserKey, self.attrName)
        self.notAllowedError = ConfigError(self.parserKey, self.notAllowedMessage)
        AttributeParser.__init__(self, self.currentCollection, [self.attrName])
        self.attr = currentCollection and currentCollection.get(self.attrName) or None
        self.defaultAttr = defaultCollection and defaultCollection.get(defaultAttrName) or None
        self.defaultCollectionParser = defaultCollection and CollectionParser(self.currentCollection.get(self.attrName),
                                                                              self.notAllowedError) or None
        self.currentCollectionParser = currentCollection and CollectionParser(self.allowedCollection,
                                                                              self.notAllowedError) or None

    def parse(self):
        AttributeParser.parse(self)
        if self.defaultCollectionParser is not None:
            self.defaultCollectionParser.parse(self.defaultAttr)
        if self.currentCollectionParser is not None:
            self.currentCollectionParser.parse(self.attr)
