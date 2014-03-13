__author__ = 'Donald'

from __init__ import *


def parse(accessTokenExpiration):
    try:
        long(accessTokenExpiration)
    except ValueError:
        raise ConfigError("accessTokenExpiration", "invalid expiration")
