from graphene import relay
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import User as UserModel, Story

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Story(SQLAlchemyObjectType):
    class Meta:
        model = Story
        interfaces = (relay.Node, )
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(User)
    User_stories = SQLAlchemyConnectionField(Story)
    find_user = graphene.relay.Node.Field(User)
    


schema = graphene.Schema(query=Query, types=[User,Story])