__author__ = 'Donald'

import xml.sax
import AppClientConfig


class SampleContentHandler(xml.sax.ContentHandler):

    def __init__(self, visitDepth=1, depthStep=1):
        self.depth = 0
        self.subContent = []
        self.visitDepth = visitDepth
        self.depthStep = depthStep
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        if self.depth >= self.visitDepth:
            self.subContent.append("<%s>" % name)
        self.depth += self.depthStep

    def endElement(self, name):
        if self.depth >= self.visitDepth:
            self.subContent.append("</%s>" % name)
        self.depth -= self.depthStep
        if self.depth == self.visitDepth:
            self.__handleElement(name)
            self.subContent = []

    def characters(self, content):
        if self.depth >= self.visitDepth:
            self.subContent.append(content)

    def __handleElement(self, name):

        try:
            parserName = "%sParser" % self.__makeCapital(name)
            parserModule = __import__(parserName)
        except ImportError:
            pass
        else:
            try:
                parserClass1 = getattr(parserModule, parserName)
                parserClass = getattr(parserClass1, parserName)
            except AttributeError:
                pass
            else:
                parser = parserClass()
                xml.sax.parseString(''.join(self.subContent), parser)

    def __makeCapital(self, name):
        pieces = []
        pieces.append(name[0].upper())
        pieces.append(name[1:])
        return ''.join(pieces)

class AddressParser(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print("startElement: " + name)

    def endElement(self, name):
        print("endElement: " + name)

    def characters(self, content):
        print("characters: " + content)


def main(sourceFileName):
    source = open(sourceFileName)
    xml.sax.parse(source, SampleContentHandler())

if __name__ == "__main__":
    main("addressbook.xml")