from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base


class Membership(Base):
    __tablename__ = 'memberships'

    user_id = Column(Integer, ForeignKey('users.id'))
    network_id = Column(Integer, ForeignKey('networks.id'))

    user = relationship('User', backref='membership')
    network = relationship('Network', backref='membership')

    def __repr__(self):
        return "<Membership('%s')>" % (self.id)
