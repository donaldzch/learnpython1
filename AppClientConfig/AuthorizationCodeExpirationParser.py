__author__ = 'Donald'

from __init__ import *


def parse(authorizationCodeExpiration):
    LongParser(authorizationCodeExpiration, ConfigError('authorizationCodeExpiration', 'invalid expiration')).parse()

