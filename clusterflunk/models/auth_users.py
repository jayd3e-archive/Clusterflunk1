from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class AuthUsersModel(Base):
    __tablename__ = 'auth_users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(80))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AuthUsers('%s')>" % (self.id)