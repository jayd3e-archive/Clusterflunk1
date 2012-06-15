from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'

    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

    user = relationship('User', backref='subscription')
    group = relationship('Group', backref='subscription')

    def __repr__(self):
        return "<Subscription('%s')>" % (self.id)
