from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    active = Column(DateTime)
    edited = Column(DateTime)
    due = Column(DateTime)
    description = Column(String(1000))
    category_id = Column(Integer, ForeignKey('categories.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    solutions = relationship('Solution', backref="post")
    comments = relationship('PostComment', backref="post")

    def __repr__(self):
        return "<Post('%s')>" % (self.id)
