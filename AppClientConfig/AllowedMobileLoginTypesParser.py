__author__ = 'Donald'

from __init__ import *


class _AllowedMobileLoginTypesParser(AllowedCollectionParser):
    allowedCollection = ('mobile_game_UPID', 'mobile_game_facebook', 'mobile_game_origin')
    parserKey = 'allowedMobileLoginTypes'

    def __init__(self, allowedMobileLoginTypes, attributes):
        AllowedCollectionParser.__init__(self, currentCollection=allowedMobileLoginTypes, attrName=attributes[0])


def parse(allowedMobileLoginTypes, attributes):
    _AllowedMobileLoginTypesParser(allowedMobileLoginTypes, attributes).parse()