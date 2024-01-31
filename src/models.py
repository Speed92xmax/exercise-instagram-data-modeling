import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base) :
    __tablename__="user"

    id = Column ( Integer, primary_key=True)
    name = Column (String(100),nullable=False)
    email = Column (String(100),nullable=False)
    password = Column (String(100),nullable=False)
    follows_list = relationship("follows_list")
    followers_list = relationship("followers_list")
    posts_list = relationship("posts_list")
    fav_post_list = relationship("fav_posts_list")

class FollowsList (Base):
    __tablename__="follows_list"

    id = Column ( Integer, primary_key=True)
    follow_user= relationship("follow_user")
    user_id= Column( Integer, ForeignKey("user.id"),nullable=False)

class FollowersList (Base):
    __tablename__="followers_list"

    id = Column ( Integer, primary_key=True)
    follower_user= relationship("follower_user")
    user_id= Column( Integer, ForeignKey("user.id"),nullable=False)


class PostsList (Base):
    __tablename__="posts_list"

    id = Column ( Integer, primary_key=True)
    post = relationship("post")
    user_id= Column( Integer, ForeignKey("user.id"),nullable=False)


class FavPostList (Base):
    __tablename__="fav_post_list"

    id = Column ( Integer, primary_key=True)
    fav_post= relationship("fav_post")
    user_id= Column( Integer, ForeignKey("user.id"),nullable=False)

class FollowUser (Base):
    __tablename__="follow_user"

    id = Column ( Integer, primary_key=True)
    name = Column (String(100),nullable=False)
    follows_list_id= Column( Integer, ForeignKey("follows_list.id"))

class FollowerUser (Base):
    __tablename__="follower_user"

    id = Column ( Integer, primary_key=True)
    name = Column (String(100),nullable=False)
    followers_list_id= Column( Integer, ForeignKey("followers_list.id"))

class Post (Base):
    __tablename__="post"

    id = Column ( Integer, primary_key=True)
    content = Column (String(350),nullable=False)
    posts_list_id= Column( Integer, ForeignKey("posts_list.id"))

class FavPost (Base):
    __tablename__="fav_post"

    id = Column ( Integer, primary_key=True)
    content = Column (String(350),nullable=False)
    fav_post_list_id= Column( Integer, ForeignKey("fav_post_list.id"))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
