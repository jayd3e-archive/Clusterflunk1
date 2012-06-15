from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base


class Tag(Base):
    __tablename__ = 'tags'

    name = Column(String(100))

    def __repr__(self):
        return "<Tag('%s')>" % (self.id)


class PostTag(Base):
    __tablename__ = 'post_tags'

    post_id = Column(Integer, ForeignKey('posts.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))

    tag = relationship('Tag')
    post = relationship('Post', backref='post_tags')

    def __repr__(self):
        return "<PostTag('%s')>" % (self.id)
