from pyramid.request import Request
from pyramid.decorator import reify
from pyramid.security import unauthenticated_userid
from clusterflunk.models.users import User

class ClusterflunkRequest(Request):
    @reify
    def db(self):
        maker = self.registry.settings['db.sessionmaker']
        return maker()
    
    @reify
    def user(self):
        session = self.db
        user_id = unauthenticated_userid(self)
        if user_id is not None:
             # this should return None if the user doesn't exist
             # in the database
             return session.query(User).filter_by(id=user_id).first()