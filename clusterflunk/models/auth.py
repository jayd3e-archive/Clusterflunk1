import os
from hashlib import sha1
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from clusterflunk.models.base import Base


class AuthUser(Base):
    __tablename__ = 'auth_users'

    username = Column(String(50))
    password = Column(String(80))
    user_id = Column(Integer, ForeignKey('users.id'))

    auth_groups = association_proxy('auth_user_groups', 'auth_group')

    def __init__(self, username, password):
        self.username = username
        self._set_password(password)

    def __repr__(self):
        return "<AuthUser('%s')>" % (self.id)

    def _set_password(self, password):
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')

        self.password = hashed_password

    def validate_password(self, password):
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()


class AuthGroup(Base):
    __tablename__ = 'auth_groups'

    name = Column(String(100))

    auth_users = association_proxy('auth_user_groups', 'auth_user')

    def __repr__(self):
        return "<AuthGroup('%s')>" % (self.id)


class AuthUserGroup(Base):
    __tablename__ = 'auth_users_groups'

    auth_user_id = Column(Integer, ForeignKey('auth_users.id'))
    auth_group_id = Column(Integer, ForeignKey('auth_groups.id'))

    auth_user = relationship('AuthUser', backref='auth_user_groups')
    auth_group = relationship('AuthGroup', backref='auth_user_groups')

    def __repr__(self):
        return "<AuthUserGroup('%s')>" % (self.id)
