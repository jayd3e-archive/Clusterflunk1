from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base


class Moderator(Base):
    __tablename__ = 'moderators'

    user_id = Column(Integer, ForeignKey('users.id'))
    study_group_id = Column(Integer, ForeignKey('study_groups.id'))

    user = relationship('User', backref="moderator")
    study_group = relationship('StudyGroup', backref="moderator")

    def __repr__(self):
        return "<Moderator('%s')>" % (self.id)
