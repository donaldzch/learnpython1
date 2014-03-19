__author__ = 'Donald'

from __init__ import *


class _UniverseParser(CollectionParser):
    collections = ("default", "integration", "lt", "lt-rs", "lt-sh", "production")
    parserKey = 'universe'

    def __init__(self, universe):
        CollectionParser.__init__(self, universe, self.collections)


def parse(universe):
    _UniverseParser(universe).parse()