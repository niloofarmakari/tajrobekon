import json

from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from taggit.serializers import TagListSerializerField, TaggitSerializer

from apps.authentication.api.serializers import UserSerializer
from ..models import ExperienceCategory, Experience, ExperienceComment


class ExperienceCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ExperienceCategory
        fields = ["name", "slug", "description", "user"]


class ExperienceCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ExperienceComment
        fields = ["id", "user", "comment"]


class ExperienceCategoryForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return ExperienceCategory.objects.all()


class ExperienceSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = ExperienceCategoryForeignKey()
    tags = TagListSerializerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Experience
        fields = ["id", "type", "category", "description", "tags", "user"]


class ExperienceDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = ExperienceCommentSerializer(read_only=True, many=True)
    schema = serializers.SerializerMethodField()

    def get_schema(self, experience: Experience):
        return json.dumps(experience.get_schema(), ensure_ascii=False)

    class Meta:
        model = Experience
        fields = ["id", "type", "category", "description", "tags", "user", "comments", "schema"]


class ExperienceCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ExperienceComment
        fields = ["id", "user", "comment"]
