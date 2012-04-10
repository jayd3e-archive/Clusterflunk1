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

class Status(Base):
    __tablename__ = 'statuses'

    created = Column(DateTime)
    body = Column(String(1000))
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', backref='statuses')
    study_groups = association_proxy('broadcasts', 'study_group')

    def __repr__(self):
        return "<Status('%s')>" % (self.id)
