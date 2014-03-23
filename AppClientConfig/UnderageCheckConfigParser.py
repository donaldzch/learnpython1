__author__ = 'Donald'

"""
    <underageCheckConfig>
        <enabled>true</enabled>
        <ageUpEnabled>true</ageUpEnabled>
        <loginRequiredOnFailure>true</loginRequiredOnFailure>
        <overrideEntitlements>
            <entitlement>
                <entitlementTag>123</entitlementTag>
                <entitlementType>SUBSCRIPTIONS</entitlementType>
                <group>123</group>
                <productId>1234</productId>
                <projectId>1234</projectId>
            </entitlement>
        </overrideEntitlements>
    </underageCheckConfig>

"""

from __init__ import *


class _Entitlement(SequenceParser):
    parserKey = 'entitlement'

    sequence = {
        'entitlementTag': (StringParser, False, None),
        'entitlementType': (CollectionParser, False, {'collections': ('SUBSCRIPTIONS')}),
        'group': (StringParser, False, None),
        'productId': (LongParser, False, None),
        'projectId': (LongParser, False, None),
    }


class _OverrideEntitlements(ListParser):
    parserKey = 'overrideEntitlements'

    def __init__(self, overrideEntitlements, attributes):
        ListParser.__init__(self, listConfig=overrideEntitlements, attributes=attributes,
                            parser=_Entitlement)


class _UnderageCheckConfig(SequenceParser):
    parserKey = 'underageCheckConfig'

    sequence = {
        'enabled': (BooleanParser, True, None),
        'ageUpEnabled': (BooleanParser, False, None),
        'loginRequiredOnFailure': (BooleanParser, False, None),
        'overrideEntitlements': (_OverrideEntitlements, False, ['entitlement'])
    }


def parse(underageCheckConfig, attributes):
    _UnderageCheckConfig(underageCheckConfig, attributes).parse()