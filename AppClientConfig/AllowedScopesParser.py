__author__ = 'Donald'

from __init__ import *


class _AllowedScopesParser(AllowedCollectionParser):
    allowedCollection = ('code', 'token', 'id_token')
    parserKey = 'allowedScopes'

    def __init__(self, allowedScopes, attributes, defaultScopesCollection):
        defaultScopes = defaultScopesCollection and defaultScopesCollection.get('defaultScopes') or None
        AllowedCollectionParser.__init__(self, currentCollection=allowedScopes, attrName=attributes[0],
                                         defaultAttrName='scope', defaultCollection=defaultScopes)


def parse(allowedScopes, extraParams, attributes):
    _AllowedScopesParser(allowedScopes, attributes, extraParams).parse()