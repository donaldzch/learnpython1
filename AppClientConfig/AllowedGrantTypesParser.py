__author__ = 'Donald'

from __init__ import *


class _AllowedGrantTypesParser(AllowedCollectionParser):
    allowedCollection = {"grantType": ('authorization_code', 'refresh_token', 'exchange', 'password',
                                       'client_credentials')}
    parserKey = 'allowedGrantTypes'
    attrName = 'grantType'


def parse(allowedGrantTypes, attributes):
    _AllowedGrantTypesParser(allowedGrantTypes, attributes).parse()