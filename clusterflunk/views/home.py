from pyramid.view import view_config

@view_config(
    route_name='home',
    renderer='clusterflunk:templates/index.mako')
def home_view(request):
    return {}
