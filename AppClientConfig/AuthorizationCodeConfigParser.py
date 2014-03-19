__author__ = 'Donald'

from __init__ import *


class _AuthorizationCodeConfigParser(SequenceParser):
    sequence = {
        'redirectUriCheck': (BooleanParser, True, None)
    }
    parserKey = 'authorizationCodeConfig'


def parse(authorizationCodeConfg, attributes):
    _AuthorizationCodeConfigParser(authorizationCodeConfg, attributes).parse()