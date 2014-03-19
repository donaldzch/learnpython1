__author__ = 'Donald'

"""
        <enabled>true</enabled>
        <scopes>
            <scope>basic.identity</scope>
            <scope>basic.identity.write</scope>
        </scopes>
"""

from __init__ import *


class _AuthTokenAccessParser(SequenceParser):
    sequence = {
        'enabled': (BooleanParser, True, None),
        'scopes': (ScopeParser, False, None)
    }
    parserKey = 'authTokenAccess'


def parse(authTokenAccess, attributes):
    _AuthTokenAccessParser(authTokenAccess, attributes).parse()