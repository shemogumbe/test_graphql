import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene import relay, Schema, ObjectType
from models import User, Story,db_session


class UserType(SQLAlchemyObjectType):   
    class Meta:        
        model = User        
        interfaces = (relay.Node,)

class StoryType(SQLAlchemyObjectType):    
    class Meta:        
        model = User       
        interfaces = (relay.Node,)


class UpdateUsername(graphene.Mutation):
	class Arguments:
		username = graphene.String()
		email = graphene.String()

	user = graphene.Field(UserType)

	def mutate(self,info,email,username):   
		query = UserType.get_query(info)
		user = query.filter(User.email == email).first()
		user.username = username
		db_session.commit()
		
		return UpdateUsername(user=user)

class Query(ObjectType):   
    node = relay.Node.Field()    
    user = SQLAlchemyConnectionField(StoryType)

class SocialMutation(graphene.ObjectType):
	update_username = UpdateUsername.Field()

schema = Schema(query=Query,mutation=SocialMutation)