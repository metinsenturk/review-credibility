import json
import datetime
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.ext import declarative
from sqlalchemy import ForeignKey

Base = declarative.declarative_base()


class Review(Base):
    __tablename__ = 'reviews'
    _id = Column('_id', Integer(), primary_key=True, autoincrement=True)
    review_id = Column(String(22))
    business_id = Column(String(22))
    user_id = Column(String(22))
    stars = Column(Integer())
    date = Column(String(10))
    text = Column(String())
    useful = Column(Integer())
    funny = Column(Integer())
    cool = Column(Integer())

    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            setattr(self, key, value)


class User(Base):
    __tablename__ = 'users'
    _id = Column('_id', Integer(), primary_key=True, autoincrement=True)
    user_id = Column(String(22))
    name = Column(String())
    review_count = Column(String())
    yelping_since = Column(String(10))
    friends = Column(String())
    useful = Column(Integer())
    funny = Column(Integer())
    cool = Column(Integer())
    fans = Column(Integer())
    elite = Column(String())
    average_stars = Column(Integer())
    compliment_hot = Column(Integer())
    compliment_more = Column(Integer())
    compliment_profile = Column(Integer())
    compliment_cute = Column(Integer())
    compliment_list = Column(Integer())
    compliment_note = Column(Integer())
    compliment_plain = Column(Integer())
    compliment_cool = Column(Integer())
    compliment_funny = Column(Integer())
    compliment_writer = Column(Integer())
    compliment_photos = Column(Integer())

    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            setattr(self, key, value)


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
    is_open = Column(Integer())
    attributes = Column(String())
    categories = Column(String())
    hours = Column(String())


    def __init__(self, data=None, *args, **kwargs):
        # init with a dict
        for key, value in data.items():
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
                setattr(self, key, value)
            else:
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
