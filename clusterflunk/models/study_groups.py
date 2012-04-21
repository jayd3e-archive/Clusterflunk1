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

class StudyGroup(Base):
    __tablename__ = 'study_groups'

    name = Column(String(100))
    description = Column(String(500))
    created = Column(DateTime)
    edited = Column(DateTime)
    network_id = Column(Integer, ForeignKey('networks.id'))
    founder_id = Column(Integer, ForeignKey('users.id'))

    founder = relationship('User', backref='founded_groups')
    posts = relationship('Post', backref='study_group')
    moderators = association_proxy('moderator', 'user')
    subscribers = association_proxy('subscription', 'user')
    statuses = association_proxy('broadcasts', 'status')

    def __repr__(self):
        return "<StudyGroup('%s')>" % (self.id)
