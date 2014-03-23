__author__ = 'Donald'

"""
        <enabled>true</enabled>
        <loginRequiredOnFailure>true</loginRequiredOnFailure>
        <enforced>true</enforced>
        <entitlements>
            <entitlement>
                <checkType>periodTrial</checkType>
                <projectId>1234</projectId>
                <productId>1234</productId>
                <autoGrant>true</autoGrant>
                <entitlementTag>1234</entitlementTag>
                <entitlementType>ONLINE_ACCESS</entitlementType>
                <group>hello</group>
                <useManagedLifeCycle>true</useManagedLifeCycle>
                <trialTimeInSeconds>300</trialTimeInSeconds>
                <trialStart>2014-01-02T00:00:00</trialStart>
                <trialEnd>2014-02-01T00:00:00</trialEnd>
            </entitlement>
        </entitlements>
"""

from __init__ import *


class _EntitlementParser(SequenceParser):
    parserKey = 'entitlement'

    sequence = {
        'checkType': (CollectionParser, False, {'collections': AllowedCollectionConstant.ENTITLEMENT_CHECK_TYPE}),
        'projectId': (LongParser, False, None),
        'productId': (LongParser, False, None),
        'autoGrant': (BooleanParser, False, None),
        'entitlementTag': (StringParser, False, None),
        'entitlementType': (CollectionParser, False, {'collections': AllowedCollectionConstant.ENTITLEMENT_TYPE}),
        'group': (StringParser, False, None),
        'useManagedLifeCycle': (BooleanParser, False, None),
        'trialTimeInSeconds': (LongParser, False, None),
        'trialStart': (DateTimeParser, False, None),
        'trialEnd': (DateTimeParser, False, None)
    }


class _EntitlementsParser(ListParser):
    parserKey = 'entitlements'

    def __init__(self, entitlements, attributes):
        ListParser.__init__(self, listConfig=entitlements, attributes=attributes, parser=_EntitlementParser)


class _EntitlementCheckConfigParser(SequenceParser):
    parserKey = 'entitlementCheckConfigParser'

    sequence = {
        'enabled': (BooleanParser, True, None),
        'loginRequiredOnFailure': (BooleanParser, False, None),
        'enforced': (BooleanParser, False, None),
        'entitlements': (_EntitlementsParser, False, ['entitlement'])
    }


def parse(entitlementCheckConfig, attributes):
    _EntitlementCheckConfigParser(entitlementCheckConfig, attributes).parse()