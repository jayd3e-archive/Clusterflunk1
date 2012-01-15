from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class SolutionCommentsModel(Base):
    __tablename__ = 'solution_comments'
    
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    edited = Column(DateTime)
    body = Column(DateTime)
    author_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<SolutionComments('%s')>" % (self.id)