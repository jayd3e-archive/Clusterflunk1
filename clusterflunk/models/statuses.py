from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class StatusesModel(Base):
    __tablename__ = 'statuses'
    
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    body = Column(String(1000))
    author_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Statuses('%s')>" % (self.id)