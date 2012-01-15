from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class ModeratorsModel(Base):
    __tablename__ = 'moderators'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Moderators('%s')>" % (self.id)