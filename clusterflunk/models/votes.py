from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base
from clusterflunk.models.users import User
from clusterflunk.models.comments import Comment


class Vote(Base):
    __tablename__ = 'votes'

    user_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    vote = Column(Integer(1))

    user = relationship(User, backref="votes")
    comment = relationship(Comment, backref="votes")

    def __repr__(self):
        return "<Vote('%s')>" % (self.id)
