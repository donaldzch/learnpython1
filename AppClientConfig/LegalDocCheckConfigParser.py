__author__ = 'Donald'

"""
<legalDocCheckConfig>
        <enabled>true</enabled>
        <gameIdentifier>default</gameIdentifier>
    </legalDocCheckConfig>
"""

from __init__ import *


class _LegalDocCheckConfigParser(SequenceParser):
    sequence = {
        'enabled': (BooleanParser, True, None)
    }
    parserKey = 'legalDocCheckConfig'


def parse(legalDocCheckConfig, attributes):
    _LegalDocCheckConfigParser(legalDocCheckConfig, attributes).parse()