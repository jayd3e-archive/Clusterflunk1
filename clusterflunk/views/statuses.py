from datetime import datetime
from pyramid.view import view_config
from clusterflunk.models.statuses import Status

@view_config(
    route_name='statuses',
    renderer='json',
    request_method='POST',
    permission='view')
def add(request):
    db = request.db
    user = request.user

    status = request.POST['status']

    status = Status(created=datetime.now(),
                    body=status,
                    author_id=user.id)
    db.add(status)
    db.flush()
    return {'id':status.id,
            'body':status.body,
            'username':user.username}