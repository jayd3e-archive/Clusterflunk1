from pyramid.view import view_config


@view_config(route_name='index', renderer='clusterflunk:templates/feed.mako')
def feed(request):
    return {}
