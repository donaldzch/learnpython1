__author__ = 'Donald'

from __init__ import *


class ScopeParser(AllowedCollectionParser):

    def __init__(self, parserKey, currentCollection):
        AllowedCollectionParser.__init__(self, currentCollection=currentCollection,
                                         allowedCollection=ALLOWED_SCOPES_COLLECTIONS, attrName='scope',
                                         parserKey=parserKey)