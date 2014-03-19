__author__ = 'Donald'

from __init__ import *


def parse(secretExpireBy):
    DateTimeParser(secretExpireBy, 'secretExpireBy').parse()