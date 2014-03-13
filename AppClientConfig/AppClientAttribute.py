__author__ = 'Donald'

APP_CLIENT = "appClient"
ALLOWED_REDIRECT_URIS = "allowedRedirectUris"
DEFAULT_REDIRECT_URI = "defaultRedirectUri"
DEFAULT_REDIRECT_URI_FOR_LOGOUT = "defaultRedirectUriForLogout"

appClient = {
    #name: (module, extra params, attributes)
    'clientId': (None, None, None),
    'clientSecret': (None, None, None),
    'universe': ('UniverseParser', None, None),
    'accessTokenExpiration': ('AccessTokenExpirationParser', None, None),
    'allowedAuthenticationSources': ('AllowedAuthenticationSourcesParser',
                                     ['defaultAuthenticationSource'], 'authenticationSource'),
    'defaultAuthenticationSource': (None, None, None),
    'allowedClientIds': ('AllowedClientIdsParser', None, 'clientId'),
    'allowedDisplays': ('AllowedDisplaysParser', 'defaultDisplay', 'displayType'),
    'allowedGrantTypes': ('AllowedGrantTypesParser', None, 'grantType'),
    'allowedRedirectUris': ('AllowedRedirectUrisParser', ['defaultRedirectUri', 'defaultRedirectUriForLogout'], 'uri'),
    'allowedMobileLoginTypes': ('AllowedMobileLoginTypesParser', None, 'mobileLoginType'),
    'allowedResponseTypes': ('AllowedResponseTypesParser', None, 'responseType'),
    'allowedRegistrationSources': ('AllowedRegistrationSourcesParser',
                                   ['defaultAuthenticationSource'], 'registrationSource'),
    'allowedScopes': ('AllowedScopesParser', ['defaultScopes'], 'scope'),
    'defaultRedirectUri': (None, None, None),
    'defaultRedirectUriForLogout': (None, None, None),
    'apiIpWhitelists': ('ApiIpWhistlistsParser', None, [''])
}