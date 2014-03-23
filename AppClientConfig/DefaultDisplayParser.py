__author__ = 'Donald'

from __init__ import *


class _DefaultDisplayParser(CollectionParser):
    parserKey = 'defaultDisplay'


def parse(defaultDisplay):
    _DefaultDisplayParser(defaultDisplay, collections=AllowedCollectionConstant.ALLOWED_DISPLAYS).parse()
