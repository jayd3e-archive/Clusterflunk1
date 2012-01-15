from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class AuthUsersGroupsModel(Base):
    __tablename__ = 'auth_users_groups'
    
    id = Column(Integer, primary_key=True)
    auth_user_id = Column(Integer, ForeignKey('auth_users.id'))
    auth_group_id = Column(Integer, ForeignKey('auth_groups.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AuthUserGroups('%s')>" % (self.id)