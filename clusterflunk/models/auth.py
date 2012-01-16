from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class AuthUser(Base):
    __tablename__ = 'auth_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(80))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<AuthUser('%s')>" % (self.id)

class AuthGroup(Base):
    __tablename__ = 'auth_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __repr__(self):
        return "<AuthGroup('%s')>" % (self.id)

class AuthUserGroup(Base):
    __tablename__ = 'auth_users_groups'

    id = Column(Integer, primary_key=True)
    auth_user_id = Column(Integer, ForeignKey('auth_users.id'))
    auth_group_id = Column(Integer, ForeignKey('auth_groups.id'))

    def __repr__(self):
        return "<AuthUserGroup('%s')>" % (self.id)
