from pyramid.view import view_config
from clusterflunk.models.posts import Post

@view_config(
    route_name='index',
    renderer='clusterflunk:templates/index.mako',
    permission='view')
def index(request):
    db = request.db

    posts = db.query(Post).all()
    return {'posts':posts}