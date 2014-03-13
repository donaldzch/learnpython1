__author__ = 'Donald'


from __init__ import *


def _getExtraParams(appClientDict, paramNames):
    params = dict()
    for paramName in paramNames:
        if paramName in appClientDict.keys():
            params[paramName] = appClientDict.get(paramName)
    return params


def parse(appClientDict):
    for key in appClientDict.keys():
        if appClientDict.get(key) is None:
            continue
        try:
            (moduleName, extraParamNames, attributes) = AppClientAttribute.appClient.get(key)
            if moduleName is not None:
                module = Utils.getModule(moduleName)
                if extraParamNames is not None:
                    extraParams = _getExtraParams(appClientDict, extraParamNames)
                    if attributes is not None:
                        module.parse(appClientDict.get(key), extraParams, attributes)
                    else:
                        module.parse(appClientDict.get(key), extraParams)
                else:
                    if attributes is not None:
                        module.parse(appClientDict.get(key), attributes)
                    else:
                        module.parse(appClientDict.get(key))
        except TypeError as TE:
            print "typeerror: " + key + " | " + TE.message
        except AttributeError as AE:
            print "attribute Error: " + key + "| " + AE.message
        except ConfigError as CE:
            print "config error: " + key + "| " + str(CE)

if __name__ == "__main__":
    clientDict = XMLConverter.toDict(file("../addressbook.xml"))
    parse(clientDict['appClient'])