from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

from clusterflunk.models.base import Base


class Status(Base):
    __tablename__ = 'statuses'

    created = Column(DateTime)
    founder_id = Column(Integer, ForeignKey('users.id'))

    founder = relationship('User', backref='statuses')
    study_groups = association_proxy('broadcasts', 'study_group')
    history = relationship('StatusHistory', backref='status')
    comments = association_proxy('status_comments', 'comment')

    def __repr__(self):
        return "<Status('%s')>" % (self.id)


class StatusHistory(Base):
    __tablename__ = 'status_history'

    revision = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))
    status_id = Column(Integer, ForeignKey('statuses.id'))
    created = Column(DateTime)

    # Version controlled fields
    body = Column(String(1000))

    # Relationships
    author = relationship('User', backref='status_revs')

    def __repr__(self):
        return "<StatusHistory('%s')>" % (self.id)


class StatusComment(Base):
    __tablename__ = 'status_comments'

    status_id = Column(Integer, ForeignKey('statuses.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    status = relationship('Status', backref='status_comments')
    comment = relationship('Comment', backref=backref('status_comment', uselist=False))

    def __repr__(self):
        return "<StatusComment('%s')>" % (self.id)
