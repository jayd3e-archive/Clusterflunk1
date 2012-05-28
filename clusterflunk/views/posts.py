from pyramid.view import view_config
from clusterflunk.models.posts import Post


@view_config(
    route_name='posts',
    renderer='clusterflunk:templates/posts/index.mako',
    permission='view')
def index(request):
    db = request.db
    user = request.user
    study_group_ids = []
    for study_group in user.subscribed_groups:
        study_group_ids.append(study_group.id)

    if study_group_ids:
        query = db.query(Post).filter(Post.study_group_id.in_(study_group_ids))
        query = query.order_by(Post.created)
        posts = query.all()
    else:
        posts = []

    return {'posts': posts}


@view_config(
    route_name='posts_view',
    renderer='clusterflunk:templates/posts/view.mako',
    request_method='GET',
    permission='view')
def view(request):
    db = request.db
    post_id = request.matchdict.get('post_id')

    post = db.query(Post).filter_by(id=post_id).first()
    latest_rev = len(post.history) - 1
    return {'post': post,
            'latest_rev': latest_rev}
