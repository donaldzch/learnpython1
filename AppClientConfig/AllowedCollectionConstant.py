__author__ = 'DonaldZhu'

ALLOWED_SCOPES_COLLECTIONS = ("basic.identity", "basic.twofactor", "basic.identity.write", "basic.persona",
                              "basic.persona.write", "basic.entitlement", "basic.entitlement.write",
                              "basic.encrypted_token", "basic.admin", "basic.utility", "basic.domaindata",
                              "basic.delegatetoken", "basic.xbltoken", "openid", "signin", "offline", "search.identity",
                              "server.search.identity", "service.atom", "basic.catalog", "basic.catalog.write",
                              "basic.anonymous.migration", "basic.migration.record",
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

ALLOWED_USER_STATUS = ('ACTIVE', 'VOLATILE', 'TENTATIVE',
                       'CHILD_APPROVED',
                       'CHILD_PENDING', 'PENDING',
                       'DISABLED', 'BANNED')

ALLOWED_PERSONA_STATUS = ('ACTIVE', 'PENDING', 'BANNED')

PID_ID_STATE = ('anyone', 'no_one', 'specific_one')

ENTITLEMENT_CHECK_TYPE = ('periodTrial', 'standard', 'timedTrial')

ENTITLEMENT_TYPE = ('ONLINE_ACCESS', 'TRIAL_ONLINE_ACCESS', 'SUBSCRIPTIONS', 'PARENTAL_APPROVAL', 'DEFAULT')

ALLOWED_DISPLAYS = ("origin_store", "xbox360", "origin_client", "fifa_mobile", "web/create",
                    "web/login", "pc/create", "pc/login", "lockbox/create",
                    "lockbox/login", "mobile/login", "mobilegame/login", "console/welcome",
                    "console2/welcome", "console3/welcome")

ALLOWED_GRANT_TYPES = ('authorization_code', 'refresh_token', 'exchange', 'password', 'client_credentials')

ALLOWED_MOBILE_LOGIN_TYPES = ('origin', 'mobile_game_UPID', 'mobile_game_facebook', 'mobile_game_origin',
                              'mobile_game_game_center', 'mobile_game_google_plus')

USER_ID_STATE = ('anyone', 'no_one')

ALLOWED_RESPONSE_TYPES = ('code', 'token', 'id_token')

SERVICE_SCOPES = ('service.identity', 'service.atom', 'service.fifa-server', 'service.orginsdk2')

THROTTLE_ACCESS_STATE = ('allowed', 'denied', 'controlled')

UNIVERSE = ("default", "integration", "lt", "lt-rs", "lt-sh", "production")