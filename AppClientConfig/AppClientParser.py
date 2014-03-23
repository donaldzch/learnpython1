__author__ = 'Donald'


from __init__ import *


def _getExtraParams(appClientDict, paramNames):
    params = dict()
    for paramName in paramNames:
        if paramName in appClientDict.keys():
            params[paramName] = appClientDict.get(paramName)
    return params


def parse(appClientDict):
    exceptions = []
    appClientDict = appClientDict.get('appClient')
    if appClientDict is None:
        return 'unknown Client', ['invalid appClient']
    for key in appClientDict.keys():
        if appClientDict.get(key) is None:
            continue
        try:
            (moduleName, extraParamNames, attributes) = AppClientAttribute.appClient.get(key)
            if moduleName is not None:
                module = Utils.getModule([Utils.APP_CLIENT_CONFIG, moduleName])
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
        except ConfigError as CE:
            exceptions.extend(["config error: " + key + " | " + str(CE)])
        except Exception as EX:
            exceptions.extend(["exception: " + key + " | " + EX.message])
    return appClientDict.get('clientId'), exceptions