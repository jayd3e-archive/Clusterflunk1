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


class Group(Base):
    __tablename__ = 'groups'

    name = Column(String(100))
    description = Column(String(500))
    created = Column(DateTime)
    edited = Column(DateTime)
    network_id = Column(Integer, ForeignKey('networks.id'))
    founder_id = Column(Integer, ForeignKey('users.id'))

    founder = relationship('User', backref='founded_groups')
    posts = relationship('Post', backref='group')
    moderators = association_proxy('moderator', 'user')
    subscribers = association_proxy('subscription', 'user')
    questions = association_proxy('broadcasts', 'question')

    def __repr__(self):
        return "<Group('%s')>" % (self.id)
