__author__ = 'Donald'

from __init__ import *


class _UniverseParser():
    collections = ("default", "integration", "lt", "lt-rs", "lt-sh", "production")
    error = ConfigError('universe')

    def __init__(self):
        self.universe = CollectionParser(self.collections, self.error)

    def parse(self, universe):
        self.universe.parse(universe)


def parse(universe):
    print ("universe")
    _UniverseParser().parse(universe)