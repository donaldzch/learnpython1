__author__ = 'Donald'

"""
    <externalStyleSheets>
        <source>https:////afdasf</source>
    </externalStyleSheets>
"""

from __init__ import *


def parse(externalStyleSheets, attributes):
    AttributeParser(externalStyleSheets, attributes, ConfigError('externalStyleSheets')).parse()