from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'

    user_id = Column(Integer, ForeignKey('users.id'))
    study_group_id = Column(Integer, ForeignKey('study_groups.id'))

    user = relationship('User', backref='subscription')
    study_group = relationship('StudyGroup', backref='subscription')

    def __repr__(self):
        return "<Subscription('%s')>" % (self.id)
