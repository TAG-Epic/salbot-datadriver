"""
Created by Epic at 7/4/20
"""
from sqlalchemy import create_engine
from .models import User, Base
from sqlalchemy.orm import sessionmaker


class DatabaseClient:
    def __init__(self, uri, echo=False):
        self.engine = create_engine(uri, echo=echo)
        self.session = sessionmaker(bind=self.engine)()
        self.base = Base
        self.base.metadata.create_all(self.engine)

    def create_user(self, id, join_date, messages):
        user = User(id=id, join_date=join_date, messages=messages)
        self.session.add(user)

    def save(self):
        self.session.commit()
