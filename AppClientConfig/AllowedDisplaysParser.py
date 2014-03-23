__author__ = 'Donald'

from __init__ import *


class _AllowedDisplaysParser(AllowedCollectionParser):
    parserKey = 'allowedDisplays'
    notAllowedMessage = 'defaultDisplay'

    def __init__(self, allowedDisplays, attributes, extraParams):
        AllowedCollectionParser.__init__(self, currentCollection=allowedDisplays, attrName=attributes[0],
                                         allowedCollection=AllowedCollectionConstant.ALLOWED_DISPLAYS,
                                         defaultAttrName='defaultDisplay', defaultCollection=extraParams)


def parse(allowedDisplays, extraParams, attributes):
    _AllowedDisplaysParser(allowedDisplays, attributes, extraParams).parse()
