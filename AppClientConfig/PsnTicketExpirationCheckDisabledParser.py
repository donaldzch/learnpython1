__author__ = 'DonaldZhu'

from __init__ import *


def parse(psnTicketExpirationCheckDisabled):
    BooleanParser(psnTicketExpirationCheckDisabled, ConfigError('psnTicketExpirationCheckDisabled')).parse()