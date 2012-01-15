from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class SolutionsModel(Base):
    __tablename__ = 'solutions'
    
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)
    body = Column(String(1000))
    post_id = Column(Integer, ForeignKey('posts.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    comments = Column(SolutionCommentsModel, backref="solution")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Solutions('%s')>" % (self.id)