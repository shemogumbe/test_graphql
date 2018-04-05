from flask import Flask
from flask_graphql import GraphQLView
from Schema import schema
from sqlalchemy import create_engine
from models import Base,db_session


app = Flask(__name__)

app.add_url_rule('/social',view_func=GraphQLView.as_view('social',schema=schema,graphiql=True))
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
if __name__ == '__main__':
    # engine = create_engine("sqlite:///graph_db.sqlite")
    # Base.metadata.create_all(engine)
    # Session = sessionmaker()
    # session = Session(bind=engine)
    app.run(debug=True)