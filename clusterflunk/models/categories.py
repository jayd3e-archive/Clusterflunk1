from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Category(Base):
    __tablename__ = 'categories'

    name = Column(String(100))

    def __repr__(self):
        return "<Category('%s')>" % (self.id)

class PostCategory(Base):
    __tablename__ = 'post_categories'

    post_id = Column(Integer, ForeignKey('posts.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category')
    post = relationship('Post', backref='post_categories')

    def __repr__(self):
        return "<PostCategory('%s')>" % (self.id)