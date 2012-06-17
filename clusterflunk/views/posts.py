from pyramid.view import view_config


@view_config(route_name='posts', renderer='clusterflunk:templates/posts/index.mako')
def index(request):
    return {}


@view_config(route_name='posts_view', renderer='clusterflunk:templates/posts/view.mako')
def view(request):
    return {}


@view_config(route_name='posts_create', renderer='clusterflunk:templates/posts/create.mako')
def create(request):
    return {}
