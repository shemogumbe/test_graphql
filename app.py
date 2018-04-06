from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models import Base

app = Flask(__name__)

app.add_url_rule('/social',view_func=GraphQLView.as_view('social',schema=schema,graphiql=True ))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    engine = create_engine("sqlite:///graph_db.sqlite")
    db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
    
    Base.query = db_session.query_property()
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    app.run()

