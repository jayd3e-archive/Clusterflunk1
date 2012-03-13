from pyramid.view import view_config
from clusterflunk.models.group import Group

@view_config(
    route_name='groups',
    renderer='clusterflunk:templates/groups/index.mako',
    permission='view')
def index(request):
    db = request.db
    groups = db.query(Group).filter_by(network_id=)
    return {'groups':groups}
