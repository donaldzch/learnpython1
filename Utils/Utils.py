__author__ = 'Donald'

APP_CLIENT_CONFIG = "AppClientConfig"
APP_CLIENT_CONFIG_PARSER = "parse"

import importlib
import pkgutil


def getModule(moduleName):
    try:
        module = importlib.import_module(isinstance(moduleName, list) and '.'.join(moduleName) or moduleName)
    except ImportError:
        return None
    else:
        return module


def getClass(moduleName, className):
    module = getModule(moduleName)
    if module is not None:
        try:
            return getattr(module, className)
        except AttributeError:
            return None
    else:
        return None


def makeFirstCapital(word):
    return word[0].upper() + word[1:]


def getModules(packageName):
    return map(getModule, map(lambda module: [packageName, module],
               [module for loader, module, isPkg in pkgutil.iter_modules(path=[packageName]) if not isPkg]))


def getAppClientConfigModules():
    return getModules(APP_CLIENT_CONFIG)


def getAppClientConfigParsers():
    parsers = []
    for module in getAppClientConfigModules():
        try:
            parser = getattr(module, APP_CLIENT_CONFIG_PARSER)
        except AttributeError:
            pass
        else:
            parsers.append(parser)
    return parsers