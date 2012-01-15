from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    joined = Column(DateTime)
    last_online = Column(DateTime)

    auth_user = relationship('AclUser', backref="user")
    articles = relationship('Article', backref="author")
    founded_groups = relationship('StudyGroup', backref="author")
    post_comments = relationship('PostComment', backref="author")
    posts = relationship('Post', backref="author")
    solution_comments = relationship('SolutionComment', backref="author")
    statuses = relationship('Status', backref="author")

    def __repr__(self):
        return "<User('%s')>" % (self.id)
