from pyramid.view import view_config

@view_config(
    route_name='groups',
    renderer='clusterflunk:templates/groups/index.mako',
    permission='view')
def index(request):
    db = request.db
    user = request.user

    study_groups = []
    for membership in user.memberships:
        study_groups.extend(membership.study_groups)
    return {'groups':study_groups}
