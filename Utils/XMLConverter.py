__author__ = 'Donald'

from xml.parsers import expat

try:
    from collections import OrderedDict
except ImportError:
    try:
        from ordereddict import OrderedDict
    except ImportError:
        OrderedDict = dict


class _XMLToDictHandler():
    def __init__(self, visitDepth=0, dictConstructor=OrderedDict):
        self.tagDepth = 0
        self.visitDepth = visitDepth
        self.visitStack = []
        self.tagContent = None
        self.tagItem = None
        self.dictConstructor = dictConstructor

    def startElement(self, tagName, tagAttributes):
        self.tagDepth += 1
        if self.tagDepth > self.visitDepth:
            self.visitStack.append((self.tagItem, self.tagContent))
        self.tagItem = None
        self.tagContent = None
        self.startCharacter = True

    def endElement(self, tagName):
        if len(self.visitStack):
            currentTagItem, currentTagContent = self.tagItem, self.tagContent
            self.tagItem, self.tagContent = self.visitStack.pop()
            if currentTagContent is not None:
                currentTagContent = currentTagContent.strip() or None
            if currentTagItem is not None:
                self.tagItem = self.addDict(self.tagItem, tagName, currentTagItem)
            else:
                self.tagItem = self.addDict(self.tagItem, tagName, currentTagContent)
        else:
            self.tagItem = self.tagContent = None
        self.tagDepth -= 1
        self.startCharacter = False

    def characters(self, content):
        if self.startCharacter:
            if not self.tagContent:
                self.tagContent = content
            else:
                self.tagContent = self.tagContent + content

    def addDict(self, tagItem, tagName, tagContent):
        if tagItem is None:
            tagItem = self.dictConstructor()
        try:
            content = tagItem[tagName]
            if isinstance(content, list):
                content.append(tagContent)
            else:
                tagItem[tagName] = [content, tagContent]
        except KeyError:
            tagItem[tagName] = tagContent
        return tagItem


def toDict(inputSource, expat=expat, **kwargs):
    contentHandler = _XMLToDictHandler(**kwargs)

    xmlParser = expat.ParserCreate()

    try:
        xmlParser.ordered_attributes = True
    except AttributeError:
        pass
    xmlParser.StartElementHandler = contentHandler.startElement
    xmlParser.EndElementHandler = contentHandler.endElement
    xmlParser.CharacterDataHandler = contentHandler.characters

    try:
        xmlParser.ParseFile(inputSource)
    except TypeError as TE:
        print "T: " + TE.message
    except AttributeError as AE:
        print "A: " + AE.message
        xmlParser.Parse(inputSource, True)
    return contentHandler.tagItem


def toJson(inputSource, indent=1, **kwargs):
    import json
    return isinstance(inputSource, dict) and json.dumps(inputSource, indent=indent) \
        or json.dumps(toDict(inputSource, **kwargs), indent=indent)


if __name__ == '__main__':
    import os
    print os.stat("/Users/DonaldZhu/Desktop/appclient/default/bf4-client-kettle.xml")
    jsonStr = toJson(file("/Users/DonaldZhu/Desktop/appclient/default/bf4-client-kettle.xml"), 3)
    print jsonStr