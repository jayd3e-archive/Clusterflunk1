import unittest
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Models
from clusterflunk.models.base import Base
from clusterflunk.models.auth import (
    AuthUser,
    AuthGroup,
    AuthUserGroup,
)
from clusterflunk.models.users import User
from clusterflunk.models.groups import Group
from clusterflunk.models.networks import Network
from clusterflunk.models.tags import Tag
from clusterflunk.models.tags import PostTag
from clusterflunk.models.posts import (
    Post,
    PostComment,
    PostHistory,
)
from clusterflunk.models.comments import (
    Comment,
    CommentHistory,
)
from clusterflunk.models.questions import (
    Question,
    QuestionHistory,
    QuestionComment
)
from clusterflunk.models.moderators import Moderator
from clusterflunk.models.subscriptions import Subscription
from clusterflunk.models.votes import Vote
from clusterflunk.models.memberships import Membership
from clusterflunk.models.broadcasts import Broadcast
from clusterflunk.models.notifications import (
    Notification,
    NotificationItem,
    GroupInviteNotification,
    QuestionCommentNotification
)


class TestModels(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite://')
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def testPosts(self):
        session = self.Session()

        post = Post(id=1,
                    founder_id=1,
                    group_id=1)

        post_rev1 = PostHistory(revision=1,
                                created=datetime.now(),
                                author_id=1,
                                description="This is an assignment.")
        post_rev2 = PostHistory(revision=2,
                                created=datetime.now(),
                                author_id=2,
                                description="This is another assignment.")
        post_rev3 = PostHistory(revision=3,
                                created=datetime.now(),
                                author_id=3,
                                description="This is the last assignment.")
        for p in [post_rev1, post_rev2, post_rev3]:
            post.history.append(p)
        session.add(post)

        comment = Comment(id=1,
                          founder_id=1)
        comment1 = Comment(id=2,
                           founder_id=1)
        comment2 = Comment(id=3,
                           founder_id=1)
        for c in [comment, comment1, comment2]:
            session.add(c)

        post_comment = PostComment(post_id=1,
                                   comment_id=1)
        post_comment1 = PostComment(post_id=1,
                                    comment_id=2)
        post_comment2 = PostComment(post_id=1,
                                    comment_id=3)
        for pc in [post_comment, post_comment1, post_comment2]:
            session.add(pc)

        tag = Tag(id=1,
                       name='Test')
        session.add(tag)

        post_tag = PostTag(id=1,
                           post_id=1,
                           tag_id=1)
        post.post_tags.append(post_tag)

        session.flush()
        self.assertTrue(str(post).startswith('<Post'),
                        msg="str(Post) must start with '<Post'")
        self.assertEqual(post.history, [post_rev1, post_rev2, post_rev3])
        self.assertEqual(post_rev1.post, post)
        self.assertEqual(post_rev2.post, post)
        self.assertEqual(post_rev3.post, post)
        self.assertEqual(post.comments, [comment, comment1, comment2])
        self.assertEqual(comment.post, post)
        self.assertEqual(comment1.post, post)
        self.assertEqual(comment2.post, post)
        self.assertIn(tag, post.tags)

    def testPostComments(self):
        session = self.Session()

        post = Post(id=1,
                    founder_id=1,
                    group_id=1)
        comment = Comment(id=1,
                          founder_id=1)
        post_comment = PostComment(post_id=1,
                                   comment_id=1)
        session.add(post)
        session.add(comment)
        session.add(post_comment)

        session.flush()
        self.assertTrue(str(post_comment).startswith('<PostComment'),
                        msg="str(PostComment) must start with '<PostComment'")
        self.assertEqual(post_comment.post, post)
        self.assertEqual(post_comment.comment, comment)
        self.assertEqual(post_comment, comment.post_comment)
        self.assertIn(post_comment, post.post_comments)

    def testPostHistory(self):
        session = self.Session()

        post_rev = PostHistory(revision=1,
                               created=datetime.now(),
                               author_id=1,
                               name="Awesome Assignment",
                               description="This is a helpful article.",
                               due=datetime.now(),
                               active=datetime.now())
        session.add(post_rev)
        session.flush()
        self.assertTrue(str(post_rev).startswith('<PostHistory'),
                        msg="str(PostHistory) must start with '<PostHistory'")

    def testComments(self):
        session = self.Session()

        #
        # - Comment(1) (3 Revisions)
        #   |
        #    - Reply Comment(2)
        #      |
        #       - Another Reply Comment(3)
        #

        comment1 = Comment(id=1,
                           parent_id=None,
                           founder_id=1)
        comment2 = Comment(id=2,
                           parent_id=1,
                           founder_id=1)
        comment3 = Comment(id=3,
                           parent_id=2,
                           founder_id=1)

        comment_rev1 = CommentHistory(id=1,
                                      revision=1,
                                      created=datetime.now(),
                                      author_id=1,
                                      comment_id=1,
                                      body="U Suk!")
        comment_rev2 = CommentHistory(id=2,
                                      revision=2,
                                      created=datetime.now(),
                                      author_id=1,
                                      comment_id=1,
                                      body="U Suk More!")
        comment_rev3 = CommentHistory(id=3,
                                      revision=3,
                                      created=datetime.now(),
                                      author_id=1,
                                      comment_id=1,
                                      body="U Suk Even More!")
        for cr in [comment_rev1, comment_rev2, comment_rev3]:
            comment1.history.append(cr)

        session.add(comment1)
        session.add(comment2)
        session.add(comment3)

        session.flush()
        self.assertTrue(str(comment1).startswith('<Comment'),
                        msg="str(Comment) must start with '<Comment'")
        self.assertEqual(comment1, comment_rev1.comment)
        self.assertEqual(comment1, comment_rev2.comment)
        self.assertEqual(comment1, comment_rev3.comment)
        self.assertEqual(comment1.history, [comment_rev1, comment_rev2, comment_rev3])
        self.assertEqual(comment1.replies, [comment2])
        self.assertEqual(comment2.replies, [comment3])
        self.assertEqual(comment2.parent_comment, comment1)

    def testCommentHistory(self):
        session = self.Session()

        comment_rev = CommentHistory(id=1,
                                     revision=1,
                                     created=datetime.now(),
                                     author_id=1,
                                     comment_id=1,
                                     body="U Suk!")
        session.add(comment_rev)
        session.flush()
        self.assertTrue(str(comment_rev).startswith('<CommentHistory'),
                        msg="str(CommentHistory) must start with '<CommentHistory'")

    def testAuth(self):
        session = self.Session()

        auth_user = AuthUser('jayd3e', 'secret')
        auth_group = AuthGroup(id=1,
                               name='admin')
        auth_user_group = AuthUserGroup(auth_user_id=1,
                                        auth_group_id=1)

        session.add(auth_user)
        session.add(auth_group)
        session.add(auth_user_group)

        session.flush()
        self.assertTrue(str(auth_user).startswith('<AuthUser'),
                        msg="str(AuthUser) must start with '<AuthUser'")
        self.assertTrue(str(auth_group).startswith('<AuthGroup'),
                        msg="str(AuthGroup) must start with '<AuthGroup'")
        self.assertTrue(str(auth_user_group).startswith('<AuthUserGroup'),
                        msg="str(AuthUserGroup) must start with '<AuthUserGroup'")
        self.assertIn(auth_user, auth_group.auth_users)
        self.assertIn(auth_group, auth_user.auth_groups)
        self.assertEqual(auth_user_group.auth_user, auth_user)
        self.assertEqual(auth_user_group.auth_group, auth_group)

    def testTags(self):
        session = self.Session()

        tag = Tag(id=1,
                       name='Test')
        post_tag = PostTag(id=1,
                           tag_id=1)

        post_tag.tag = tag
        session.add(post_tag)

        session.flush()
        self.assertTrue(str(tag).startswith('<Tag'),
                        msg="str(Tag) must start with '<Tag'")
        self.assertTrue(str(post_tag).startswith('<PostTag'),
                        msg="str(PostTag) must start with '<PostTag'")
        self.assertEqual(post_tag.tag, tag)

    def testModerators(self):
        session = self.Session()

        group = Group(id=1,
                      name="Physics 101",
                      created=datetime.now(),
                      edited=datetime.now())

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())

        moderator = Moderator(user_id=1,
                              group_id=1)

        session.add(group)
        session.add(user)
        session.add(moderator)

        session.flush()
        self.assertTrue(str(moderator).startswith('<Moderator'),
                        msg="str(Moderator) must start with '<Moderator'")
        self.assertIn(user, group.moderators)
        self.assertIn(group, user.moderated_groups)
        self.assertEqual(moderator.user, user)
        self.assertEqual(moderator.group, group)

    def testNetworks(self):
        session = self.Session()

        network = Network(id=1,
                          name="Uni of Iowa",
                          created=datetime.now())
        session.add(network)

        group1 = Group(id=1,
                       name="Class of Physics",
                       network_id=1)
        group2 = Group(id=2,
                       name="Class of Math",
                       network_id=1)
        group3 = Group(id=3,
                       name="Small Study Group",
                       network_id=1)
        for sg in [group1, group2, group3]:
            session.add(sg)

        session.flush()
        self.assertTrue(str(network).startswith('<Network'),
                        msg="str(Network) must start with '<Network'")
        self.assertEqual(network.groups, [group1, group2, group3])
        self.assertEqual(network, group1.network)
        self.assertEqual(network, group2.network)
        self.assertEqual(network, group3.network)

    def testQuestions(self):
        session = self.Session()

        question = Question(id=1,
                            created=datetime.now(),
                            founder_id=1)

        session.add(question)
        self.assertTrue(str(question).startswith('<Question'),
                        msg="str(Question) must start with '<Question'")

    def testQuestionHistory(self):
        session = self.Session()

        question = Question(id=1,
                            created=datetime.now(),
                            founder_id=1)

        question_rev = QuestionHistory(revision=1,
                                       created=datetime.now(),
                                       author_id=1,
                                       question_id=1,
                                       body="This is a question.")

        question.history.append(question_rev)
        session.add(question)
        session.flush()
        self.assertTrue(str(question_rev).startswith('<QuestionHistory'),
                        msg="str(QuestionHistory) must start with '<QuestionHistory'")
        self.assertEqual(question_rev.question, question)
        self.assertEqual(question.history, [question_rev])

    def testQuestionComments(self):
        session = self.Session()

        question = Question(id=1,
                            created=datetime.now(),
                            founder_id=1)
        comment = Comment(id=1,
                          founder_id=1)
        question_comment = QuestionComment(question_id=1,
                                       comment_id=1)
        session.add(question)
        session.add(comment)
        session.add(question_comment)

        session.flush()
        self.assertTrue(str(question_comment).startswith('<QuestionComment'),
                        msg="str(QuestionComment) must start with '<QuestionComment'")
        self.assertEqual(question_comment.question, question)
        self.assertEqual(question_comment.comment, comment)
        self.assertEqual(question_comment, comment.question_comment)
        self.assertIn(question_comment, question.question_comments)

    def testGroups(self):
        session = self.Session()

        group = Group(id=1,
                      name="My cool group",
                      created=datetime.now(),
                      edited=datetime.now())
        post = Post(id=1,
                    founder_id=1,
                    group_id=1)
        group.posts.append(post)

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        session.add(user)

        moderator = Moderator(user_id=1,
                              group_id=1)
        group.moderator.append(moderator)

        session.add(group)
        session.flush()
        self.assertTrue(str(group).startswith('<Group'),
                        msg="str(Group) must start with '<Group'")
        self.assertIn(post, group.posts)
        self.assertEqual(post.group, group)
        self.assertIn(user, group.moderators)
        self.assertIn(group, user.moderated_groups)

    def testSubscriptions(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        group = Group(id=1,
                      name="My cool group",
                      created=datetime.now(),
                      edited=datetime.now())
        subscription = Subscription(user_id=1,
                                    group_id=1)

        session.add(group)
        session.add(user)
        session.add(subscription)

        session.flush()
        self.assertTrue(str(subscription).startswith('<Subscription'),
                        msg="str(Subscription) must start with '<Subscription'")
        self.assertIn(group, user.subscribed_groups)
        self.assertIn(user, group.subscribers)

    def testUsers(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        auth_user = AuthUser('jayd3e', 'secret')
        post = Post(id=1,
                    founder_id=1,
                    group_id=1)
        question = Question(id=1,
                            created=datetime.now(),
                            founder_id=1)
        group = Group(id=1,
                      name="My cool group",
                      created=datetime.now(),
                      edited=datetime.now())
        comment = Comment(id=1)

        user.auth_user = auth_user
        user.posts.append(post)
        user.questions.append(question)
        user.founded_groups.append(group)
        user.comments.append(comment)
        session.add(user)

        # Moderator of founded group
        moderator = Moderator(user_id=1,
                              group_id=1)
        session.add(moderator)

        # Subscribed to founded group
        subscription = Subscription(user_id=1,
                                    group_id=1)
        session.add(subscription)

        session.flush()
        self.assertTrue(str(subscription).startswith('<Subscription'),
                        msg="str(Subscription) must start with '<Subscription'")
        self.assertEqual(user.auth_user, auth_user)
        self.assertEqual(auth_user.user, user)
        self.assertIn(post, user.posts)
        self.assertEqual(post.founder, user)
        self.assertIn(question, user.questions)
        self.assertEqual(question.founder, user)
        self.assertIn(group, user.founded_groups)
        self.assertEqual(user, group.founder)
        self.assertIn(comment, user.comments)
        self.assertEqual(user, comment.founder)
        self.assertIn(group, user.subscribed_groups)
        self.assertIn(user, group.subscribers)
        self.assertIn(user, group.moderators)
        self.assertIn(group, user.moderated_groups)

    def testVotes(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        group = Group(id=1,
                      name="My cool group",
                      created=datetime.now(),
                      edited=datetime.now())
        comment = Comment(id=1,
                          founder_id=1)
        #upvote
        vote = Vote(id=1,
                    user_id=1,
                    comment_id=1,
                    vote=1)

        session.add(group)
        session.add(user)
        session.add(comment)
        session.add(vote)

        session.flush()
        self.assertTrue(str(vote).startswith('<Vote'),
                        msg="str(Vote) must start with '<Vote'")
        self.assertIn(vote, user.votes)
        self.assertEqual(user, vote.user)
        self.assertIn(vote, comment.votes)
        self.assertEqual(comment, vote.comment)

    def testMemberships(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        network = Network(id=1,
                          name="Uni of Iowa",
                          created=datetime.now())
        membership = Membership(id=1,
                                user_id=1,
                                network_id=1)

        session.add(user)
        session.add(network)
        session.add(membership)

        session.flush()
        self.assertTrue(str(membership).startswith('<Membership'),
                        msg="str(Membership) must start with '<Membership'")
        self.assertIn(network, user.memberships)
        self.assertEqual(network, membership.network)
        self.assertIn(user, network.members)
        self.assertEqual(user, membership.user)

    def testBroadcasts(self):
        session = self.Session()

        question = Question(id=1,
                            created=datetime.now(),
                            founder_id=1)
        group = Group(id=1,
                      name="My cool group",
                      created=datetime.now(),
                      edited=datetime.now())
        broadcast = Broadcast(id=1,
                              question_id=1,
                              group_id=1)

        session.add(question)
        session.add(group)
        session.add(broadcast)

        session.flush()
        self.assertTrue(str(broadcast).startswith('<Broadcast'),
                        msg="str(Broadcast) must start with '<Broadcast'")
        self.assertIn(question, group.questions)
        self.assertIn(group, question.groups)
        self.assertEqual(question, broadcast.question)
        self.assertEqual(group, broadcast.group)

    def testGroupInviteNotifiions(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        group = Group(id=1,
                      name="My cool group",
                      created=datetime.now(),
                      edited=datetime.now())
        session.add(user)
        session.add(group)

        group_invite_notification = GroupInviteNotification(created=datetime.now(),
                                                            discriminator="group_invite",
                                                            user_id=1,
                                                            group_id=1)
        session.add(group_invite_notification)
        session.flush()

        notification = Notification(user_id=1,
                                    notification_item_id=group_invite_notification.id)
        session.add(notification)
        session.flush()
        self.assertTrue(str(notification).startswith('<Notification'),
                        msg="str(Notification) must start with '<Notification'")

        notification_item = NotificationItem(created=datetime.now(),
                                             discriminator="group_invite")
        self.assertTrue(str(notification_item).startswith('<NotificationItem'),
                        msg="str(NotificationItem) must start with '<NotificationItem'")

        self.assertTrue(str(group_invite_notification).startswith('<GroupInviteNotification'),
                        msg="str(GroupInviteNotification) must start with '<GroupInviteNotification'")
        self.assertIn(group_invite_notification, user.notifications)
        self.assertEqual(user, notification.user)
        self.assertEqual(user, group_invite_notification.inviter)
        self.assertEqual(group, group_invite_notification.group)

    def testQuestionCommentNotifications(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        question = Question(id=1,
                            created=datetime.now(),
                            founder_id=1)
        comment = Comment(id=1,
                          founder_id=1)
        question_comment = QuestionComment(question_id=1,
                                           comment_id=1)
        session.add(user)
        session.add(question)
        session.add(comment)
        session.add(question_comment)
        session.flush()

        question_comment_notification = QuestionCommentNotification(created=datetime.now(),
                                                                    discriminator="question_comment",
                                                                    user_id=user.id,
                                                                    comment_id=comment.id,
                                                                    question_id=question.id)
        session.add(question_comment_notification)
        session.flush()

        notification = Notification(user_id=user.id,
                                    notification_item_id=question_comment_notification.id)
        session.add(notification)
        session.flush()
        self.assertTrue(str(question_comment_notification).startswith('<QuestionCommentNotification'),
                        msg="str(QuestionCommentNotification) must start with '<QuestionCommentNotification'")
        self.assertIn(question_comment_notification, user.notifications)
        self.assertEqual(user, notification.user)
        self.assertEqual(user, question_comment_notification.commenter)
        self.assertEqual(comment, question_comment_notification.comment)
        self.assertEqual(question, question_comment_notification.question)
