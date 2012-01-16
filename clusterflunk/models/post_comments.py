from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class PostComment(Base):
    __tablename__ = 'post_comments'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    comment_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<PostComment('%s')>" % (self.id)
