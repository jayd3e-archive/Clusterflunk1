from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class WorkingOn(Base):
    __tablename__ = 'working_on'

    id = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    when = Column(DateTime)

    worker = relationship('User', backref='working_ons')
    post = relationship('Post', backref='working_ons')

    def __repr__(self):
        return "<WorkingOn('%s')>" % (self.id)
