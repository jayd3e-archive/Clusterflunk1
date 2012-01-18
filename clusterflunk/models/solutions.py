from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from clusterflunk.models.base import Base

class Solution(Base):
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    history = relationship('SolutionHistory', backref="solution")
    comments = association_proxy('solution_comments', 'comment')

    def __repr__(self):
        return "<Solution('%s')>" % (self.id)

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

class SolutionComment(Base):
    __tablename__ = 'solution_comments'

    id = Column(Integer, primary_key=True)
    solution_id = Column(Integer, ForeignKey('solutions.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    solution = relationship('Solution', backref='solution_comments')
    comment = relationship('Comment', backref='solution_comments')

    def __repr__(self):
        return "<SolutionComment('%s')>" % (self.id)
