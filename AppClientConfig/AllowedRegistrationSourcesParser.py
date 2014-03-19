__author__ = 'Donald'

from __init__ import *


class _AllowedRegistrationSourcesParser(AllowedCollectionParser):
    parserKey = 'allowedRegistrationSources'
    notAllowedMessage = 'defaultRegistrationSource'

    def __init__(self, registrationSources, extraParams, attributes):
        AllowedCollectionParser.__init__(self, currentCollection=registrationSources,
                                         allowedCollection=registrationSources.get(attributes[0]),
                                         attrName=attributes[0],
                                         defaultAttrName='defaultRegistrationSource', defaultCollection=extraParams)


def parse(allowedRegistrationSources, extraParams, attributes):
    _AllowedRegistrationSourcesParser(allowedRegistrationSources, extraParams, attributes).parse()