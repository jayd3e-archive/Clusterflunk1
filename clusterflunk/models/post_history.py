from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class PostHistory(Base):
    __tablename__ = 'post_history'

    id = Column(Integer, primary_key=True)
    revision = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created = Column(Datetime)

    # Version controlled fields
    name = Column(String(100))
    description = Column(String(1000))
    due = Column(Datetime)
    active = Column(DateTime)

    def __repr__(self):
        return "<Post('%s')>" % (self.id)
