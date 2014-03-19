__author__ = 'Donald'

from __init__ import *


def parse(lastAuthDateUpdateCoolDown):
    LongParser(lastAuthDateUpdateCoolDown, ConfigError('lastAuthDateUpdateCoolDown', 'invalid expiration')).parse()
