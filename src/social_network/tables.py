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
    actions = relationship(
        "Action",
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
    actions = relationship("Action", back_populates="post")


class Action(Base):
    __tablename__ = 'actions'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    action_type = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    post_id = sa.Column(sa.Integer, sa.ForeignKey("posts.id"))

    user = relationship("User", back_populates="actions")
    post = relationship("Post", back_populates="actions")
