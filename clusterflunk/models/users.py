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

    username = Column(String(50))
    email = Column(String(50))
    joined = Column(DateTime)
    last_online = Column(DateTime)

    auth_user = relationship('AuthUser', backref='user', uselist=False)
    moderated_groups = association_proxy('moderator', 'study_group')
    subscribed_groups = association_proxy('subscription', 'study_group')
    memberships = association_proxy('membership', 'network')
    notifications = association_proxy('notification', 'notification_item')

    def get_study_group_ids(self):
        study_group_ids = []
        for study_group in self.subscribed_groups:
            study_group_ids.append(study_group.id)
        return study_group_ids

    def __repr__(self):
        return "<User('%s')>" % (self.id)