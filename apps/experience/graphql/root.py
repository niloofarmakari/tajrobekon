import graphene
from graphene_django.types import ObjectType
import graphene_django_optimizer as gql_optimizer

from apps.experience.graphql.types import ExperienceType
from ..models import Experience


class ExperienceRoot(ObjectType):
    experience = graphene.Field(ExperienceType, id=graphene.ID())
    experiences = graphene.List(ExperienceType, page=graphene.Int(), page_size=graphene.Int())

    def resolve_experiences(self, info, page, page_size=20, **kwargs):
        from_index = max((page - 1) * page_size, 0)
        to_index = max((page) * page_size, 0)
        return gql_optimizer.query(Experience.objects.all()[from_index:to_index], info)

    def resolve_experience(self, info, id, **kwargs):
        if id is not None:
            return Experience.objects.filter(id=id).first()
