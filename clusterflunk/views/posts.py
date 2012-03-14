from pyramid.view import view_config
from clusterflunk.models.posts import Post

@view_config(
    route_name='posts_view',
    renderer='clusterflunk:templates/posts/view.mako',
    permission='view')
def view(request):
    db = request.db
    user = request.user
    post_id = request.matchdict.get('post_id')

    post = db.query(Post).filter_by(id=post_id).first()
    latest_rev = len(post.history) - 1
    return {'post': post,
            'latest_rev': latest_rev}