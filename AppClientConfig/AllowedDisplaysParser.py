__author__ = 'Donald'

from __init__ import *


class _AllowedDisplaysParser(AllowedCollectionParser):
    allowedCollection = ("origin_store", "xbox360", "origin_client", "fifa_mobile",
                                         "web/create", "web/login", "pc/create", "pc/login", "lockbox/create",
                                         "lockbox/login", "mobile/login", "mobilegame/login", "console/welcome",
                                         "console2/welcome")
    parserKey = 'allowedDisplays'
    notAllowedMessage = 'defaultDisplay'

    def __init__(self, allowedDisplays, attributes, extraParams):
        AllowedCollectionParser.__init__(self, currentCollection=allowedDisplays, attrName=attributes[0],
                                         defaultAttrName='defaultDisplay', defaultCollection=extraParams)


def parse(allowedDisplays, extraParams, attributes):
    _AllowedDisplaysParser(allowedDisplays, attributes, extraParams).parse()
