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
    category_id = Column(Integer, ForeignKey('categories.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    study_group_id = Column(Integer, ForeignKey('study_groups.id'))

    history = relationship('PostHistory', backref="post")
    problems = relationship('Problem', backref="post")
    comments = relationship('PostComment', backref="post")

    def __repr__(self):
        return "<Post('%s')>" % (self.id)
