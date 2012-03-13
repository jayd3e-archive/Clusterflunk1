from pyramid.view import view_config
from clusterflunk.models.posts import Post

@view_config(
    route_name='index',
    renderer='clusterflunk:templates/index.mako',
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
    return {'posts':posts}