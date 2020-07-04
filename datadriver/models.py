"""
Created by Epic at 7/4/20
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, Integer, DateTime, String

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT, primary_key=True, unique=True)
    messages = Column(Integer)
    join_date = Column(DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, messages=f{self.messages}, join_date=f{self.join_date})>"


class Ban(Base):
    __tablename__ = "bans"

    id = Column(BIGINT, primary_key=True, unique=True)
    banned_at = Column(DateTime)
    expires_at = Column(DateTime)

    reason = Column(String)
