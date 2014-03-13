__author__ = 'Donald'

from __init__ import *


class _AllowedResponseTypesParser(AllowedCollectionParser):
    allowedCollection = {"responseType": ('code', 'token', 'id_token')}
    parserKey = 'allowedResponseTypes'
    attrName = 'responseType'


def parse(allowedResponseTypes, attributes):
    _AllowedResponseTypesParser(allowedResponseTypes, attributes).parse()