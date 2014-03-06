__author__ = 'Donald'

import AppClientAttribute
from urlparse import urlparse
import re

ATTRIBUTE_URI = "uri"
URI_REGEX_ANY = "*"


class _AllowedRedirectUrisParser(object):

    def __init__(self, allowedUris):
        self.allowedUris = allowedUris
        self.regularUris = []
        self.regexUris = []

    def _getRegexUris(self):
        self.regexUris = [uri for uri in self.allowedUris if URI_REGEX_ANY in uri]
        if len(self.regexUris):
            self.regexUris = map(lambda uri: uri.replace(".", "\\.").replace("?", "\\?").replace("*", ".*") + ".*",
                                 self.regexUris)
            for regexUri in self.regexUris:
                uriScheme = urlparse(regexUri).scheme
                if uriScheme == "http" or uriScheme == "https":
                    pass
                else:
                    raise AttributeError

    def _getRegularUris(self):
        self.regularUris = [uri for uri in self.allowedUris if URI_REGEX_ANY not in uri]

    def prepare(self):
        self._getRegexUris()
        self._getRegularUris()
        return self

    def validate(self, redirectUri):
        allowed = False
        for regexUri in self.regexUris:
            if re.match(regexUri, redirectUri):
                allowed = True
                break
        if not allowed:
            for regularUri in self.regularUris:
                if redirectUri.startswith(regularUri):
                    allowed = True
                    break
        if not allowed:
            raise AttributeError()


def _validateUri(parser, item, key):
    try:
        redirectUri = item[key]
    except KeyError:
        pass
    else:
        parser.validate(redirectUri)


def parse(appClientDict):
    try:
        allowedUris = appClientDict[AppClientAttribute.ALLOWED_REDIRECT_URIS][ATTRIBUTE_URI]
    except KeyError:
        pass
    else:
        parser = _AllowedRedirectUrisParser(allowedUris).prepare()
        _validateUri(parser, appClientDict, AppClientAttribute.DEFAULT_REDIRECT_URI)
        _validateUri(parser, appClientDict, AppClientAttribute.DEFAULT_REDIRECT_URI_FOR_LOGOUT)