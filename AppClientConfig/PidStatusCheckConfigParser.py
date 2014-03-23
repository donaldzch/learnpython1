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
        'loginRequiredOnFailure': (BooleanParser, False, None),
        'allowedUserStatus': (AllowedCollectionParser, True, {'allowedCollection': AllowedCollectionConstant.ALLOWED_USER_STATUS,
                                                              'attrName': 'status'}),
        'allowedPersonaStatus': (AllowedCollectionParser, True, {'allowedCollection': AllowedCollectionConstant.ALLOWED_PERSONA_STATUS,
                                                                 'attrName': 'status'})
    }


def parse(pidStatusCheckConfig, attributes):
    _PidStatusCheckConfigParser(pidStatusCheckConfig, attributes).parse()