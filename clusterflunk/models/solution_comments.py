from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class SolutionComment(Base):
    __tablename__ = 'solution_comments'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)
    body = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<SolutionComment('%s')>" % (self.id)
