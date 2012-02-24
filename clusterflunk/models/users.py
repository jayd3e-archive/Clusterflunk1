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

    def __repr__(self):
        return "<User('%s')>" % (self.id)
