import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import User, Story, save


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class StoryType(SQLAlchemyObjectType):
    class Meta:
        model = Story
        interfaces = (relay.Node, )


class CreateStory(graphene.Mutation):
    class Arguments:
        story = graphene.String()
        user_id = graphene.Int()
    story = graphene.Field(StoryType)

    def mutate(self, info, **kwargs):
        story = Story(**kwargs)
        save(story)

        return CreateStory(story=story)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(UserType)
    user_stories = SQLAlchemyConnectionField(StoryType)


class SocialMutations(graphene.ObjectType):
    create_story = CreateStory.Field()

schema = Schema(query=Query, mutation=SocialMutations)
