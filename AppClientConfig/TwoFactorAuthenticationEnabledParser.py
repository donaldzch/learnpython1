__author__ = 'Donald'

from __init__ import *


def parse(twoFactorAuthEnabled):
    BooleanParser(twoFactorAuthEnabled, ConfigError('twoFactorAuthEnabled')).parse()