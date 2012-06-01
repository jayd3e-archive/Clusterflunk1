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
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.networks import Network
from clusterflunk.models.categories import Category
from clusterflunk.models.categories import PostCategory
from clusterflunk.models.articles import (
    Article,
    ArticleHistory,
    ArticleComment,
)
from clusterflunk.models.posts import (
    Post,
    PostComment,
    PostHistory,
)
from clusterflunk.models.comments import (
    Comment,
    CommentHistory,
)
from clusterflunk.models.statuses import (
    Status,
    StatusComment
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
    StatusCommentNotification
)


class TestModels(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite://')
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def testArticles(self):
        session = self.Session()

        article = Article(id=1,
                          founder_id=1)
        article_rev1 = ArticleHistory(revision=1,
                                      created=datetime.now(),
                                      author_id=1,
                                      body="This is a helpful article.")
        article_rev2 = ArticleHistory(revision=2,
                                      created=datetime.now(),
                                      author_id=2,
                                      body="This is another helpful article.")
        article_rev3 = ArticleHistory(revision=3,
                                      created=datetime.now(),
                                      author_id=3,
                                      body="This is the last helpful article.")
        for ar in [article_rev1, article_rev2, article_rev3]:
            article.history.append(ar)
        session.add(article)

        comment = Comment(id=1,
                          founder_id=1)
        comment1 = Comment(id=2,
                           founder_id=1)
        comment2 = Comment(id=3,
                           founder_id=1)
        for c in [comment, comment1, comment2]:
            session.add(c)

        article_comment = ArticleComment(article_id=1,
                                         comment_id=1)
        article_comment1 = ArticleComment(article_id=1,
                                          comment_id=2)
        article_comment2 = ArticleComment(article_id=1,
                                          comment_id=3)
        for ac in [article_comment, article_comment1, article_comment2]:
            session.add(ac)

        session.flush()
        self.assertTrue(str(article).startswith('<Article'),
                        msg="str(Article) must start with '<Article'")
        self.assertEqual(article.history, [article_rev1, article_rev2, article_rev3])
        self.assertEqual(article_rev1.article, article)
        self.assertEqual(article_rev2.article, article)
        self.assertEqual(article_rev3.article, article)
        self.assertEqual(article.comments, [comment, comment1, comment2])
        self.assertEqual(comment.article, article)
        self.assertEqual(comment1.article, article)
        self.assertEqual(comment2.article, article)

    def testArticleComments(self):
        session = self.Session()

        article = Article(id=1,
                          founder_id=1)
        comment = Comment(id=1,
                          founder_id=1)
        article_comment = ArticleComment(article_id=1,
                                         comment_id=1)
        session.add(article)
        session.add(comment)
        session.add(article_comment)

        session.flush()
        self.assertTrue(str(article_comment).startswith('<ArticleComment'),
                        msg="str(ArticleComment) must start with '<ArticleComment'")
        self.assertEqual(article_comment.article, article)
        self.assertEqual(article_comment.comment, comment)
        self.assertEqual(article_comment, comment.article_comment)
        self.assertIn(article_comment, article.article_comments)

    def testArticleHistory(self):
        session = self.Session()

        article_rev = ArticleHistory(revision=1,
                                     created=datetime.now(),
                                     author_id=1,
                                     body="This is a helpful article.")
        session.add(article_rev)
        session.flush()
        self.assertTrue(str(article_rev).startswith('<ArticleHistory'),
                        msg="str(ArticleHistory) must start with '<ArticleHistory'")

    def testPosts(self):
        session = self.Session()

        post = Post(id=1,
                    founder_id=1,
                    study_group_id=1)

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

        category = Category(id=1,
                            name='Test')
        session.add(category)

        post_category = PostCategory(id=1,
                                     post_id=1,
                                     category_id=1)
        post.post_categories.append(post_category)

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
        self.assertIn(category, post.categories)

    def testPostComments(self):
        session = self.Session()

        post = Post(id=1,
                    founder_id=1,
                    study_group_id=1)
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

    def testCategories(self):
        session = self.Session()

        category = Category(id=1,
                            name='Test')
        post_category = PostCategory(id=1,
                                     category_id=1)

        post_category.category = category
        session.add(post_category)

        session.flush()
        self.assertTrue(str(category).startswith('<Category'),
                        msg="str(Category) must start with '<Category'")
        self.assertTrue(str(post_category).startswith('<PostCategory'),
                        msg="str(PostCategory) must start with '<PostCategory'")
        self.assertEqual(post_category.category, category)

    def testModerators(self):
        session = self.Session()

        study_group = StudyGroup(id=1,
                                 name="Physics 101",
                                 created=datetime.now(),
                                 edited=datetime.now())

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())

        moderator = Moderator(user_id=1,
                              study_group_id=1)

        session.add(study_group)
        session.add(user)
        session.add(moderator)

        session.flush()
        self.assertTrue(str(moderator).startswith('<Moderator'),
                        msg="str(Moderator) must start with '<Moderator'")
        self.assertIn(user, study_group.moderators)
        self.assertIn(study_group, user.moderated_groups)
        self.assertEqual(moderator.user, user)
        self.assertEqual(moderator.study_group, study_group)

    def testNetworks(self):
        session = self.Session()

        network = Network(id=1,
                          name="Uni of Iowa",
                          created=datetime.now())
        session.add(network)

        study_group1 = StudyGroup(id=1,
                                  name="Class of Physics",
                                  network_id=1)
        study_group2 = StudyGroup(id=2,
                                  name="Class of Math",
                                  network_id=1)
        study_group3 = StudyGroup(id=3,
                                  name="Small Study Group",
                                  network_id=1)
        for sg in [study_group1, study_group2, study_group3]:
            session.add(sg)

        session.flush()
        self.assertTrue(str(network).startswith('<Network'),
                        msg="str(Network) must start with '<Network'")
        self.assertEqual(network.study_groups, [study_group1, study_group2, study_group3])
        self.assertEqual(network, study_group1.network)
        self.assertEqual(network, study_group2.network)
        self.assertEqual(network, study_group3.network)

    def testStatuses(self):
        session = self.Session()

        status = Status(id=1,
                        created=datetime.now(),
                        body="I luv studying <3",
                        author_id=1)

        session.add(status)
        self.assertTrue(str(status).startswith('<Status'),
                        msg="str(Status) must start with '<Status'")

    def testStatusComments(self):
        session = self.Session()

        status = Status(id=1,
                        created=datetime.now(),
                        body="I luv studying <3",
                        author_id=1)
        comment = Comment(id=1,
                          founder_id=1)
        status_comment = StatusComment(status_id=1,
                                       comment_id=1)
        session.add(status)
        session.add(comment)
        session.add(status_comment)

        session.flush()
        self.assertTrue(str(status_comment).startswith('<StatusComment'),
                        msg="str(StatusComment) must start with '<StatusComment'")
        self.assertEqual(status_comment.status, status)
        self.assertEqual(status_comment.comment, comment)
        self.assertEqual(status_comment, comment.status_comment)
        self.assertIn(status_comment, status.status_comments)

    def testStudyGroups(self):
        session = self.Session()

        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        post = Post(id=1,
                    founder_id=1,
                    study_group_id=1)
        study_group.posts.append(post)

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        session.add(user)

        moderator = Moderator(user_id=1,
                              study_group_id=1)
        study_group.moderator.append(moderator)

        session.add(study_group)
        session.flush()
        self.assertTrue(str(study_group).startswith('<StudyGroup'),
                        msg="str(StudyGroup) must start with '<StudyGroup'")
        self.assertIn(post, study_group.posts)
        self.assertEqual(post.study_group, study_group)
        self.assertIn(user, study_group.moderators)
        self.assertIn(study_group, user.moderated_groups)

    def testSubscriptions(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        subscription = Subscription(user_id=1,
                                    study_group_id=1)

        session.add(study_group)
        session.add(user)
        session.add(subscription)

        session.flush()
        self.assertTrue(str(subscription).startswith('<Subscription'),
                        msg="str(Subscription) must start with '<Subscription'")
        self.assertIn(study_group, user.subscribed_groups)
        self.assertIn(user, study_group.subscribers)

    def testUsers(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        auth_user = AuthUser('jayd3e', 'secret')
        article = Article(id=1,
                          founder_id=1)
        post = Post(id=1,
                    founder_id=1,
                    study_group_id=1)
        status = Status(id=1,
                        created=datetime.now(),
                        body="I luv studying <3",
                        author_id=1)
        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        comment = Comment(id=1)

        user.auth_user = auth_user
        user.articles.append(article)
        user.posts.append(post)
        user.statuses.append(status)
        user.founded_groups.append(study_group)
        user.comments.append(comment)
        session.add(user)

        # Moderator of founded group
        moderator = Moderator(user_id=1,
                              study_group_id=1)
        session.add(moderator)

        # Subscribed to founded group
        subscription = Subscription(user_id=1,
                                    study_group_id=1)
        session.add(subscription)

        session.flush()
        self.assertTrue(str(subscription).startswith('<Subscription'),
                        msg="str(Subscription) must start with '<Subscription'")
        self.assertEqual(user.auth_user, auth_user)
        self.assertEqual(auth_user.user, user)
        self.assertIn(article, user.articles)
        self.assertEqual(article.founder, user)
        self.assertIn(post, user.posts)
        self.assertEqual(post.founder, user)
        self.assertIn(status, user.statuses)
        self.assertEqual(status.author, user)
        self.assertIn(study_group, user.founded_groups)
        self.assertEqual(user, study_group.founder)
        self.assertIn(comment, user.comments)
        self.assertEqual(user, comment.founder)
        self.assertIn(study_group, user.subscribed_groups)
        self.assertIn(user, study_group.subscribers)
        self.assertIn(user, study_group.moderators)
        self.assertIn(study_group, user.moderated_groups)

    def testVotes(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        post = Post(id=1,
                    founder_id=1,
                    study_group_id=1)
        #upvote
        vote = Vote(id=1,
                    user_id=1,
                    post_id=1,
                    vote=1)

        session.add(study_group)
        session.add(user)
        session.add(post)
        session.add(vote)

        session.flush()
        self.assertTrue(str(vote).startswith('<Vote'),
                        msg="str(Vote) must start with '<Vote'")
        self.assertIn(vote, user.votes)
        self.assertEqual(user, vote.user)
        self.assertIn(vote, post.votes)
        self.assertEqual(post, vote.post)

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

        status = Status(id=1,
                        created=datetime.now(),
                        body="I luv studying <3",
                        author_id=1)
        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        broadcast = Broadcast(id=1,
                              status_id=1,
                              study_group_id=1)

        session.add(status)
        session.add(study_group)
        session.add(broadcast)

        session.flush()
        self.assertTrue(str(broadcast).startswith('<Broadcast'),
                        msg="str(Broadcast) must start with '<Broadcast'")
        self.assertIn(status, study_group.statuses)
        self.assertIn(study_group, status.study_groups)
        self.assertEqual(status, broadcast.status)
        self.assertEqual(study_group, broadcast.study_group)

    def testGroupInviteNotifications(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        study_group = StudyGroup(id=1,
                                 name="My cool group",
                                 created=datetime.now(),
                                 edited=datetime.now())
        session.add(user)
        session.add(study_group)

        group_invite_notification = GroupInviteNotification(created=datetime.now(),
                                                            discriminator="group_invite",
                                                            user_id=1,
                                                            study_group_id=1)
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
        self.assertEqual(study_group, group_invite_notification.study_group)

    def testStatusCommentNotifications(self):
        session = self.Session()

        user = User(id=1,
                    username="jayd3e",
                    email="jd.dallago@gmail.com",
                    joined=datetime.now(),
                    last_online=datetime.now())
        status = Status(id=1,
                        created=datetime.now(),
                        body="I luv studying <3",
                        author_id=1)
        comment = Comment(id=1,
                          founder_id=1)
        status_comment = StatusComment(status_id=1,
                                       comment_id=1)
        session.add(user)
        session.add(status)
        session.add(comment)
        session.add(status_comment)
        session.flush()

        status_comment_notification = StatusCommentNotification(created=datetime.now(),
                                                                discriminator="status_comment",
                                                                user_id=user.id,
                                                                comment_id=comment.id,
                                                                status_id=status.id)
        session.add(status_comment_notification)
        session.flush()

        notification = Notification(user_id=user.id,
                                    notification_item_id=status_comment_notification.id)
        session.add(notification)
        session.flush()
        self.assertTrue(str(status_comment_notification).startswith('<StatusCommentNotification'),
                        msg="str(StatusCommentNotification) must start with '<StatusCommentNotification'")
        self.assertIn(status_comment_notification, user.notifications)
        self.assertEqual(user, notification.user)
        self.assertEqual(user, status_comment_notification.commenter)
        self.assertEqual(comment, status_comment_notification.comment)
        self.assertEqual(status, status_comment_notification.status)