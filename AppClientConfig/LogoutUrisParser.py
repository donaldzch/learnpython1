__author__ = 'Donald'

"""
<uri>http://localhost/clear/sid</uri>
<uri>http://localhost/logout</uri>
"""

from __init__ import *


def parse(logoutUris, attributes):
    AttributeParser(logoutUris, attributes, 'logoutUris').parse()