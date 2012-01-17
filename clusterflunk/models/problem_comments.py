from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class ProblemComment(Base):
    __tablename__ = 'problem_comments'

    id = Column(Integer, primary_key=True)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    problem = relationship('Problem', backref='problem_comments')
    comment = relationship('Comment', backref='problem_comments')

    def __repr__(self):
        return "<ProblemComment('%s')>" % (self.id)
