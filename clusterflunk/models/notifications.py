from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from clusterflunk.models.base import Base


class Notification(Base):
    __tablename__ = 'notifications'

    user_id = Column(Integer, ForeignKey('users.id'))
    notification_item_id = Column(Integer, ForeignKey('notification_items.id'))

    user = relationship('User', backref='notification')
    notification_item = relationship('NotificationItem')

    def __repr__(self):
        return "<Notification('%s')>" % (self.id)


class NotificationItem(Base):
    __tablename__ = 'notification_items'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    discriminator = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': discriminator}

    def __repr__(self):
        return "<NotificationItem('%s')>" % (self.id)


class GroupInviteNotification(NotificationItem):
    __tablename__ = 'group_invite_notifications'

    id = Column(Integer, ForeignKey('notification_items.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    study_group_id = Column(Integer, ForeignKey('study_groups.id'))
    __mapper_args__ = {'polymorphic_identity': 'group_invite'}

    inviter = relationship('User')
    study_group = relationship('StudyGroup')

    def __repr__(self):
        return "<GroupInviteNotification('%s')>" % (self.id)


class StatusCommentNotification(NotificationItem):
    __tablename__ = 'status_comment_notifications'

    id = Column(Integer, ForeignKey('notification_items.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))
    status_id = Column(Integer, ForeignKey('statuses.id'))
    __mapper_args__ = {'polymorphic_identity': 'status_comment'}

    commenter = relationship('User')
    comment = relationship('Comment')
    status = relationship('Status')

    def __repr__(self):
        return "<StatusCommentNotification('%s')>" % (self.id)
