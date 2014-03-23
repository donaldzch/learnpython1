__author__ = 'Donald'

from Error.ConfigError import ConfigError
from AttributeParser import AttributeParser
from CollectionParser import CollectionParser


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
        AttributeParser.__init__(self, self.currentCollection, [self.attrName], self.parserKey)
        self.attr = currentCollection and currentCollection.get(self.attrName) or None
        self.defaultAttr = defaultCollection and defaultCollection.get(defaultAttrName) or None
        self.defaultCollectionParser = defaultCollection and CollectionParser(collection=self.defaultAttr,
                                                                              collections=self.currentCollection.get(self.attrName),
                                                                              parserKey=self.parserKey,
                                                                              errorMsg=self.notAllowedMessage) or None
        self.currentCollectionParser = currentCollection and CollectionParser(collection=self.attr,
                                                                              collections=self.allowedCollection,
                                                                              parserKey=self.parserKey,
                                                                              errorMsg=self.notAllowedMessage) or None

    def parse(self):
        AttributeParser.parse(self)
        if self.defaultCollectionParser is not None:
            self.defaultCollectionParser.parse()
        if self.currentCollectionParser is not None:
            self.currentCollectionParser.parse()
