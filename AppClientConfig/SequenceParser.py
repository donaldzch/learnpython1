__author__ = 'DonaldZhu'

from AttributeParser import AttributeParser
from Utils import Utils
from Error.ConfigError import ConfigError
from BasicParser import BasicParser
from ScopeParser import ScopeParser
from ListParser import ListParser
from AllowedCollectionParser import AllowedCollectionParser
from CollectionParser import CollectionParser


class SequenceParser(AttributeParser):
    parserKey = 'SequenceParser'
    #attr: (parser, mandatory, extraParam)
    sequence = {}

    def __init__(self, configure, attributes={}):
        self.attributes = attributes and attributes or Utils.getDictKeys(self.sequence)
        AttributeParser.__init__(self, configure, self.attributes, self.parserKey)

    def parse(self):
        AttributeParser.parse(self)
        for attr, (parser, mandatory, extraParam) in self.sequence.items():
            if mandatory:
                if self.configure.get(attr) is None:
                    raise ConfigError(self.parserKey, 'missing ' + attr)
            if parser is not None:
                self._subParse(attr, parser, extraParam)

    def _subParse(self, attr, parser, extraParam):
        if self.configure.get(attr) is not None:
            self._getParser(attr, self.configure.get(attr), parser, extraParam).parse()

    def _getParser(self, attrName, attrValue, parser, extraParam):
        if issubclass(parser, BasicParser):
            return parser(attrValue, attrName)
        elif parser.__name__ == ScopeParser.__name__:
            return ScopeParser(attrName, attrValue)
        elif parser.__name__ == AttributeParser.__name__:
            return AttributeParser(attrValue, extraParam, attrName)
        elif parser.__name__ == AllowedCollectionParser.__name__:
            return AllowedCollectionParser(attrValue, extraParam.get('allowedCollection'),
                                           attrName, extraParam.get('attrName'))
        elif parser.__name__ == CollectionParser.__name__:
            return CollectionParser(attrValue, extraParam.get('collections'), attrName)
        elif issubclass(parser, SequenceParser):
            return parser(attrValue, extraParam)
        elif issubclass(parser, ListParser):
            return parser(attrValue, extraParam)
        else:
            raise ConfigError("unknown parser", parser.__name__)