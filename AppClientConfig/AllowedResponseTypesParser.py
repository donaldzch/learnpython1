__author__ = 'Donald'

from __init__ import *


def parse(appClient):
    allowedResponseTypes = ("id_token", "token", "code")
    print ("allowedResponseTypes")
    try:
        responseTypes = appClient["allowedResponseTypes"]["responseType"]
    except KeyError:
        pass
    else:
        if Utils.containsAll(responseTypes, allowedResponseTypes):
            pass
        else:
            raise AttributeError()