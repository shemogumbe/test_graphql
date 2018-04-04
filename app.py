from flask import Flask
from models import Base
from flask_graphql import GraphQLView
from sqlalchemy.orm import sessionmaker

from schema import schema

app = Flask(__name__)

app.add_url_rule('/social', view_func=GraphQLView.as_view('social',schema=schema, graphiql=True))



if __name__ == '__main__':
    app.run()

# 