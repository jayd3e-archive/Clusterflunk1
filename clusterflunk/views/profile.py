from pyramid.view import view_config
from clusterflunk.models.users import User


@view_config(
    route_name='profile',
    renderer='clusterflunk:templates/profile/index.mako',
    permission='view')
def index(request):
    db = request.db
    user = db.query(User).filter_by(username=request.matchdict['username']).first()
    return {'user': user}
