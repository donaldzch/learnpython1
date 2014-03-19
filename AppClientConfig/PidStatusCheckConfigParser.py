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
        'allowedUserStatus': (AllowedCollectionParser, True, )
    }
