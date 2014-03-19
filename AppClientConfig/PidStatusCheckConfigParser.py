__author__ = 'Donald'

"""
        <enabled>true</enabled>
        <loginRequiredOnFailure>true</loginRequiredOnFailure>
        <allowedUserStatus>
            <status>ACTIVE</status>
        </allowedUserStatus>
        <allowedPersonaStatus>
            <status>ACTIVE</status>
        </allowedPersonaStatus>
"""

from __init__ import *


class _PidStatusCheckConfigParser(SequenceParser):
    parserKey = 'pidStatusCheckConfig'
    sequence = {
        'enabled': (BooleanParser, True, None),
        'loginRequiredOnFailure': (BooleanParser, True, None),
        'allowedUserStatus': (AllowedCollectionParser, True, {'allowedCollection': ('ACTIVE', 'CHILD_APPROVED',
                                                                                    'CHILD_PENDING', 'PENDING',
                                                                                    'DISABLED', 'BANNED'),
                                                              'attrName': 'status'}),
        'allowedPersonaStatus': (AllowedCollectionParser, True, {'allowedCollection': ('ACTIVE', 'PENDING', 'BANNED'),
                                                                 'attrName': 'status'})
    }


def parse(pidStatusCheckConfig, attributes):
    _PidStatusCheckConfigParser(pidStatusCheckConfig, attributes).parse()