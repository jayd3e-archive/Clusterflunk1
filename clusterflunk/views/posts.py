from pyramid.view import view_config


@view_config(route_name='index', renderer='clusterflunk:templates/posts/posts.mako')
@view_config(route_name='posts', renderer='clusterflunk:templates/posts/posts.mako')
def posts(request):
    return {}


@view_config(route_name='post', renderer='clusterflunk:templates/posts/post.mako')
def post(request):
    return {}
