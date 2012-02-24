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
    founder_id = Column(Integer, ForeignKey('users.id'))

    founder = relationship('User', backref="articles")
    history = relationship('ArticleHistory', backref="article")
    comments = association_proxy('article_comments', 'comment')

    def __repr__(self):
        return "<Article('%s', '%s')>" % (self.id,
                                          self.founder_id)

class ArticleHistory(Base):
    __tablename__ = 'article_history'

    id = Column(Integer, primary_key=True)
    revision = Column(Integer)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))
    article_id = Column(Integer, ForeignKey('articles.id'))

    # Version controlled fields
    body = Column(String(1000))

    # Relationships
    author = relationship('User', backref='article_revs')

    def __repr__(self):
        return "<ArticleHistory('%s', '%s', '%s', '%s', '%s')>" % (
            self.id,
            self.revision,
            self.created,
            self.author_id,
            self.article_id)

class ArticleComment(Base):
    __tablename__ = 'article_comments'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    article = relationship('Article', backref='article_comments')
    comment = relationship('Comment', backref='article_comments')

    def __repr__(self):
        return "<ArticleComment('%s')>" % (self.id)
