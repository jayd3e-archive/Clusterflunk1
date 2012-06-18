from pyramid.view import view_config


@view_config(route_name='groups', renderer='clusterflunk:templates/groups/groups.mako')
def groups(request):
    return {}


@view_config(route_name='group', renderer='clusterflunk:templates/groups/group.mako')
def group(request):
    return {}


@view_config(route_name='groups_create', renderer='clusterflunk:templates/groups/create.mako')
def create(request):
    return {}
