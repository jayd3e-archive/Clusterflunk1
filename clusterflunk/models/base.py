from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base
from clusterflunk.util import get_timedelta_string


class Base(object):
    id = Column(Integer, primary_key=True)

    @property
    def created_timedelta(self):
        if hasattr(self, 'created'):
            return get_timedelta_string(self.created)
        else:
            return None

Base = declarative_base(cls=Base)


def initializeBase(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
