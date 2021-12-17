from rest_framework import serializers
from apps.experience.models import ExperienceCategory, Experience


class ExperienceCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceCategory
        fields = "__all__"


class ExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
