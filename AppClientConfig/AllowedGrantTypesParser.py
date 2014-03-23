__author__ = 'Donald'

from __init__ import *


class _AllowedGrantTypesParser(AllowedCollectionParser):
    parserKey = 'allowedGrantTypes'

    def __init__(self, allowedGrantTypes, attributes):
        AllowedCollectionParser.__init__(self, currentCollection=allowedGrantTypes, attrName=attributes[0],
                                         allowedCollection=AllowedCollectionConstant.ALLOWED_GRANT_TYPES)


def parse(allowedGrantTypes, attributes):
    _AllowedGrantTypesParser(allowedGrantTypes, attributes).parse()