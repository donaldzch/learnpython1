__author__ = 'Donald'

from Utils import Utils
from Error.ConfigError import ConfigError


class CollectionParser():
    collections = ()
    parserKey = 'collectionParser'
    errorMsg = 'contains invalid value'

    def __init__(self, collection, collections=(), parserKey=None, errorMsg=None):
        self.collections = collections and collections or self.collections
        self.collection = collection
        self.parserKey = parserKey and parserKey or self.parserKey
        self.errorMsg = errorMsg and errorMsg or self.errorMsg
        self.error = ConfigError(self.parserKey, self.errorMsg)

    def parse(self):
        if Utils.containsAll(self.collection, self.collections):
            pass
        else:
            raise self.error