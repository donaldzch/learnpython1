__author__ = 'Donald'

"""
        <optin>1234</optin>
        <optin>12345</optin>
"""

from __init__ import *


def parse(preferenceOptins, attributes):
    AttributeParser(preferenceOptins, attributes, 'preferenceOptins').parse()