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

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', backref='articles')
    history = relationship('ArticleHistory', backref="article")
    comments = association_proxy('article_comments', 'comment')

    def __repr__(self):
        return "<Article('%s', '%s')>" % (self.id,
                                          self.author_id)
