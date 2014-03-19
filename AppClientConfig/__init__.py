__author__ = 'Donald'

from Utils import Utils
from Utils import XMLConverter
from Error.ConfigError import ConfigError

ALLOWED_SCOPES_COLLECTIONS = ("basic.identity", "basic.twofactor", "basic.identity.write", "basic.persona",
                              "basic.persona.write", "basic.entitlement", "basic.entitlement.write",
                              "basic.encrypted_token", "basic.admin", "basic.utility", "basic.domaindata",
                              "basic.delegatetoken", "basic.xbltoken", "openid", "signin", "offline", "search.identity",
                              "server.search.identity", "service.atom", "basic.catalog", "basic.catalog.write",
                              "basic.anonymous.migration",
                              "basic.catalog.int", "basic.catalog.write.int", "service.fifa-server", "service.originsdk2",
                              "basic.commerce", "basic.commerce.write","basic.billing","basic.billing.write",
                              "basic.keymaster", "basic.keymaster.write", "bulk.identity", "basic.migration", "bytevault",
                              "basic.commerce.console", "basic.commerce.console.write", "basic.privilege",
                              "basic.psntoken", "basic.securityqa.read", "basic.securityqa.write",
                              "gos_tools_user", "gos_tools_admin", "gos_tools_server_admin", "gos_tools_super_admin",
                              "gos_bytevault_admin_service", "gos_achievements_global_admin", "gos_pas_admin",
                              "gos_oa_admin", "gos_achievements_post", "gos_achievements_user_level_admin",
                              "gos_achievements_product_level_admin", "gos_achievements_enduser", "gos_notify_post_event",
                              "gos_notify_get_event", "gos_notify_admin", "gos_friends_enduser", "gos_friends_integrator",
                              "gos_friends_fromxmpp", "gos_group_integrator")


import AppClientAttribute
from CollectionParser import CollectionParser
from AttributeParser import AttributeParser
from AllowedCollectionParser import AllowedCollectionParser
from BasicParser import BasicParser
from LongParser import LongParser
from BooleanParser import BooleanParser
from StringParser import StringParser
from ScopeParser import ScopeParser
from DateTimeParser import DateTimeParser
from ListParser import ListParser
from SequenceParser import SequenceParser



