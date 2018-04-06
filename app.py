from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User,Story,Base,engine,db_session
from flask_graphql import  GraphQLView
from schema import schema


engine = create_engine("sqlite:///graph_db.sqlite")

app = Flask(__name__)
app.add_url_rule('/social', view_func=GraphQLView.as_view('social',schema=schema, graphiql=True))
# Session = sessionmaker()
# session = Session(bind=engine)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)

