__author__ = 'Donald'

from __init__ import *
import re

ATTRIBUTE_URI = "uri"
URI_REGEX_ANY = "*"


class _AllowedRedirectUrisParser(AttributeParser):
    parserKey = 'allowedRedirectUris'

    def __init__(self, configure, allowedUris, defaultUris, attributes):
        AttributeParser.__init__(self, configure, attributes)
        self.allowedUris = allowedUris
        self.regularUris = []
        self.regexUris = []
        self.defaultUris = defaultUris

    def _getRegexUris(self):
        self.regexUris = [uri for uri in self.allowedUris if URI_REGEX_ANY in uri]
        if len(self.regexUris):
            self.regexUris = map(lambda uri: uri.replace(".", "\\.").replace("?", "\\?").replace("*", ".*") + ".*",
                                 self.regexUris)
            for regexUri in self.regexUris:
                from urlparse import urlparse
                uriScheme = urlparse(regexUri).scheme
                if uriScheme == "http" or uriScheme == "https":
                    pass
                else:
                    raise ConfigError('allowedRedirectUris', regexUri)

    def _getRegularUris(self):
        self.regularUris = [uri for uri in self.allowedUris if URI_REGEX_ANY not in uri]

    def _validate(self, uriName, redirectUri):
        self._getRegexUris()
        self._getRegularUris()

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
            raise ConfigError(uriName, redirectUri)

    def parse(self):
        AttributeParser.parse(self)
        for uriName, uriValue in self.defaultUris.items():
            if uriValue is not None:
                self._validate(uriName, uriValue)


def parse(allowedRedirectUris, extraParams, attributes):
    try:
        allowedUris = allowedRedirectUris[ATTRIBUTE_URI]
    except KeyError:
        pass
    else:
        _AllowedRedirectUrisParser(allowedRedirectUris, allowedUris, extraParams, attributes).parse()