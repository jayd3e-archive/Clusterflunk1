from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    body = Column(String(1000))
    author_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<Status('%s')>" % (self.id)
