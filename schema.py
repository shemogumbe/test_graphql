from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay, Schema, ObjectType, Mutation, String, Field, Boolean
from models import User, Story, db_session


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)

class CreateUser(Mutation):
  user = Field(UserType)

  class Arguments:
    first_name = String(required=True)
    last_name = String(required=True)
    username = String(required=True)
    password = String(required=True)
    email = String(required=True)
  ok = Boolean()

  def mutate(self, info, first_name, last_name, username, password, email):
    user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
    db_session().add(user)
    db_session().commit()
    ok = True
    return CreateUser(user=user, ok=ok)


class StoryType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)


class Query(ObjectType):
  node = relay.Node.Field()
  all_user = SQLAlchemyConnectionField(UserType)

class MyMutations(ObjectType):
  create_user = CreateUser.Field()


schema = Schema(query=Query, mutation=MyMutations)
