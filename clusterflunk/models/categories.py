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

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __repr__(self):
        return "<Category('%s')>" % (self.id)

class PostCategory(Base):
    __tablename__ = 'post_categories'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    category_id = Column(Integer, ForeignKey('category.id'))

    def __repr__(self):
        return "<Category('%s')>" % (self.id)