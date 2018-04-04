from sqlalchemy import Column, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    stories = relationship('Story')


class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    story = Column(String)
    user_id = Column(Integer, ForeignKey('users.id))
    created_at = Column(DateTime, default=func.now())
    


