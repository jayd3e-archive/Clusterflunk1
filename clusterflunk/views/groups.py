from pyramid.view import view_config


@view_config(route_name='groups', renderer='clusterflunk:templates/groups/index.mako')
def index(request):
    return {}


@view_config(route_name='groups_view', renderer='clusterflunk:templates/groups/view.mako')
def view(request):
    return {}


@view_config(route_name='groups_create', renderer='clusterflunk:templates/groups/create.mako')
def create(request):
    return {}
