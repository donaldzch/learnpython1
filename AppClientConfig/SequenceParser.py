__author__ = 'DonaldZhu'

from __init__ import *


class SequenceParser(AttributeParser):
    parserKey = 'SequenceParser'
    #attr: (parser, mandatory, extraParam)
    sequence = {}

    def __init__(self, configure, attributes):
        AttributeParser.__init__(self, configure, attributes, ConfigError(self.parserKey))

    def parse(self):
        AttributeParser.parse(self)
        for attr, (parser, mandatory, extraParam) in self.sequence.items():
            if mandatory:
                if self.configure.get(attr) is None:
                    raise ConfigError(self.parserKey, 'missing' + attr)
            if parser is not None:
                self._subParse(attr, parser, extraParam)

    def _subParse(self, attr, parser, extraParam):
        if self.configure.get(attr) is not None:
            self._getParser(attr, self.configure.get(attr), parser, extraParam).parse()

    def _getParser(self, attrName, attrValue, parser, extraParam):
        error = ConfigError(self.parserKey, 'invalid ' + attrName)
        if parser.__name__ == BooleanParser.__name__:
            return BooleanParser(attrValue, error)
        elif parser.__name__ == LongParser.__name__:
            return LongParser(attrValue, error)
        elif parser.__name__ == DateTimeParser.__name__:
            return DateTimeParser(attrValue, error)
        elif parser.__name__ == ScopeParser.__name__:
            return ScopeParser(self.parserKey, attrValue)
        elif parser.__name__ == AttributeParser.__name__:
            return AttributeParser(attrValue, extraParam, error)
        elif parser.__name__ == AllowedCollectionParser.__name__:
            return AllowedCollectionParser(attrValue, extraParam.get('allowedCollection'),
                                           self.parserKey, extraParam.get('attrName'))
        elif parser.__name__ == StringParser.__name__:
            return StringParser(attrValue, error)
        else:
            raise ConfigError("unknown parser", parser.__name__)