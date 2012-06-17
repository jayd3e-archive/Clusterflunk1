from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPForbidden
from clusterflunk.models.base import initializeBase
from clusterflunk.models.auth import AuthUser
from clusterflunk.models.auth import AuthGroup
from clusterflunk.models.auth import AuthUserGroup
from clusterflunk.models.tags import Tag
from clusterflunk.models.tags import PostTag
from clusterflunk.models.comments import Comment
from clusterflunk.models.comments import CommentHistory
from clusterflunk.models.moderators import Moderator
from clusterflunk.models.networks import Network
from clusterflunk.models.notifications import Notification
from clusterflunk.models.notifications import NotificationItem
from clusterflunk.models.notifications import GroupInviteNotification
from clusterflunk.models.notifications import QuestionCommentNotification
from clusterflunk.models.posts import Post
from clusterflunk.models.posts import PostHistory
from clusterflunk.models.posts import PostComment
from clusterflunk.models.questions import Question
from clusterflunk.models.questions import QuestionComment
from clusterflunk.models.groups import Group
from clusterflunk.models.subscriptions import Subscription
from clusterflunk.models.users import User
from clusterflunk.models.votes import Vote
from clusterflunk.models.memberships import Membership
from clusterflunk.models.broadcasts import Broadcast
from clusterflunk.resources import Site
from clusterflunk.exceptions import notFound
from clusterflunk.exceptions import forbidden


def main(global_config, **settings):
    '''Main config function'''
    config = Configurator(settings=settings,
                          root_factory=Site)

    # Includes
    # config.include('pyramid_debugtoolbar')

    # Security
    config.set_default_permission('logged_in')
    config.add_static_view(name='static', path='clusterflunk:static')

    # Routes
    config.add_route('index', '/')

    #Exception Views
    config.add_view(notFound,
                    context=HTTPNotFound,
                    permission='__no_permission_required__',
                    renderer='clusterflunk:templates/exceptions/not_found.mako')
    config.add_view(forbidden,
                    context=HTTPForbidden,
                    permission='__no_permission_required__')

    config.scan('clusterflunk')
    return config.make_wsgi_app()
