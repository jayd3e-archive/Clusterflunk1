from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class WorkingOnModel(Base):
    __tablename__ = 'working_on'
    
    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    when = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<WorkingOn('%s')>" % (self.id)