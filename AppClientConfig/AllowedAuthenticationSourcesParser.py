__author__ = 'Donald'

from __init__ import *


class _AllowedAuthenticationSourcesParser(AllowedCollectionParser):
    parserKey = 'allowedAuthenticationSources'
    notAllowedMessage = 'defaultAuthenticationSource'

    def __init__(self, authSources, extraParams, attributes):
        AllowedCollectionParser.__init__(self, currentCollection=authSources,
                                         allowedCollection=authSources.get(attributes[0]),
                                         attrName=attributes[0],
                                         defaultAttrName='defaultAuthenticationSource',
                                         defaultCollection=extraParams)


def parse(allowedAuthSources, extraParams, attributes):
    print ('allowedAuthenticationSources')
    _AllowedAuthenticationSourcesParser(allowedAuthSources, extraParams, attributes).parse()