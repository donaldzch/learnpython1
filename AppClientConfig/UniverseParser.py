__author__ = 'Donald'

from __init__ import *


class _UniverseParser(CollectionParser):
    parserKey = 'universe'

    def __init__(self, universe):
        CollectionParser.__init__(self, universe, AllowedCollectionConstant.UNIVERSE)


def parse(universe):
    _UniverseParser(universe).parse()