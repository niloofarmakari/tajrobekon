import graphene

from apps.experience.graphql.root import ExperienceRoot


class Query(graphene.ObjectType):
    experience = graphene.Field(ExperienceRoot)

    def resolve_experience(self, info, **kwargs):
        return ExperienceRoot()


schema = graphene.Schema(query=Query)
