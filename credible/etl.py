import datetime

from sqlalchemy import Table, MetaData, Column
from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy import ForeignKey
from sqlalchemy.ext import declarative
from contextlib import contextmanager

Base = declarative.declarative_base()


class Etl:
    def __init__(self, Base, Session, engine):
        """
        Custom etl wrapper for SqlAlchemy. Implements Basic ETL operations for tables.
        """
        self.Base = Base
        self.Session = Session
        self.engine = engine

    def create_all(self):
        """
        Create all tables.
        """
        self.Base.metadata.drop_all(bind=self.engine)
        self.Base.metadata.create_all(bind=self.engine)

    def insert(self, obj_list, batch_size=-1):
        """
        Insert function.
        """
        if batch_size == -1:
            with self.session_scope() as session:
                session.add_all(obj_list)
        else:
            # todo: divide obj_list into batches, insert in loop.
            pass

    def bulk_insert(self, mapper, mappings, *args):
        """
        Bulk insert wrapper of SqlAlchemy.
        """

        with self.session_scope() as session:
            if issubclass(mappings[0].__class__, Base):
                session.bulk_save_objects(mappings)
            else:
                session.bulk_insert_mappings(mapper, mappings, *args)

    @contextmanager
    def session_scope(self):
        """
        Effective usage of session for an operation. Use `with` scope.
        """
        session = self.Session()

        try:
            yield session
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            session.close()


class Photo(Base):
    __tablename__ = 'photos'
    _id = Column('_id', Integer(), primary_key=True, autoincrement=True)
    photo_id = Column('photo_id', String(22))
    business_id = Column('business_id', String(22))
    caption = Column('caption', String(150))
    label = Column('label', String(10))

    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            setattr(self, key, value)


class Business(Base):
    __tablename__ = 'businesses'

    _id = Column('_id', Integer(), primary_key=True, autoincrement=True)
    business_id = Column(String(150))
    name = Column(String(22))
    address = Column(String(22))
    city = Column(String(10))
    state = Column(String(10))
    postal_code = Column(String(20))
    latitude = Column(Float(6))
    longitude = Column(Float(6))
    starts = Column(Float(1))
    review_count = Column(Integer())

    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            setattr(self, key, value)


class Checkin(Base):
    __tablename__ = 'checkins'

    _id = Column('_id', Integer, primary_key=True)
    business_id = Column(String(22))
    date = Column(String())

    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            setattr(self, key, value)


class Tip(Base):
    __tablename__ = 'tips'

    _id = Column(Integer, primary_key=True)
    user_id = Column(String(22))
    business_id = Column(String(22))
    text = Column(String(500))
    date = Column(DateTime())
    compliment_count = Column(Integer())

    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            if key == 'date':
                value = datetime.datetime.strptime(
                    value, r'%Y-%m-%d %H:%M:%S')
            setattr(self, key, value)
