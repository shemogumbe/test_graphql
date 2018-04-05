from sqlalchemy import Column, String, Integer, ForeignKey, func, DateTime,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine('sqlite:///graph_db.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.metadata.create_all(engine)
Base.query = db_session.query_property()

class UtilityMethods:
    def save(self):
        if not self.id:
            db_session.add(self)
        return db_session.commit()

class User(Base, UtilityMethods):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    stories = relationship('Story')


class Story(Base,UtilityMethods):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    story = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=func.now())
    


