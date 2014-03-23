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


class _DirectAccessConfigParser(SequenceParser):
    parserKey = 'directAccessConfig'
    sequence = {
        'enabled': (BooleanParser, True, None),
        'userIdState': (CollectionParser, True, {"collections": AllowedCollectionConstant.USER_ID_STATE}),
        'scopes': (ScopeParser, True, None),
        'allowIps': (AttributeParser, False, ['ip'])
    }
    attrError = ConfigError('directAccessConfig')


def parse(directAccessConfig, attributes):
    _DirectAccessConfigParser(directAccessConfig, attributes).parse()