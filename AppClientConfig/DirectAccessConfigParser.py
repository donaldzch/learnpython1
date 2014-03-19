__author__ = 'Donald'

"""
        <enabled>true</enabled>
        <userIdState>anyone</userIdState>
        <scopes>
            <scope>basic.identity</scope>
            <scope>basic.persona</scope>
            <scope>basic.entitlement</scope>
        </scopes>
        <allowIps>
            <ip>192.168.1.1</ip>
        </allowIps>
"""

from __init__ import *


class _UserIdStateParser(CollectionParser):
    stateCollection = ('anyone', 'no_one')

    def __init__(self, value):
        CollectionParser.__init__(self, self.stateCollection, ConfigError('directAccessConfig', 'invalid userIdState'))
        self.collection = value

    def parse(self):
        CollectionParser.parse(self, self.collection)


class _AllowIpsParser(AttributeParser):
    attrError = ConfigError('directAccessConfig', 'invalid ip in allowIps')


class _DirectAccessConfigParser(AttributeParser):
    attrError = ConfigError('directAccessConfig')

    def parse(self):
        AttributeParser.parse(self)
        BooleanParser(self.configure.get('enabled'), self.attrError).parse()
        if self.configure.get('userIdState') is not None:
            _UserIdStateParser(self.configure.get('userIdState')).parse()
        if self.configure.get('scopes') is not None:
            ScopeParser('directAccessConfig', self.configure.get('scopes'), ['scope']).parse()
        if self.configure.get('allowIps') is not None:
            _AllowIpsParser(self.configure.get('allowIps'), ['ip']).parse()


def parse(directAccessConfig, attributes):
    _DirectAccessConfigParser(directAccessConfig, attributes).parse()