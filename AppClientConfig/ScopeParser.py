__author__ = 'Donald'

from AllowedCollectionParser import AllowedCollectionParser
import AllowedCollectionConstant


class ScopeParser(AllowedCollectionParser):

    def __init__(self, parserKey, currentCollection):
        AllowedCollectionParser.__init__(self, currentCollection=currentCollection,
                                         allowedCollection=AllowedCollectionConstant.ALLOWED_SCOPES_COLLECTIONS, attrName='scope',
                                         parserKey=parserKey)