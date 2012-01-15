from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class StatusesModel(Base):
    __tablename__ = 'statuses'
    
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    body = Column(String(1000))
    author = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Statuses('%s')>" % (self.id)