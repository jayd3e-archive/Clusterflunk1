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


class Post(Base):
    __tablename__ = 'posts'

    group_id = Column(Integer, ForeignKey('groups.id'))
    founder_id = Column(Integer, ForeignKey('users.id'))
    created = Column(DateTime)

    founder = relationship('User', backref="posts")
    history = relationship('PostHistory', backref='post')
    comments = association_proxy('post_comments', 'comment')
    tags = association_proxy('post_tags', 'tag')

    def __repr__(self):
        return "<Post('%s')>" % (self.id)


class PostHistory(Base):
    __tablename__ = 'post_history'

    revision = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created = Column(DateTime)

    # Version controlled fields
    name = Column(String(100))
    description = Column(String(1000))
    due = Column(DateTime)
    active = Column(DateTime)

    # Relationships
    author = relationship('User', backref='post_revs')

    def __repr__(self):
        return "<PostHistory('%s')>" % (self.id)


class PostComment(Base):
    __tablename__ = 'post_comments'

    post_id = Column(Integer, ForeignKey('posts.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    post = relationship('Post', backref='post_comments')
    comment = relationship('Comment', backref=backref('post_comment', uselist=False))

    def __repr__(self):
        return "<PostComment('%s')>" % (self.id)
