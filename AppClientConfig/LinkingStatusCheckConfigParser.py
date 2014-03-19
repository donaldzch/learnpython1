__author__ = 'Donald'

"""
<linkingStatusCheckConfig>
    <enabled>true1</enabled>
</linkingStatusCheckConfig>
"""

from __init__ import *


class _LinkStatusCheckConfigParser(SequenceParser):
    sequence = {
        'enabled': (BooleanParser, True, None)
    }
    parserKey = 'linkStatusCheckConfig'


def parse(linkStatusCheckConfig, attributes):
    _LinkStatusCheckConfigParser(linkStatusCheckConfig, attributes).parse()