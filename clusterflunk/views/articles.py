from pyramid.view import view_config

@view_config(
    route_name='articles',
    renderer='clusterflunk:templates/articles/index.mako',
    permission='view')
def index(request):
    return {}
