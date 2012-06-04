from pyramid.view import view_config
from clusterflunk.models.users import User


@view_config(
    route_name='users',
    renderer='json',
    permission='view',
    request_param='s')
def search(request):
    db = request.db
    s = request.GET['s']

    users_json = []
    users = db.query(User).filter(User.username.like('%' + s + '%'))
    for user in users:
        users_json.append({
            'id': user.id,
            'username': user.username
        })
    return users_json
