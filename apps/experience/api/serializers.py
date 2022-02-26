import json

from rest_framework import serializers

from apps.authentication.api.serializers import UserSerializer

from ..models import Experience, ExperienceCategory, ExperienceComment


class ExperienceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceCategory
        fields = ["name", "slug", "description"]


class ExperienceCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info = UserSerializer(read_only=True, source="user")

    class Meta:
        model = ExperienceComment
        fields = ["id", "user", "user_info", "comment"]


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_info = UserSerializer(read_only=True, source="user")

    class Meta:
        model = Experience
        fields = ["id", "category", "description", "user", "user_info"]


class ExperienceDetailSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(read_only=True, source="user")
    comments = ExperienceCommentSerializer(read_only=True, many=True)
    similar = ExperienceSerializer(source="get_similar", read_only=True, many=True)
    schema = serializers.SerializerMethodField()

    def get_schema(self, experience: Experience) -> str:
        return json.dumps(experience.get_schema(), ensure_ascii=False)

    class Meta:
        model = Experience
        fields = ["id", "category", "description", "similar", "user_info", "comments", "schema"]
