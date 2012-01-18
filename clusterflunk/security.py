import logging
import os

from pyramid.authentication import AuthTktCookieHelper
from pyramid.security import (
    Allow,
    Authenticated,
    Deny,
    Everyone,
)

log = logging.getLogger(__name__)

class AuthenticationPolicy(object):
    def __init__(self, settings):
        secret = settings.get('auth.secret')
        if secret is None:
            secret = ''.join('%02x' % ord(x) for x in os.urandom(16))
            log.warn('Using randomly generated cookie secret because none '
                     'could be found in the settings: %s', secret)

        self.cookie = AuthTktCookieHelper(
            secret,
            http_only=True,
        )

    def unauthenticated_userid(self, request):
        return self.cookie.identify(request)

    def authenticated_userid(self, request):
        return self.unauthenticated_userid(request)

    def effective_principals(self, request):
        principals = [Everyone]
        userid = self.authenticated_userid(request)
        if userid is not None:
            principals += [Authenticated, 'u:%s' % userid]
        return principals

    def forget(self, request):
        return self.cookie.forget(request)

    def remember(self, request, userid, **kw):
        return self.cookie.remember(request, userid, **kw)

class Root(object):
    __acl__ = [
        (Allow, Authenticated, 'logged_in'),
    ]

def root_factory(request):
    return Root()
