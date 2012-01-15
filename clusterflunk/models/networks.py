from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class NetworksModel(Base):
    __tablename__ = 'networks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Networks('%s')>" % (self.id)