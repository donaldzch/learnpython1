__author__ = 'Donald'

"""
<enabled>true</enabled>
<allowedMigrationStatus>
    <status>completed</status>
    <status>started</status>
</allowedMigrationStatus>
<migrationClientIds>
    <clientId>migration_test_server</client>
</migrationClientIds>
"""

from __init__ import *


class _ClientMigrationConfigParser(SequenceParser):
    sequence = {
        'enabled': (BooleanParser, True, None),
        'allowedMigrationStatus': (AllowedCollectionParser, False,
                                   {'allowedCollection': ('completed', 'started'),
                                    'attrName': 'status'}),
        'migrationClientIds': (AttributeParser, False, 'clientId')
    }
    parserKey = 'clientMigrationConfig'


def parse(clientMigrationConfig, attributes):
    _ClientMigrationConfigParser(clientMigrationConfig, attributes).parse()