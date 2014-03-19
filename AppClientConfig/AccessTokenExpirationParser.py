__author__ = 'Donald'

from __init__ import *


def parse(accessTokenExpiration):
    LongParser(accessTokenExpiration, ConfigError('accessTokenExpiration', 'invalid expiration')).parse()
