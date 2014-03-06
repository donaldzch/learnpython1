__author__ = 'Donald'

import xml.sax
from Utils import Utils


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

        parserName = "%sParser" % Utils.makeFirstCapital(name)
        parser = Utils.getClass("AppClientConfig." + parserName, parserName)
        if parser is not None:
            xml.sax.parseString(''.join(self.subContent), parser())


def main(sourceFileName):
    source = open(sourceFileName)
    xml.sax.parse(source, SampleContentHandler())

if __name__ == "__main__":
    main("addressbook.xml")