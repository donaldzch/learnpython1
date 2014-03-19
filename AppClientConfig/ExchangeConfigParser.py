__author__ = 'Donald'

"""
<exchangeConfig>
    <trustedClients>
        <clientId>Fusion</clientId>
    </trustedClients>
</exchangeConfig>
"""

from __init__ import *


class _ExchangeConfigParser(SequenceParser):
    sequence = {
        'trustedClients': (AttributeParser, True, 'clientId')
    }
    parserKey = 'exchangeConfig'


def parse(exchangeConfig, attributes):
    _ExchangeConfigParser(exchangeConfig, attributes).parse()