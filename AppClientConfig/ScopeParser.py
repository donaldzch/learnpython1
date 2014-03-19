__author__ = 'Donald'

from __init__ import *


class ScopeParser(AllowedCollectionParser):
    allowedCollection = ('authorization_code', 'refresh_token', 'exchange', 'password', 'client_credentials')

    def __init__(self, parserKey, currentCollection):
        AllowedCollectionParser.__init__(self, currentCollection=currentCollection, attrName='scope',
                                         parserKey=parserKey)