__author__ = 'Donald'

from __init__ import *


class _DeviceProfileCheckConfigParser(SequenceParser):
    sequence = {
        'enabled': (BooleanParser, True, None)
    }
    parserKey = 'deviceProfileCheckConfig'


def parse(deviceProfileCheckConfig, attributes):
    _DeviceProfileCheckConfigParser(deviceProfileCheckConfig, attributes).parse()