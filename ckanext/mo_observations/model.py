import re
import uuid

from sqlalchemy import Table, Column, MetaData, ForeignKey
from sqlalchemy import types
from sqlalchemy.sql import select
from sqlalchemy.orm import mapper, relation
from sqlalchemy import func

import ckan.model as model
from ckan.lib.base import *

log = __import__('logging').getLogger(__name__)


def make_uuid():
    return unicode(uuid.uuid4())

metadata = MetaData()

class TimeStep(object):

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find(cls, timestamp):
        q = model.Session.query(TimeStep).filter(TimeStep.when==timestamp)
        return q.first()

    def __str__(self):
        return u"<Ruleset: %s, %s>" % (self.publisher_name, self.url_regex)

timestep_table = Table('mo_timesteps', metadata,
                      Column('id', types.UnicodeText, primary_key=True,
                             default=make_uuid),
                      Column('when', types.DateTime),
                )
mapper(TimeStep, timestep_table)

"""
class Ruleset(object):

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find(cls, publisher_name, url):
        query = "select * from lf_ruleset where publisher_name=:pub and :url ~ url_regex"
        q = model.Session.query(Ruleset).from_statement(query).params(url=url,pub=publisher_name)
        return q.first()

    def __str__(self):
        return u"<Ruleset: %s, %s>" % (self.publisher_name, self.url_regex)

ruleset_table = Table('lf_ruleset', metadata,
                      Column('id', types.UnicodeText, primary_key=True,
                             default=make_uuid),
                      Column('publisher_name', types.UnicodeText),
                      Column('url_regex', types.UnicodeText),
                      Column('follow_link', types.UnicodeText),
                      Column('xpath', types.UnicodeText),
                      Column('css', types.UnicodeText),
                      Column('link_regex', types.UnicodeText),
                      Column('link_text_regex', types.UnicodeText),
                      Column('allow_multiple', types.Integer),
                )
mapper(Ruleset, ruleset_table)

"""

def init_tables():
    metadata.create_all(model.meta.engine)

