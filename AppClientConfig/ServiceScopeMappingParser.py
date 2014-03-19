__author__ = 'Donald'

"""
    <serviceScopeMapping>
        <serviceScope>
            <serviceName>service.identity</serviceName>
            <serviceScopeConfig>
                <scopes>
                    <scope>basic.identity</scope>
                    <scope>basic.identity.write</scope>
                </scopes>
            </serviceScopeConfig>
        </serviceScope>
    </serviceScopeMapping>

"""

from __init__ import *


class _ServiceScopeMappingParser(ListParser):
    parserKey = 'serviceScopeMapping'

    def __init__(self, serviceScopeMapping, attributes):
        ListParser.__init__(self, listConfig=serviceScopeMapping, attributes=attributes, parser=_ServiceScopeParser)


class _ServiceScopeParser(SequenceParser):
    parserKey = 'serviceScope'

    sequence = {
        'serviceName': (CollectionParser, True, {'collections': ('service.identity', 'service.atom',
                                                                 'service.fifa_server', 'service.orginsdk2')}),
        'serviceScopeConfig': (AttributeParser, True, ['scopes'])
    }

    def parse(self):
        SequenceParser.parse(self)
        ScopeParser('serviceScopeConfig', self.configure.get('serviceScopeConfig').get('scopes'))


def parse(serviceScopeMapping, attributes):
    _ServiceScopeMappingParser(serviceScopeMapping, attributes).parse()