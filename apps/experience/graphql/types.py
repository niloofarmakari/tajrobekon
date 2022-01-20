import json
import graphene
import graphene_django_optimizer as gql_optimizer

from django.contrib.auth import get_user_model
from taggit.models import Tag
from graphene_django.types import DjangoObjectType

from ..models import Experience, ExperienceComment, ExperienceCategory


class ExperienceTagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ["name", "slug"]


class ExperienceCategoryType(DjangoObjectType):
    class Meta:
        model = ExperienceCategory
        fields = ["id", "name", "slug", "description", "created_at"]


class ExperienceUser(DjangoObjectType):
    full_name = graphene.String()

    def resolve_full_name(user, info):
        return user.get_full_name()

    class Meta:
        model = get_user_model()
        only_fields = ["id", "username", "first_name", "last_name"]


class ExperienceCommentType(DjangoObjectType):
    class Meta:
        model = ExperienceComment
        fields = [
            "user",
            "comment",
            "created_at",
        ]


class ExperienceType(gql_optimizer.OptimizedDjangoObjectType):
    comments = graphene.List(ExperienceCommentType)
    tags = graphene.List(ExperienceTagType)
    schema = graphene.String()

    class Meta:
        model = Experience
        fields = [
            "id",
            "description",
            "created_at",
            "category",
            "user",
        ]

    @gql_optimizer.resolver_hints(prefetch_related=("comments__user",))
    def resolve_comments(experience: Experience, info, **kwargs):
        return experience.comments.all()

    @gql_optimizer.resolver_hints(prefetch_related=("tags",))
    def resolve_tags(experience: Experience, info, **kwargs):
        return experience.tags.all()

    @gql_optimizer.resolver_hints(select_related=("category", "user"), prefetch_related=("comments__user", "tags"))
    def resolve_schema(experience: Experience, info, **kwargs):
        return json.dumps(experience.get_schema(), ensure_ascii=False)
