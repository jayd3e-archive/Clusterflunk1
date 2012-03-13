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
from clusterflunk.models.subscriptions import Subscription

def data():
    num_of_groups = 3
    num_of_posts = 10

    engine = create_engine('postgresql+psycopg2://jayd3e:sharp7&7@localhost/clusterflunk')
    Session = sessionmaker(bind=engine, autocommit=True)
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
                                 edited=datetime.now())
        subscription = Subscription(user_id=1,
                                    study_group_id=int(i))
        session.add(subscription)
        session.add(study_group)

    for i in range(num_of_posts + 1):
        post = Post(id=int(i),
                    title="Post #" + str(i),
                    founder_id=1,
                    study_group_id=random.randint(1, num_of_groups))
        session.add(post)
    
    session.flush()

if __name__ == '__main__':
    data()