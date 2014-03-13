__author__ = 'Donald'

from __init__ import *


class _AllowedAuthenticationSourcesParser(AllowedCollectionParser):
    parserKey = 'allowedAuthenticationSources'
    attrName = 'authenticationSource'
    notAllowedMessage = 'defaultAuthenticationSource'

    def __init__(self, authSources, extraParams, attributes):
        self.allowedCollection = authSources
        AllowedCollectionParser.__init__(self, authSources,
                                         attributes, 'defaultAuthenticationSource', extraParams)


def parse(allowedAuthSources, extraParams, attributes):
    print ('allowedAuthenticationSources')
    _AllowedAuthenticationSourcesParser(allowedAuthSources, extraParams, attributes).parse()