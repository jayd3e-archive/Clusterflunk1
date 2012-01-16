from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class ArticleComment(Base):
    __tablename__ = 'article_comments'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    article = relationship('Article', backref='article_comments')
    comment = relationship('Comment', backref='article_comments')

    def __repr__(self):
        return "<ArticleComment('%s')>" % (self.id)
