from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class PostsModel(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)
    active = Column(DateTime)
    edited = Column(DateTime)
    due = Column(DateTime)
    description = Column(String(1000))
    group_id = Column(Integer, ForeignKey('groups.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    solutions = relationship(SolutionsModel, backref="post")
    comments = relationship(PostCommentsModel, backref="post")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Posts('%s')>" % (self.id)