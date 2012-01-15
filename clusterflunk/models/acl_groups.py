from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class AclGroupsModel(Base):
    __tablename__ = 'acl_groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclGroups('%s')>" % (self.id)
