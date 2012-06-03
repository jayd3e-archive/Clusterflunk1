from sqlalchemy import (
    Column,
    DateTime,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from clusterflunk.models.base import Base


class Network(Base):
    __tablename__ = 'networks'

    name = Column(String(100))
    created = Column(DateTime)

    study_groups = relationship('StudyGroup', backref="network")
    members = association_proxy('membership', 'user')

    def __repr__(self):
        return "<Network('%s')>" % (self.id)
