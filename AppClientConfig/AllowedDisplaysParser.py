__author__ = 'Donald'

from __init__ import *


class _AllowedDisplaysParser(AllowedCollectionParser):
    allowedCollection = {'displayType': ("origin_store", "xbox360", "origin_client", "fifa_mobile",
                                         "web/create", "web/login", "pc/create", "pc/login", "lockbox/create",
                                         "lockbox/login", "mobile/login", "mobilegame/login", "console/welcome",
                                         "console2/welcome")}
    parserKey = 'allowedDisplays'
    attrName = 'displayType'
    notAllowedMessage = 'defaultDisplay'


def parse(allowedDisplays, extraParams, attributes):
    print ('allowedDisplays')
    _AllowedDisplaysParser(allowedDisplays, attributes, 'defaultDisplay', extraParams).parse()
