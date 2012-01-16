from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class Problem(Base):
    __tablename__ = 'problems'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))

    history = relationship('ProblemHistory', backref="problem")
    solutions = relationship('Solution', backref="problem")
    comments = relationship('ProblemComment', backref="problem")

    def __repr__(self):
        return "<Problem('%s')>" % (self.id)
