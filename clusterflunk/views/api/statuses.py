from datetime import datetime
from pyramid.view import view_config
from clusterflunk.models.statuses import (
    Status,
    StatusHistory
)
from clusterflunk.models.broadcasts import Broadcast


@view_config(
    route_name='statuses',
    renderer='json',
    request_method='POST',
    permission='view')
def add(request):
    db = request.db
    user = request.user

    chosen_groups = request.json_body['chosen_groups']
    body = request.json_body['body']

    status = Status(created=datetime.now(),
                    founder_id=user.id)
    status_rev = StatusHistory(revision=1,
                               author_id=user.id,
                               status_id=status.id,
                               created=datetime.now(),
                               body=body)

    status.history.append(status_rev)
    db.add(status)
    db.flush()

    for chosen_group_id in chosen_groups:
        broadcast = Broadcast(status_id=status.id,
                              study_group_id=chosen_group_id)
        db.add(broadcast)

    db.flush()
    return {'id': status.id,
            'body': status.history[0].body,
            'username': user.username,
            'created_timedelta': status.created_timedelta}
