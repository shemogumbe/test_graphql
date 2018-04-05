from graphene import relay
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import User, Story

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class StoryObject(SQLAlchemyObjectType):
    class Meta:
        model = Story
        interfaces = (relay.Node, )
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(UserObject)
    user_stories = SQLAlchemyConnectionField(StoryObject)
    story = graphene.relay.Node.Field(StoryObject)

    


schema = graphene.Schema(query=Query)