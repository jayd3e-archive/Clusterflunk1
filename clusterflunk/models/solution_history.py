from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class SolutionHistory(Base):
    __tablename__ = 'solution_history'

    id = Column(Integer, primary_key=True)
    revision = Column(Integer)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))
    solution_id = Column(Integer, ForeignKey('solutions.id'))

    # Version controlled fields
    body = Column(String(1000))

    def __repr__(self):
        return "<SolutionHistory('%s')>" % (self.id)
