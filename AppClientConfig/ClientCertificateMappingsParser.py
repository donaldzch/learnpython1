__author__ = 'Donald'

"""
<clientCertificateMappings>
    <clientCertificateMapping>
        <certificateSubject>123456</certificateSubject>
        <certificateIssuer>123456</certificateIssuer>
    </clientCertificateMapping>
    <clientCertificateMapping>
        <certificateSubject>123456</certificateSubject>
        <certificateIssuer>123456</certificateIssuer>
    </clientCertificateMapping>
</clientCertificateMappings>
"""

from __init__ import *


class _ClientCertificateMappings(ListParser):
    parserKey = 'clientCertificateMapping'

    def __init__(self, mappings, attributes):
        ListParser.__init__(self, listConfig=mappings, attributes=attributes,
                            parser=_ClientCertificateMapping, parserAttr=['certificateSubject', 'certificateIssuer'])


class _ClientCertificateMapping(SequenceParser):
    parserKey = 'clientCertificateMapping'
    sequence = {
        'certificateSubject': (StringParser, True, None),
        'certificateIssuer': (StringParser, True, None)
    }


def parse(clientCertificateMappings, attributes):
    _ClientCertificateMappings(clientCertificateMappings, attributes).parse()