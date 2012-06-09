import random
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clusterflunk.models.networks import Network
from clusterflunk.models.users import User
from clusterflunk.models.auth import AuthUser
from clusterflunk.models.memberships import Membership
from clusterflunk.models.study_groups import StudyGroup
from clusterflunk.models.posts import Post
from clusterflunk.models.posts import PostComment
from clusterflunk.models.subscriptions import Subscription
from clusterflunk.models.articles import Article
from clusterflunk.models.articles import ArticleHistory
from clusterflunk.models.posts import PostHistory
from clusterflunk.models.comments import Comment
from clusterflunk.models.comments import CommentHistory
from clusterflunk.models.statuses import Status
from clusterflunk.models.statuses import StatusHistory
from clusterflunk.models.broadcasts import Broadcast

statuses = ['I love studying <3',
            'How do I do this hard problem?',
            'Can anyone else in this group solve problem 1A?',
            'Anyone done with the circuits hw yet?',
            'How do you interpret this piece of art?']


def reply(session, _id):
    comment = Comment(parent_id=_id,
                      founder_id=1,
                      created=datetime.now())
    session.add(comment)
    session.flush()
    comment_rev = CommentHistory(revision=1,
                                 created=datetime.now(),
                                 author_id=1,
                                 comment_id=comment.id,
                                 body="This is branch with parent_comment=" + str(_id) + " comment=" + str(comment.id))
    session.add(comment_rev)

    if random.randint(0, 1) == 1:
        reply(session, comment.id)


def data():
    num_of_groups = 3
    num_of_posts = 10
    num_of_articles = 10
    num_of_histories = 5
    num_of_comments = 5
    num_of_replies = 5
    num_of_statuses = 5

    engine = create_engine('postgresql+psycopg2://vagrant:fluffy&Bunny@localhost/clusterflunk')
    Session = sessionmaker(bind=engine)
    session = Session()

    network = Network(id=1,
                      name="Uni of Iowa",
                      created=datetime.now())
    session.add(network)

    user = User(id=1,
                username="jayd3e",
                email="jd.dallago@gmail.com",
                joined=datetime.now(),
                last_online=datetime.now())
    auth_user = AuthUser("jayd3e", "blah7")
    user.auth_user = auth_user
    session.add(user)

    membership = Membership(id=1,
                            user_id=1,
                            network_id=1)
    session.add(membership)

    for i in range(num_of_groups + 1):
        study_group = StudyGroup(id=int(i),
                                 name="Physics 10" + str(i),
                                 network_id=1,
                                 created=datetime.now(),
                                 edited=datetime.now(),
                                 founder_id=1)
        subscription = Subscription(user_id=1,
                                    study_group_id=int(i))
        session.add(subscription)
        session.add(study_group)

        for j in range(num_of_statuses + 1):
            status = Status(created=datetime.now(),
                            founder_id=1)
            session.add(status)
            session.flush()
            for k in range(num_of_histories + 1):
                status_len = len(statuses)
                status_num = random.randint(0, status_len - 1)

                status_rev = StatusHistory(revision=int(k),
                                           author_id=1,
                                           status_id=status.id,
                                           created=datetime.now(),
                                           body=statuses[status_num])
                status.history.append(status_rev)

            broadcast = Broadcast(status_id=status.id,
                                  study_group_id=int(i))
            session.add(broadcast)

        session.flush()

    for i in range(num_of_posts + 1):
        post = Post(id=int(i),
                    founder_id=1,
                    study_group_id=random.randint(1, num_of_groups),
                    created=datetime.now())
        session.add(post)
        session.flush()
        for j in range(num_of_histories + 1):
            post_rev = PostHistory(revision=int(j),
                                   author_id=1,
                                   post_id=post.id,
                                   created=datetime.now(),
                                   name="Post #" + str(i) + str(j),
                                   description="This is a description.  Version #" + str(j))
            post.history.append(post_rev)

        for k in range(num_of_comments + 1):
            comment = Comment(parent_id=None,
                              founder_id=1,
                              created=datetime.now())
            session.add(comment)
            session.flush()
            post_comment = PostComment(post_id=post.id,
                                       comment_id=comment.id)
            comment_rev = CommentHistory(revision=1,
                                         created=datetime.now(),
                                         author_id=1,
                                         comment_id=comment.id,
                                         body="U Suk!")
            session.add(post_comment)
            session.add(comment_rev)

            for l in range(num_of_replies + 1):
                reply(session, comment.id)

    for i in range(num_of_articles + 1):
        article = Article(id=int(i),
                          founder_id=1,
                          created=datetime.now())
        for j in range(num_of_histories + 1):
            article_rev = ArticleHistory(title="Awesome Title",
                                         body="This explains a super complicated \
                                         topic.  And is revision " + str(j),
                                         revision=int(j),
                                         author_id=1,
                                         article_id=int(i),
                                         created=datetime.now())
            article.history.append(article_rev)
        session.add(article)

    session.flush()
    session.commit()

if __name__ == '__main__':
    data()