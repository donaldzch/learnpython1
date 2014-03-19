__author__ = 'Donald'

"""
<ipWhitelists>
    <ip>192.168.1.1</ip>
</ipWhitelists>
"""

from __init__ import *


def parse(ipWhitelists, attributes):
    AttributeParser(ipWhitelists, attributes, ConfigError('ipWhitelists')).parse()