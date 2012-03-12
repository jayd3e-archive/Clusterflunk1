from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from .base import Base
from .users import User
from .posts import Post

class Vote(Base):
    __tablename__ = 'votes'

    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    vote = Column(Integer(1))

    users = relationship(User,
                         backref="votes")
    posts = relationship(Post,
                         backref="votes")
    
    def __repr__(self):
        return "<Vote('%s')>" % (self.id)