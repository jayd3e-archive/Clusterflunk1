from pyramid.view import view_config


@view_config(
    route_name='profile',
    renderer='clusterflunk:templates/profile/index.mako',
    permission='view')
def index(request):
    user = request.user

    return {'user': user}
