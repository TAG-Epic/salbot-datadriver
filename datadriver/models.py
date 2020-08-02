"""
Created by Epic at 7/4/20
"""

from sqlalchemy import Column, BIGINT, Integer, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def jsonify_punishment(punishment):
    return {
        "punishment_id": punishment.punishment_id,
        "punishment_type": punishment.punishment_type,
        "expired": punishment.expired,
        "punished_id": punishment.punished_id,
        "moderator_id": punishment.moderator_id,
        "punished_at": punishment.punished_at.timestamp(),
        "expires_at": None if punishment.expires_at.timestamp() == 0 else punishment.expires_at.timestamp(),
        "reason": punishment.reason
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


class Punishment(Base):
    __tablename__ = "punishments"

    punishment_id = Column(String, primary_key=True, unique=True)
    punishment_type = Column(String)
    expired = Column(Boolean)

    punished_id = Column(BIGINT)
    moderator_id = Column(BIGINT)

    punished_at = Column(DateTime)
    expires_at = Column(DateTime)

    reason = Column(String)


class Faq(Base):
    __tablename__ = "faq"

    name = Column(String, primary_key=True, unique=True)
    description = Column(String)
