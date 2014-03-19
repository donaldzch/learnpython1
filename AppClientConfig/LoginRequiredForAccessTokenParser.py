__author__ = 'Donald'

from __init__ import *


def parse(loginRequiredForAccessToken):
    BooleanParser(loginRequiredForAccessToken, ConfigError('loginRequiredForAccessToken'))