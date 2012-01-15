from clusterflunk.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class UsersModel(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    joined = Column(DateTime)
    last_online = Column(DateTime)

    acl_user = relationship(AclUsersModel, backref="user")
    articles = relationship(ArticlesModel, backref="author")
    founded_groups = relationship(GroupsModel, backref="author")
    post_comments = relationship(PostCommentsModel, backref="author")
    posts = relationship(PostsModel, backref="author")
    solution_comments = relationship(SolutionCommentsModel, backref="author")
    statuses = relationship(StatusModel, backref="author")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Users('%s')>" % (self.id)