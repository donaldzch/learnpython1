__author__ = 'Donald'

from __init__ import *


def parse(refreshTokenExpiration):
    LongParser(refreshTokenExpiration, 'refreshTokenExpiration').parse()
