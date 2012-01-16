from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('users.id'))

    history = relationship('ArticleHistory', backref="article")
    comments = relationship('ArticleComment', backref="article")

    def __repr__(self):
        return "<Article('%s')>" % (self.id)
