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

class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))

    history = relationship('ProblemHistory', backref="problem")
    solutions = relationship('Solution', backref="problem")
    comments = association_proxy('problem_comments', 'comment')

    def __repr__(self):
        return "<Problem('%s')>" % (self.id)

class ProblemHistory(Base):
    __tablename__ = 'problem_history'

    id = Column(Integer, primary_key=True)
    revision = Column(Integer)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))
    problem_id = Column(Integer, ForeignKey('problems.id'))

    # Version controlled fields
    body = Column(String(1000))

    def __repr__(self):
        return "<ProblemHistory('%s')>" % (self.id)

class ProblemComment(Base):
    __tablename__ = 'problem_comments'

    id = Column(Integer, primary_key=True)
    problem_id = Column(Integer, ForeignKey('problems.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    problem = relationship('Problem', backref='problem_comments')
    comment = relationship('Comment', backref='problem_comments')

    def __repr__(self):
        return "<ProblemComment('%s')>" % (self.id)
