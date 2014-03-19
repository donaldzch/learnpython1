__author__ = 'Donald'

from __init__ import *


class _AllowedGrantTypesParser(AllowedCollectionParser):
    allowedCollection = ('authorization_code', 'refresh_token', 'exchange', 'password', 'client_credentials')
    parserKey = 'allowedGrantTypes'

    def __init__(self, allowedGrantTypes, attributes):
        AllowedCollectionParser.__init__(self, currentCollection=allowedGrantTypes, attrName=attributes[0])


def parse(allowedGrantTypes, attributes):
    _AllowedGrantTypesParser(allowedGrantTypes, attributes).parse()