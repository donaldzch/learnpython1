__author__ = 'Donald'

"""
    <throttleConfigs>
        <throttleConfig>
            <configName>pid_put</configName>
            <configuration>
                <unitTime>10000</unitTime>
                <maximumRequest>10000000</maximumRequest>
                <accessState>allowed</accessState>
            </configuration>
        </throttleConfig>
        <throttleConfig>
            <configName>pid_get</configName>
            <configuration>
                <unitTime>10000</unitTime>
                <maximumRequest>10000000</maximumRequest>
                <accessState>allowed</accessState>
            </configuration>
        </throttleConfig>
    </throttleConfigs>
"""

from __init__ import *


class _ConfigurationParser(SequenceParser):
    parserKey = 'throttleConfiguration'

    sequence = {
        'unitTime': (LongParser, True, None),
        'maximumRequest': (LongParser, True, None),
        'accessState': (CollectionParser, True, {'collections': AllowedCollectionConstant.THROTTLE_ACCESS_STATE})
    }


class _ThrottleConfigParser(SequenceParser):
    parserKey = 'throttleConfig'

    sequence = {
        'configName': (CollectionParser, True, {'collections': ('pid_get', 'pid_put')}),
        'configuration': (_ConfigurationParser, True, ['unitTime', 'maximumRequest', 'accessState'])
    }


class _ThrottleConfigsParser(ListParser):
    parserKey = 'throttleConfigs'

    def __init__(self, throttleConfigs, attributes):
        ListParser.__init__(self, listConfig=throttleConfigs, attributes=attributes,
                            parser=_ThrottleConfigParser)


def parse(throttleConfigs, attributes):
    _ThrottleConfigsParser(throttleConfigs, attributes).parse()