__author__ = 'Donald'

from Utils import XMLConverter
from Utils import Utils

APP_CLIENT = "appClient"


def load(input):
    clientDict = XMLConverter.toDict(input)[APP_CLIENT]
    for parser in Utils.getAppClientConfigParsers():
        parser(clientDict)
    #print XMLConverter.toJson(clientDict, 3)

if __name__ == "__main__":
    load(file("addressbook.xml"))
