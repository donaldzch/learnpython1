__author__ = 'Donald'

"""
<clientCredentialsConfig>
        <pidIdState>anyone</pidIdState>
    </clientCredentialsConfig>
"""

from __init__ import *


class _PidIdState(CollectionParser):
    def __init__(self, value):
        CollectionParser.__init__(self, ('anyone', 'no_one'), ConfigError('ClientCredentialsConfig', 'invalid pidIdState'))
        self.collection = value

    def parse(self):
        CollectionParser.parse(self, self.collection)


class _ClientCredentialsConfigParser(AttributeParser):
    attrError = ConfigError('ClientCredentialsConfig', 'invalid pidIdState')
    grantTypeError = ConfigError('clientCredentialsConfig', 'miss client_credentials')

    def __init__(self, config, extraParams, attributes):
        AttributeParser.__init__(self, config, attributes)
        self.grantTypes = extraParams.get('allowedGrantTypes')

    def parse(self):
        AttributeParser.parse(self)
        _PidIdState(self.configure.get('pidIdState')).parse()
        CollectionParser(self.grantTypes.get('grantType'), self.grantTypeError).parse('client_credentials')


def parse(clientCredentialsConfig, extraParams, attributes):
    _ClientCredentialsConfigParser(clientCredentialsConfig, extraParams, attributes).parse()