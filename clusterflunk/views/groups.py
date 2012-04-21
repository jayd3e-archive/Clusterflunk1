from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from clusterflunk.forms import CreateGroupForm
from clusterflunk.models.users import User
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.subscriptions import Subscription

@view_config(
    route_name='groups',
    renderer='clusterflunk:templates/groups/index.mako',
    permission='view')
def index(request):
    db = request.db
    user = request.user
    category = request.GET.get('category', 'all')

    study_groups = []
    if category == 'all':
        for membership in user.memberships:
            study_groups.extend(membership.study_groups)
    elif category == 'mine':
        for subscription in user.subscribed_groups:
            study_groups.append(subscription)
    return {'groups':study_groups}

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
        db.flush()
        return HTTPFound(location="/groups")
        
    return {'group_create_form':group_create_form}

@view_config(
    route_name='groups_view',
    renderer='clusterflunk:templates/groups/view.mako',
    permission='view')
def view(request):
    db = request.db
    user = request.user
    _id = request.matchdict.get('group_id')

    group = db.query(StudyGroup).filter_by(id=_id).first()
    return {'group':group}

@view_config(
    route_name='groups',
    renderer='json',
    permission='view',
    request_param='s')
def search(request):
    db = request.db
    user = request.user
    s = request.GET['s']
    study_group_ids = user.get_study_group_ids()

    groups_json = []
    groups = db.query(StudyGroup).join(Subscription, StudyGroup.id==Subscription.study_group_id). \
                                 join(User, Subscription.user_id==User.id). \
                                 filter(StudyGroup.id.in_(study_group_ids)). \
                                 filter(StudyGroup.name.like('%' + s + '%'))
    for group in groups:
        groups_json.append({
            'id' : group.id,
            'name' : group.name
        })
    return groups_json

@view_config(
    route_name='subscribe_to_group',
    renderer='json',
    permission='view')
def subscribe_to_group(request):
    db = request.db
    user = request.user
    group_id = request.matchdict.get('group_id')

    subscription = db.query(Subscription).filter_by(user_id=user.id,
                                                    study_group_id=group_id).first()
    
    if not subscription:
        subscription = Subscription(user_id=user.id,
                                    study_group_id=group_id)
        db.add(subscription)
        db.flush()
        status = 'subscribed'
    else:
        status = 'exists'
    
    return {'status': status}

@view_config(
    route_name='unsubscribe_to_group',
    renderer='json',
    permission='view')
def unsubscribe_to_group(request):
    db = request.db
    user = request.user
    group_id = request.matchdict.get('group_id')

    subscription = db.query(Subscription).filter_by(user_id=user.id,
                                                    study_group_id=group_id).first()
    if subscription:
        db.delete(subscription)
        db.flush()
        status = 'unsubscribed'
    else:
        status = 'nonexistant'
    
    return {'status': status}