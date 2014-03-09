__author__ = 'Donald'

from __init__ import *


class CollectionParser():
    collections = ()

    def __init__(self, collection, key, error):
        self.collection = collection
        self.key = key
        self.error = error

    def parse(self):
        if Utils.containsAll(self.collection, self.collections):
            pass
        else:
            raise ConfigError(self.key, self.error)