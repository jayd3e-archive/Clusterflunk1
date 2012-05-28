from datetime import datetime
from pyramid.view import view_config
from clusterflunk.models.statuses import Status
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
                    body=body,
                    author_id=user.id)
    db.add(status)
    db.flush()

    for chosen_group_id in chosen_groups:
        broadcast = Broadcast(status_id=status.id,
                              study_group_id=chosen_group_id)
        db.add(broadcast)

    db.flush()
    return {'id': status.id,
            'body': status.body,
            'username': user.username}
