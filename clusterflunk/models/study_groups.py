from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class StudyGroup(Base):
    __tablename__ = 'study_groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    edited = Column(DateTime)
    network_id = Column(Integer, ForeignKey('networks.id'))
    founder_id = Column(Integer, ForeignKey('users.id'))

    posts = relationship('Post', backref="study_group")

    def __repr__(self):
        return "<StudyGroup('%s')>" % (self.id)
