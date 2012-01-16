from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Solution(Base):
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    history = relationship('SolutionHistory', backref="solution")
    comments = relationship('SolutionComment', backref="solution")

    def __repr__(self):
        return "<Solution('%s')>" % (self.id)
