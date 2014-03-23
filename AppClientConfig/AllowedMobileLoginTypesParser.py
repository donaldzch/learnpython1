__author__ = 'Donald'

from __init__ import *


class _AllowedMobileLoginTypesParser(AllowedCollectionParser):
    parserKey = 'allowedMobileLoginTypes'

    def __init__(self, allowedMobileLoginTypes, attributes):
        AllowedCollectionParser.__init__(self, currentCollection=allowedMobileLoginTypes, attrName=attributes[0],
                                         allowedCollection=AllowedCollectionConstant.ALLOWED_MOBILE_LOGIN_TYPES)


def parse(allowedMobileLoginTypes, attributes):
    _AllowedMobileLoginTypesParser(allowedMobileLoginTypes, attributes).parse()