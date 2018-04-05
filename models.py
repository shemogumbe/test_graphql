from sqlalchemy import Column, String, Integer, ForeignKey, func,DateTime
from sqlalchemy.orm import relationship,scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine




engine = create_engine('sqlite:///graph_db.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

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
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=func.now())
    


