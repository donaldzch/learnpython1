__author__ = 'Donald'

from __init__ import *


class _AllowedClientIdsParser(AttributeParser):
    attrError = ConfigError('allowedClientIds', 'clientId')


def parse(allowedClientIds, attributes):
    _AllowedClientIdsParser(allowedClientIds, attributes).parse()