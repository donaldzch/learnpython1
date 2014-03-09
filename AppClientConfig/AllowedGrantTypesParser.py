__author__ = 'Donald'

from CollectionParser import CollectionParser


class _AllowedGrantTypesParser(CollectionParser):
    collections = ("authorization_code", "refresh_token", "exchange", "password", "client_credentials")

    def __init__(self, config, name, error):
        CollectionParser.__init__(self, config and config['grantType'] or None, name, error)


def parse(appClient):
    print ("allowGrantTypes")
    _AllowedGrantTypesParser(appClient["allowedGrantTypes"], 'allowedGrantTypes', 'Invalid Grant Type').parse()