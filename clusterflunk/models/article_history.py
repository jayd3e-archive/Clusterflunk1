from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class ArticleHistory(Base):
    __tablename__ = 'article_history'

    id = Column(Integer, primary_key=True)
    revision = Column(Integer)
    created = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))
    article_id = Colun(Integer, ForeignKey('problems.id'))

    # Version controlled fields
    body = Column(String(1000))

    def __repr__(self):
        return "<ArticleHistory('%s')>" % (self.id)
