from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPForbidden
from clusterflunk.models.base import initializeBase
from clusterflunk.models.articles import Article
from clusterflunk.models.auth import AuthUser
from clusterflunk.models.auth import AuthGroup
from clusterflunk.models.auth import AuthUserGroup
from clusterflunk.models.categories import Category
from clusterflunk.models.categories import PostCategory
from clusterflunk.models.comments import Comment
from clusterflunk.models.comments import CommentHistory
from clusterflunk.models.moderators import Moderator
from clusterflunk.models.networks import Network
from clusterflunk.models.notifications import Notification
from clusterflunk.models.notifications import NotificationItem
from clusterflunk.models.notifications import GroupInviteNotification
from clusterflunk.models.posts import Post
from clusterflunk.models.posts import PostHistory
from clusterflunk.models.posts import PostComment
from clusterflunk.models.statuses import Status
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.subscriptions import Subscription
from clusterflunk.models.users import User
from clusterflunk.models.votes import Vote
from clusterflunk.models.memberships import Membership
from clusterflunk.models.broadcasts import Broadcast
from clusterflunk.resources import Site
from clusterflunk.request import ClusterflunkRequest
from clusterflunk.security import groupfinder
from clusterflunk.exceptions import notFound
from clusterflunk.exceptions import forbidden
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def main(global_config, **settings):
    '''Main config function'''
    engine = engine_from_config(settings, 'sqlalchemy.')
    initializeBase(engine)
    # NOTE: A transaction is created by default in postgres, so I have added the
    # 'autocommit' kwarg so that I don't have to deal with transactions for
    # the moment.  Remove it once I have pyramid_tm & zope.sqlalchemy implemented.
    maker = sessionmaker(bind=engine, autocommit=True)
    settings['db.sessionmaker'] = maker
    
    authentication_policy = SessionAuthenticationPolicy(callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    session_factory = UnencryptedCookieSessionFactoryConfig('1h209asf093nf930fni23f0fb29401', cookie_max_age=3600)
    config = Configurator(settings=settings,
                          root_factory=Site,
                          request_factory=ClusterflunkRequest,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          session_factory=session_factory)
    
    # Includes
    config.include('pyramid_debugtoolbar')

    # Security
    config.set_default_permission('logged_in')

    config.add_static_view(name='static', path='clusterflunk:static')
                                   
    #View Root Routes
    config.add_route('index', '/') 
    config.add_route('login', '/login')
    config.add_route('register', '/register') 
    config.add_route('logout', '/logout')
    config.add_route('posts', '/posts')
    config.add_route('users', '/users')
    config.add_route('groups', '/groups')
    config.add_route('articles', '/articles')
    config.add_route('statuses', '/statuses')
    config.add_route('profile', '/profile')

    #View Action Routes
    config.add_route('posts_view', '/posts/{post_id}')
    config.add_route('comments_post_view', '/comments/post/{post_id}')
    config.add_route('comments_status_view', '/comments/status/{status_id}')
    config.add_route('articles_view', '/articles/{article_id}')
    config.add_route('groups_create', '/groups/create')
    config.add_route('groups_view', '/groups/{group_id}')
    config.add_route('subscribe_to_group', '/groups/{group_id}/subscribe')
    config.add_route('unsubscribe_to_group', '/groups/{group_id}/unsubscribe')

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