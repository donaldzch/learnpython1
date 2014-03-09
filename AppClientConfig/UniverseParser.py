__author__ = 'Donald'

from __init__ import *


def parse(appClient):
    universeSet = ("default", "integration", "lt", "lt-rs", "lt-sh", "production")
    print ("universe")
    try:
        universe = appClient["universe"]
    except KeyError:
        pass
    else:
        if Utils.containsAll(str(universe), universeSet):
            pass
        else:
            raise AttributeError()