__author__ = 'Donald'

from __init__ import *


def parse(idTokenExpiration):
    LongParser(idTokenExpiration, ConfigError('idTokenExpiration', 'invalid expiration')).parse()
