from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Broadcast(Base):
    __tablename__ = 'broadcasts'

    status_id = Column(Integer, ForeignKey('statuses.id'))
    study_group_id = Column(Integer, ForeignKey('study_groups.id'))

    status = relationship('Status', backref='broadcasts')
    study_group = relationship('StudyGroup', backref='broadcasts')

    def __repr__(self):
        return "<Broadcast('%s')>" % (self.id)
