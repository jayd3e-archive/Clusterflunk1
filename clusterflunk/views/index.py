from pyramid.view import view_config

@view_config(
    route_name='index',
    renderer='clusterflunk:templates/index.mako',
    permission='view')
def index(request):
    return {}
