from pyramid.view import view_config
from clusterflunk.models.posts import Post

@view_config(
    route_name='profile',
    renderer='clusterflunk:templates/profile/index.mako',
    permission='view')
def index(request):
    user = request.user
    
    return {'user':user}