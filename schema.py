from graphene import relay
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import User, Story

class User(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class Story(SQLAlchemyObjectType):
    class Meta:
        model = Story
        interfaces = (relay.Node, )
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(User)
    User_stories = SQLAlchemyConnectionField(Story)
    


schema = graphene.Schema(query=Query)