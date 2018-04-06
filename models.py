from sqlalchemy import Column, String, Integer, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

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
    user_id = Column(Integer, ForeignKey(User.id))
    created_at = Column(DateTime, default=func.now())
    


