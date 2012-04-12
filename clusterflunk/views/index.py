from pyramid.view import view_config
from clusterflunk.models.statuses import Status
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.broadcasts import Broadcast

@view_config(
    route_name='index',
    renderer='clusterflunk:templates/index.mako',
    permission='view')
def index(request):
    db = request.db
    user = request.user
    study_group_ids = user.get_study_group_ids()

    if study_group_ids:
        query = db.query(Status).join(Broadcast, Status.id==Broadcast.status_id). \
                                 join(StudyGroup, Broadcast.study_group_id==StudyGroup.id). \
                                 filter(StudyGroup.id.in_(study_group_ids))
        statuses = query.all()
    else:
        statuses = []
    
    return {'statuses' : statuses}