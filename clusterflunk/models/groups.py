from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTimes

class GroupsModel(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
	name = Column(String(100))
	created = Column(Datetime)
	edited = Column(Datetime)
	network_id = Column(Integer, ForeignKey('networks.id'))
	founder_id = Column(Integer, ForeignKey('users.id'))

	posts = relationship(PostsModel, backref="group")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclGroups('%s')>" % (self.id)