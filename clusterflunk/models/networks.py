from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Network(Base):
    __tablename__ = 'networks'

    name = Column(String(100))
    created = Column(DateTime)

    study_groups = relationship('StudyGroup', backref="network")

    def __repr__(self):
        return "<Network('%s')>" % (self.id)
