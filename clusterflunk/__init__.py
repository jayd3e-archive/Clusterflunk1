from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy

from clusterflunk.security import (
    AuthenticationPolicy,
    root_factory,
)

def main(global_config, **settings):
    '''Main config function'''
    authn_policy = AuthenticationPolicy(settings)
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy,
        root_factory=root_factory,
    )
    config.add_static_view('static', 'clusterflunk:static/')
    config.add_route('home', '/')
    config.add_route('api.login', '/api/login')
    config.add_route('api.logout', '/api/logout')
    config.scan('clusterflunk.views')
    return config.make_wsgi_app()
