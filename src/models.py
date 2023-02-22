import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, ForeignKey("User.ID"), primary_key=True)
    user_to_id = Column(Integer, ForeignKey("User.ID"))
    #Relationship
    User = relationship("User")


class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    #Relationship   


    def to_dict(self):
        return {}

class Comment(Base):
        __tablename__ = "Comment"
        ID = Column(Integer, primary_key=True)
        comment_text = Column(String(250), nullable=False)
        author_id = Column(Integer, ForeignKey("User.ID"), nullable=False)
        post_id = Column(Integer, ForeignKey("Post.ID"), nullable=False)

        User = relationship("User")
        Post = relationship("Post")


class Media(Base):
        __tablename__ = "Media"
        ID = Column(Integer, primary_key=True)
        type = Column(String(25), nullable=False)
        url = Column(String(250))
        post_id = Column(Integer, ForeignKey("Post.ID"), nullable=False)

        Post = relationship("Post")

class Post(Base):
        __tablename__ = "Post"
        ID = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey("User.ID"), primary_key=True)

        User = relationship("User")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
