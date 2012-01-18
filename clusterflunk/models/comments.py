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

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', backref='comments')
    history = relationship('CommentHistory', backref='comment')
    articles = association_proxy('article_comments', 'article')
    posts = association_proxy('post_comments', 'post')
    problems = association_proxy('problem_comments', 'problem')
    solutions = association_proxy('solution_comments', 'solution')

    def __repr__(self):
        return "<Comment('%s')>" % (self.id)

class CommentHistory(Base):
    __tablename__ = 'comment_history'

    id = Column(Integer, primary_key=True)
    revision = Column(Integer)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    # Version controlled fields
    body = Column(String(1000))

    def __repr__(self):
        return "<CommentHistory('%s')>" % (self.id)
