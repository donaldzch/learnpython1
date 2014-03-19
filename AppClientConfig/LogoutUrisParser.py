__author__ = 'Donald'

"""
<uri>http://localhost/clear/sid</uri>
<uri>http://localhost/logout</uri>
"""

from __init__ import *


class _LogoutUrisParser(AttributeParser):
    attrError = ConfigError('logoutUris')


def parse(logoutUris, attributes):
    _LogoutUrisParser(logoutUris, attributes).parse()