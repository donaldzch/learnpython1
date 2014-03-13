__author__ = 'Donald'

from __init__ import *


class _AllowedScopesParser(AllowedCollectionParser):
    allowedCollection = {"scope": ('code', 'token', 'id_token')}
    parserKey = 'allowedScopes'
    attrName = 'scope'

    def __init__(self, scopes, attributes, defaultScopesCollection):
        defaultScopes = defaultScopesCollection and defaultScopesCollection.get('defaultScopes') or None
        AllowedCollectionParser.__init__(self, scopes, attributes, 'scope', defaultScopes)


def parse(allowedResponseTypes, extraParams, attributes):
    _AllowedScopesParser(allowedResponseTypes, attributes, extraParams).parse()