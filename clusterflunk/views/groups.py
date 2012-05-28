from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from clusterflunk.forms import CreateGroupForm
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.notifications import (
    GroupInviteNotification,
    Notification
)


@view_config(
    route_name='groups',
    renderer='clusterflunk:templates/groups/index.mako',
    permission='view')
def index(request):
    user = request.user
    category = request.GET.get('category', 'all')

    study_groups = []
    if category == 'all':
        for membership in user.memberships:
            study_groups.extend(membership.study_groups)
    elif category == 'mine':
        for subscription in user.subscribed_groups:
            study_groups.append(subscription)
    return {'groups': study_groups}


@view_config(
    route_name='groups_create',
    renderer='clusterflunk:templates/groups/create.mako',
    permission='view')
def create(request):
    db = request.db
    user = request.user

    group_create_form = CreateGroupForm(request.POST)

    if request.method == 'POST' and \
        'submit' in request.POST and \
        group_create_form.validate():
        name = group_create_form.name.data
        description = group_create_form.description.data

        study_group = StudyGroup(name=name,
                                 description=description,
                                 created=datetime.now(),
                                 edited=datetime.now(),
                                 network_id=1)
        db.add(study_group)

        group_invite_notification = GroupInviteNotification(created=datetime.now(),
                                                            discriminator="group_invite",
                                                            user_id=user.id,
                                                            study_group=study_group)
        db.add(group_invite_notification)
        for invite in request.POST['invites']:
            notification = Notification(user_id=user.id,
                                        notification_item=group_invite_notification)

            db.add(notification)

        db.flush()
        return HTTPFound(location="/groups")

    return {'group_create_form': group_create_form}
