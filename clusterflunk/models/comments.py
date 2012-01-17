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
    body = Column(String(1000))
    author_id = Column(Integer, ForeignKey('users.id'))

    articles = association_proxy('article_comments', 'article')
    posts = association_proxy('post_comments', 'post')

    def __repr__(self):
        return "<Comment('%s')>" % (self.id)
