import enum

import sqlalchemy as sa
from sqlalchemy import Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# define models
class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String, unique=True)
    age = sa.Column(sa.Integer)
    password_hash = sa.Column(sa.Text)

    posts = relationship(
        "Post",
        back_populates="author",
        cascade="all, delete-orphan",
    )
    likes = relationship(
        "Likes",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    dislikes = relationship(
        "Dislikes",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    body = sa.Column(sa.TEXT)
    author_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
    likes = relationship("Likes", back_populates="post", lazy='dynamic', uselist=True)
    dislikes = relationship("Dislikes", back_populates="post", lazy='dynamic', uselist=True)


class Likes(Base):
    __tablename__ = 'likes'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    post_id = sa.Column(sa.Integer, sa.ForeignKey("posts.id"))

    user = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes", lazy='dynamic', uselist=True)


class Dislikes(Base):
    __tablename__ = 'dislikes'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    post_id = sa.Column(sa.Integer, sa.ForeignKey("posts.id"))

    user = relationship("User", back_populates="dislikes")
    post = relationship("Post", back_populates="dislikes", lazy='dynamic', uselist=True)
