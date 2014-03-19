__author__ = 'Donald'

from __init__ import *


class _DefaultDisplayParser(CollectionParser):
    allowedCollection = ("origin_store", "xbox360", "origin_client", "fifa_mobile",
                                         "web/create", "web/login", "pc/create", "pc/login", "lockbox/create",
                                         "lockbox/login", "mobile/login", "mobilegame/login", "console/welcome",
                                         "console2/welcome")

    def __init__(self, value):
        CollectionParser.__init__(self, self.allowedCollection, ConfigError("defaultDisplay"))
        self.value = value

    def parse(self):
        CollectionParser.parse(self, self.value)


def parse(defaultDisplay):
    _DefaultDisplayParser(defaultDisplay).parse()
