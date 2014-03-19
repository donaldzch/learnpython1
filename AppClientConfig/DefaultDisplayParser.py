__author__ = 'Donald'

from __init__ import *


class _DefaultDisplayParser(CollectionParser):
    collections = ("origin_store", "xbox360", "origin_client", "fifa_mobile",
                   "web/create", "web/login", "pc/create", "pc/login", "lockbox/create",
                   "lockbox/login", "mobile/login", "mobilegame/login", "console/welcome",
                   "console2/welcome")
    parserKey = 'defaultDisplay'


def parse(defaultDisplay):
    _DefaultDisplayParser(defaultDisplay).parse()
