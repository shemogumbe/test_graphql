from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay, Schema, ObjectType, Mutation, String, Field, Boolean
from models import User, Story, save



class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )

class CreateUser(Mutation):
  user = Field(UserObject)

  class Arguments:
    first_name = String()
    last_name = String()
    username = String(required=True)
    password = String(required=True)
    email = String(required=True)
  ok = Boolean()

  def mutate(self, info, **kwargs):
    user = User(**kwargs)
    save(user)
    ok = True
    return CreateUser(user=user, ok=ok)

class StoryObject(SQLAlchemyObjectType):
    class Meta:
        model = Story
        interfaces = (relay.Node, )

class Mutations(ObjectType):
  create_user = CreateUser.Field()

class Query(ObjectType):
    users = SQLAlchemyConnectionField(UserObject)
    user_stories = SQLAlchemyConnectionField(StoryObject)
    story = relay.Node.Field(StoryObject)


schema = Schema(query=Query, mutation=Mutations)

