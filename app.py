from flask import Flask
from flask_graphql import GraphQLView
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from schema import schema
from models import Base, db_session


app = Flask(__name__)

app.add_url_rule(
    '/social',
    view_func=GraphQLView.as_view(
        'social',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
if __name__ == '__main__':
    app.run(debug=True)

