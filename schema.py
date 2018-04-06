from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay, Schema, ObjectType, Mutation, String, Field, Boolean
from models import User, Story, db_session, save


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)

class CreateUser(Mutation):
  user = Field(UserType)

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


class StoryType(SQLAlchemyObjectType): 
    class Meta:
        model = User
        interfaces = (relay.Node,)


class Query(ObjectType):
  node = relay.Node.Field()
  all_user = SQLAlchemyConnectionField(UserType)

class SocualMutations(ObjectType):
  create_user = CreateUser.Field()


schema = Schema(query=Query, mutation=SocualMutations)
