import re
import uuid

from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy import types, orm
from sqlalchemy.sql import select
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

import ckan.model as model
from ckan.lib.base import *

log = __import__('logging').getLogger(__name__)

Base = declarative_base()

def make_uuid():
    return unicode(uuid.uuid4())

metadata = MetaData()

class TimeStep(Base):
    """
    """
    __tablename__ = 'mo_timestep'
    id = Column(types.UnicodeText,
           primary_key=True,
           default=make_uuid)
    when = Column(types.DateTime)

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find(cls, timestamp):
        q = model.Session.query(TimeStep).filter(TimeStep.when==timestamp)
        return q.first()

    def __str__(self):
        return u"<TimeStep: %s>" % (self.when)



class Location(Base):
    """
    """
    __tablename__ = 'mo_location'

    id = Column(types.UnicodeText,
           primary_key=True,
           default=make_uuid)
    lat = Column(types.UnicodeText)
    lon = Column(types.UnicodeText)
    lat = Column(types.UnicodeText)
    name = Column(types.UnicodeText)
    country = Column(types.UnicodeText)
    continent = Column(types.UnicodeText)

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def get(cls, name):
        l = model.Session.query(Location).filter(Location.name==name).first()
        if not l:
          l = model.Session.query(Location).filter(TimeStep.id==name).first()
        return l

    def __str__(self):
        return u"<Location: %s>" % (self.name)


class Observation(Base):
    """
    """
    __tablename__ = 'mo_observation'

    id = Column(types.UnicodeText,
           primary_key=True,
           default=make_uuid)
    weather_type = Column( types.UnicodeText)
    visibility = Column( types.UnicodeText)
    temperature = Column(types.UnicodeText)
    wind_speed = Column(types.UnicodeText)
    pressure = Column(types.UnicodeText)
    wind_gust = Column(types.UnicodeText)
    wind_direction = Column(types.UnicodeText)
    timestep_id = Column(types.UnicodeText, ForeignKey('mo_timestep.id'), nullable=False)
    location_id = Column(types.UnicodeText, ForeignKey('mo_location.id'), nullable=False)
    location = relationship(Location,primaryjoin="Observation.location_id==Location.id")
    timestep = relationship(TimeStep,primaryjoin="Observation.timestep_id==TimeStep.id", backref='observations')

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return u"<Observation: %s, %s>" % (self.name)

def init_tables():
    Base.metadata.create_all(model.meta.engine)
