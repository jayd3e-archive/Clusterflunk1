from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class AclUsersGroupsModel(Base):
    __tablename__ = 'acl_users_groups'
    
    id = Column(Integer, primary_key=True)
    acl_user_id = Column(Integer)
    acl_group_id = Column(Integer)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclUserGroups('%s')>" % (self.id)