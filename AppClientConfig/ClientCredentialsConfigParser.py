__author__ = 'Donald'

"""
<clientCredentialsConfig>
        <pidIdState>anyone</pidIdState>
    </clientCredentialsConfig>
"""

from __init__ import *


class _ClientCredentialsConfigParser(SequenceParser):
    parserKey = 'clientCredentialsConfig'

    sequence = {
        'pidIdState': (CollectionParser, True, {'collections': AllowedCollectionConstant.PID_ID_STATE})
    }

    def __init__(self, config, extraParams, attributes):
        SequenceParser.__init__(self, config, attributes)
        self.grantTypeParser = CollectionParser(collection='client_credentials',
                                                collections=extraParams.get('allowedGrantTypes').get('grantType'),
                                                parserKey=self.parserKey,
                                                errorMsg='missing client_credentials grant type')

    def parse(self):
        SequenceParser.parse(self)
        self.grantTypeParser.parse()


def parse(clientCredentialsConfig, extraParams, attributes):
    _ClientCredentialsConfigParser(clientCredentialsConfig, extraParams, attributes).parse()