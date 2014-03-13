__author__ = 'Donald'

from __init__ import *


class CollectionParser():

    def __init__(self, collections, error):
        self.collections = collections
        self.error = error

    def parse(self, collection):
        if Utils.containsAll(collection, self.collections):
            pass
        else:
            raise self.error