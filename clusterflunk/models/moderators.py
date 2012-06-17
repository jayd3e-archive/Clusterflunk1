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
    group_id = Column(Integer, ForeignKey('groups.id'))

    user = relationship('User', backref="moderator")
    group = relationship('Group', backref="moderator")

    def __repr__(self):
        return "<Moderator('%s')>" % (self.id)
