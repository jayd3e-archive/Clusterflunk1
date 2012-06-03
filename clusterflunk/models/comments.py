from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.associationproxy import association_proxy
from clusterflunk.models.base import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('comments.id'))
    founder_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime)

    founder = relationship('User', backref='comments')
    history = relationship('CommentHistory', backref='comment')
    replies = relationship('Comment', backref=backref('parent_comment', remote_side=id))
    article = association_proxy('article_comment', 'article')
    post = association_proxy('post_comment', 'post')
    status = association_proxy('status_comment', 'status')

    def __repr__(self):
        return "<Comment('%s')>" % (self.id)


class CommentHistory(Base):
    __tablename__ = 'comment_history'

    revision = Column(Integer)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    # Version controlled fields
    body = Column(String(1000))

    # Relationships
    author = relationship('User', backref='comment_revs')

    def __repr__(self):
        return "<CommentHistory('%s')>" % (self.id)
