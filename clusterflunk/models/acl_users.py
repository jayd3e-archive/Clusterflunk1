from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class AclUsersModel(Base):
    __tablename__ = 'acl_users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(80))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclUsers('%s')>" % (self.id)