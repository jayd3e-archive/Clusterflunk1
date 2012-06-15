from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base


class Broadcast(Base):
    __tablename__ = 'broadcasts'

    status_id = Column(Integer, ForeignKey('statuses.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

    status = relationship('Status', backref='broadcasts')
    group = relationship('Group', backref='broadcasts')

    def __repr__(self):
        return "<Broadcast('%s')>" % (self.id)
