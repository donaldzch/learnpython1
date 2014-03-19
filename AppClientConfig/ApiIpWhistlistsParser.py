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


class _ApiIpWhitelistsParser(ListParser):

    def __init__(self, apiIpWhitelists, attributes):
        ListParser.__init__(self, listConfig=apiIpWhitelists, attributes=attributes,
                            parser=_ApiIpWhitelistParser, parserAttr=['apiName', 'apiIpWhitelistConfig'])


class _ApiIpWhitelistParser(SequenceParser):
    sequence = {
        'apiName': (StringParser, True, None),
        'apiIpWhitelistConfig': (None, True, None)
    }
    parserKey = 'apiIpWhitelist'

    def parse(self):
        SequenceParser.parse(self)
        _ApiIpWhitelistConfigParser(self.configure.get('apiIpWhitelistConfig'), ['ips']).parse()


class _ApiIpWhitelistConfigParser(SequenceParser):
    sequence = {
        'ips': (AttributeParser, True, ['ip'])
    }
    parserKey = 'apiIpWhitelistConfig'


def parse(apiIpWhitelists, attributes):
    _ApiIpWhitelistParser(apiIpWhitelists, attributes).parse()