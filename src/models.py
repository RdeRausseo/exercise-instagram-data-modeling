import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(250), nullable=False)
    userName = Column(String(250), nullable=  False, unique=True)

    Followers = relationship("Followers", backref="user") #No voy a modificar el useList porque tal vez no está demás que me devuelva una list
    Follow = relationship("Followed", backref="user") 
    comments = relationship("Comment", backref="user") #Solo quiero ver un comentario a la vez del usario

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, autoincrement = True)
    userName = Column(String(250), nullable=False, unique= True)
    id_user_follower = Column(String(250), ForeignKey("user.id"), nullable = False)

class Followed(Base):
    __tablename__ = 'followed'
    id = Column(Integer, primary_key=True, autoincrement = True)
    userName = Column(String(250), nullable=True, unique =  True)
    id_user_follow = Column(Integer, ForeignKey("user.id"), nullable = False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement = True)
    content = Column(Text, nullable = False, unique = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    user = relationship("User", backref="posts")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key= True, autoincrement = True)
    comment = Column(Text, nullable = False)
    id_post = Column(Integer, ForeignKey("Post.id"), nullable = False)
    id_user = Column(Integer, ForeignKey("user.id"), nullable = False) 
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
