from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    joined = Column(DateTime)
    last_online = Column(DateTime)

    auth_user = relationship('AuthUser', backref='user', uselist=False)
    moderated_groups = association_proxy('moderator', 'study_group')
    subscribed_groups = association_proxy('subscription', 'study_group')

    def __init__(self, username, password, email=None):
        self.username = username
        self._set_password(password)
        if email is not None:
            self.email = email

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.username,
                                       self.email)

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
