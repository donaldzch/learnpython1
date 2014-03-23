__author__ = 'Donald'

from __init__ import *


class _AllowedResponseTypesParser(AllowedCollectionParser):
    parserKey = 'allowedResponseTypes'

    def __init__(self, allowedResponseTypes, attrbitues):
        AllowedCollectionParser.__init__(self, currentCollection=allowedResponseTypes, attrName=attrbitues[0],
                                         allowedCollection=AllowedCollectionConstant.ALLOWED_RESPONSE_TYPES)


def parse(allowedResponseTypes, attributes):
    _AllowedResponseTypesParser(allowedResponseTypes, attributes).parse()