__author__ = 'Donald'

from __init__ import *


class _AllowedMobileLoginTypesParser(AllowedCollectionParser):
    allowedCollection = {"mobileLoginType": ('mobile_game_UPID', 'mobile_game_facebook', 'mobile_game_origin')}
    parserKey = 'allowedMobileLoginTypes'
    attrName = 'mobileLoginType'


def parse(allowedMobileLoginTypes, attributes):
    _AllowedMobileLoginTypesParser(allowedMobileLoginTypes, attributes).parse()