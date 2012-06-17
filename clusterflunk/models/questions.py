from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

from clusterflunk.models.base import Base


class Question(Base):
    __tablename__ = 'questions'

    created = Column(DateTime)
    founder_id = Column(Integer, ForeignKey('users.id'))

    founder = relationship('User', backref='questions')
    groups = association_proxy('broadcasts', 'group')
    history = relationship('QuestionHistory', backref='question')
    comments = association_proxy('question_comments', 'comment')

    def __repr__(self):
        return "<Question('%s')>" % (self.id)


class QuestionHistory(Base):
    __tablename__ = 'question_history'

    revision = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    created = Column(DateTime)

    # Version controlled fields
    body = Column(String(1000))

    # Relationships
    author = relationship('User', backref='question_revs')

    def __repr__(self):
        return "<QuestionHistory('%s')>" % (self.id)


class QuestionComment(Base):
    __tablename__ = 'question_comments'

    question_id = Column(Integer, ForeignKey('questions.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    question = relationship('Question', backref='question_comments')
    comment = relationship('Comment', backref=backref('question_comment', uselist=False))

    def __repr__(self):
        return "<QuestionComment('%s')>" % (self.id)
