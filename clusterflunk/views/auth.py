from pyramid.view import view_config


@view_config(route_name='login', renderer='clusterflunk:templates/auth/login.mako')
def login(request):
    return {}


@view_config(route_name='register', renderer='clusterflunk:templates/auth/register.mako')
def register(request):
    return {}
