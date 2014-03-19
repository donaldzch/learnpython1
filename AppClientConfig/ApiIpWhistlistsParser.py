__author__ = 'Donald'

from __init__ import *

"""
<apiIpWhitelists>
    <apiIpWhitelist>
        <apiName>pid_get</apiName>
        <apiIpWhitelistConfig>
            <ips>
                <ip>10.88.1.1</ip>
            </ips>
        </apiIpWhitelistConfig>
    </apiIpWhitelist>
</apiIpWhitelists>
"""


class _ApiIpWhitelistConfigParser(SequenceParser):
    sequence = {
        'ips': (AttributeParser, True, ['ip'])
    }
    parserKey = 'apiIpWhitelistConfig'


class _ApiIpWhitelistParser(SequenceParser):
    sequence = {
        'apiName': (StringParser, True, None),
        'apiIpWhitelistConfig': (_ApiIpWhitelistConfigParser, True, ['ips'])
    }
    parserKey = 'apiIpWhitelist'


class _ApiIpWhitelistsParser(ListParser):

    def __init__(self, apiIpWhitelists, attributes):
        ListParser.__init__(self, listConfig=apiIpWhitelists, attributes=attributes,
                            parser=_ApiIpWhitelistParser)


def parse(apiIpWhitelists, attributes):
    _ApiIpWhitelistsParser(apiIpWhitelists, attributes).parse()