"""
Created by Epic at 7/4/20
"""

from sqlalchemy import Column, BIGINT, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def jsonify_ban(ban):
    return {
        "id": ban.id,
        "reason": ban.reason,
        "banned_at": ban.banned_at.timestamp(),
        "expires_at": None if ban.expires_at.timestamp() == 0 else ban.expires_at.timestamp()
    }


def jsonify_user(user):
    return {
        "id": user.id,
        "messages": user.messages,
        "join_date": user.join_date.timestamp()
    }


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
