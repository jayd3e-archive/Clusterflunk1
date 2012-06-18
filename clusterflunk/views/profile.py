from pyramid.view import view_config


@view_config(route_name='profile', renderer='clusterflunk:templates/profile/index.mako')
def profile(request):
    return {}
