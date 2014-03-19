__author__ = 'Donald'

from __init__ import *


def parse(refreshTokenExpiration):
    LongParser(refreshTokenExpiration, ConfigError('refreshTokenExpiration', 'invalid expiration')).parse()
