import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er 

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, index=True)
    firstname = Column(String(25),nullable=False)
    lastname = Column(String(25),nullable=False)
    email = Column(String(30),nullable=False,unique=True)

    def serialize(self):
        return{
            'id' : self.id,
            'username' : self.username,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'email' : self.email,

        }

class Follower(Base):
    __tablename__ = 'follower'

    user_from_id = Column(Integer,ForeignKey(User.id), primary_key=True)
    user_to_id = Column(Integer,ForeignKey(User.id))

    def serialize(self):
        return{
            'user_from_id' : self.user_from_id,
            'user_to_id' : self.user_to_id,
        }   


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey(User.id))


    def serialize(self):
        return{
            'id' : self.id,
            'user_id' : self.user_id
        }
    

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(25))
    author_id = Column(Integer,ForeignKey(User.id))
    post_id = Column(Integer,ForeignKey(Post.id))
    

    def serialize(self):
        return{
            'id' : self.id,
            'comment_text' : self.comment_text,
            'author_id' : self.author_id,
            'post_id' : self.post_id,
        }
    

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type =  Column(Enum,nullable=False)
    url = Column(String(30),nullable=False)
    post_id = Column(Integer, ForeignKey(Post.id))
   

    def serialize(self):
        return{
            'id' : self.id,
            'type' : self.type,
            'url' : self.url,
            'post_id' : self.post_id,
        }

    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
