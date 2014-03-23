__author__ = 'Donald'

"""
<passwordConfig>
    <userIPHeaderEnabled>true</userIPHeaderEnabled>
</passwordConfig>
"""

from __init__ import *


class _PasswordConfigParser(SequenceParser):
    sequence = {
        'userIPHeaderEnabled': (BooleanParser, True, None),
        'allowedReferers': (AttributeParser, False, ['referer']),
        'captchaHeaderEnabled': (BooleanParser, False, None)
    }
    parserKey = 'passwordConfig'

    def __init__(self, configure, attributes, extraParams):
        SequenceParser.__init__(self, configure, attributes)
        self.grantTypeParser = CollectionParser(collection='password',
                                                collections=extraParams.get('allowedGrantTypes').get('grantType'),
                                                parserKey='passwordConfig',
                                                errorMsg='missing password grant type')

    def parse(self):
        SequenceParser.parse(self)
        self.grantTypeParser.parse()


def parse(passwordConfig, extraParams, attributes):
    _PasswordConfigParser(passwordConfig, attributes, extraParams).parse()