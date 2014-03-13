__author__ = 'Donald'

from __init__ import *


class _AllowedRegistrationSourcesParser(AllowedCollectionParser):
    parserKey = 'allowedRegistrationSources'
    attrName = 'registrationSource'
    notAllowedMessage = 'defaultRegistrationSource'

    def __init__(self, registrationSources, extraParams, attributes):
        self.allowedCollection = registrationSources
        AllowedCollectionParser.__init__(self, registrationSources,
                                         attributes, 'defaultRegistrationSource', extraParams)


def parse(allowedRegistrationSources, extraParams, attributes):
    print ('allowedRegistrationSources')
    _AllowedRegistrationSourcesParser(allowedRegistrationSources, extraParams, attributes).parse()