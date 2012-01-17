from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

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
