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
    solution_id = Column(Integer, ForeignKey('solutions.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    solution = relationship('Solution', backref='solution_comments')
    comment = relationship('Comment', backref='solution_comments')

    def __repr__(self):
        return "<SolutionComment('%s')>" % (self.id)
