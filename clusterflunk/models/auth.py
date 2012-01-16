from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from clusterflunk.models.base import Base

class AuthUser(Base):
    __tablename__ = 'auth_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(80))
    user_id = Column(Integer, ForeignKey('users.id'))

    auth_groups = association_proxy('auth_user_groups', 'auth_group')

    def __repr__(self):
        return "<AuthUser('%s')>" % (self.id)

class AuthGroup(Base):
    __tablename__ = 'auth_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    auth_users = association_proxy('auth_user_groups', 'auth_user')

    def __repr__(self):
        return "<AuthGroup('%s')>" % (self.id)

class AuthUserGroup(Base):
    __tablename__ = 'auth_users_groups'

    id = Column(Integer, primary_key=True)
    auth_user_id = Column(Integer, ForeignKey('auth_users.id'))
    auth_group_id = Column(Integer, ForeignKey('auth_groups.id'))

    auth_user = relationship('AuthUser', backref='auth_user_groups')
    auth_group = relationship('AuthGroup', backref='auth_user_groups')

    def __repr__(self):
        return "<AuthUserGroup('%s')>" % (self.id)
