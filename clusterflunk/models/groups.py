from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class GroupsModel(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
	name = Column(String(100))
	created = Column(Datetime)
	edited = Column(Datetime)
	founder = Column(Integer, ForeignKey('users.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclGroups('%s')>" % (self.id)