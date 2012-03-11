from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
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
from clusterflunk.models.posts import Post
from clusterflunk.models.posts import PostHistory
from clusterflunk.models.posts import PostComment
from clusterflunk.models.statuses import Status
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.subscriptions import Subscription
from clusterflunk.models.users import User
from clusterflunk.resources import Site
from clusterflunk.request import ClusterflunkRequest
from clusterflunk.security import groupfinder
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
    config = Configurator(settings=settings,
                          root_factory=Site,
                          request_factory=ClusterflunkRequest,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy)
    
    # Includes
    config.include('pyramid_beaker')
    config.include('pyramid_debugtoolbar')

    # Security
    config.set_default_permission('everyone')

    config.add_static_view(name='static', path='clusterflunk:static')
                        
    config.add_route('index', '/')            
    #Handler Root Routes
    #Handler Action Routes
                      
    config.scan('clusterflunk')
    return config.make_wsgi_app()