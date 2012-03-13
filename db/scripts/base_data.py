from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clusterflunk.models.networks import Network
from clusterflunk.models.users import User
from clusterflunk.models.auth import AuthUser
from clusterflunk.models.memberships import Membership
from clusterflunk.models.study_groups import StudyGroup

def data():
    engine = create_engine('postgresql+psycopg2://jayd3e:sharp7&7@localhost/clusterflunk')
    Session = sessionmaker(bind=engine, autocommit=True)
    session = Session()

    network = Network(id=1,
                      name="Uni of Iowa",
                      created=datetime.now())
    session.add(network)

    study_group0 = StudyGroup(id=1,
                              name="Physics 101",
                              network_id=1,
                              created=datetime.now(),
                              edited=datetime.now())
    study_group1 = StudyGroup(id=2,
                              name="Physics 102",
                              network_id=1,
                              created=datetime.now(),
                              edited=datetime.now())
    study_group2 = StudyGroup(id=3,
                              name="Physics 103",
                              network_id=1,
                              created=datetime.now(),
                              edited=datetime.now())

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
    
    for group in [study_group0, study_group1, study_group2]:
        session.add(group)
    
    session.flush()

if __name__ == '__main__':
    data()