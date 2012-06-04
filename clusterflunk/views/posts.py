from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from clusterflunk.models.posts import (
    Post,
    PostHistory
)
from clusterflunk.forms import CreatePostForm


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


@view_config(
    route_name='posts_create',
    renderer='clusterflunk:templates/posts/create.mako',
    permission='view')
def create(request):
    db = request.db
    user = request.user

    study_group_choices = [(g.id, g.name) for g in user.subscribed_groups]

    post_create_form = CreatePostForm(request.POST)
    post_create_form.study_group.choices = study_group_choices
    if 'study_group' in request.GET:
        post_create_form.study_group.data = int(request.GET['study_group'])

    if request.method == 'POST' and post_create_form.validate():
        name = post_create_form.name.data
        description = post_create_form.description.data
        study_group_id = post_create_form.study_group.data

        post_rev = PostHistory(revision=1,
                               author=user,
                               created=datetime.now(),
                               name=name,
                               description=description)
        post = Post(created=datetime.now(),
                    founder=user,
                    history=[post_rev],
                    study_group_id=study_group_id)
        db.add(post)
        db.flush()
        return HTTPFound(location="/posts/%s" % str(post.id))

    return {'post_create_form': post_create_form}
