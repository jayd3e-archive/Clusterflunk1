from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Moderator(Base):
    __tablename__ = 'moderators'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    study_group_id = Column(Integer, ForeignKey('study_groups.id'))

    def __repr__(self):
        return "<Moderator('%s')>" % (self.id)
