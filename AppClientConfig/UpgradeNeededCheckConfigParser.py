__author__ = 'Donald'

"""
<upgradeNeededCheckConfig>
    <enabled>true</enabled>
</upgradeNeededCheckConfig>
"""

from __init__ import *


class _UpgradeNeededCheckConfigParser(SequenceParser):
    sequence = {
        'enabled': (BooleanParser, True, None)
    }
    parserKey = 'upgradeNeededCheckConfig'


def parse(upgradeNeededCheckConfig, attributes):
    _UpgradeNeededCheckConfigParser(upgradeNeededCheckConfig, attributes).parse()