from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class PostCommentsModel(Base):
    __tablename__ = 'post_comments'
    
    id = Column(Integer, primary_key=True)
    created = Column(Datetime)
    edited = Column(Datetime)
    body = Column(String(1000))
    author = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<PostComments('%s')>" % (self.id)