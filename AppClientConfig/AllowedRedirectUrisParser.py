__author__ = 'Donald'

from xml.sax import ContentHandler


class AllowedRedirectUrisParser(ContentHandler):

    def __init__(self):
        ContentHandler.__init__(self)

    def characters(self, *args, **kwargs):
        print(args, kwargs)