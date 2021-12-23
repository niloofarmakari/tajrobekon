from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

from .serializers import (
    ExperienceCategorySerializer,
    ExperienceDetailSerializer,
    ExperienceSerializer,
    ExperienceCommentSerializer,
)
from ..models import Experience, ExperienceCategory, ExperienceComment


class ExperienceCategoryList(ListCreateAPIView):
    model = ExperienceCategory
    queryset = ExperienceCategory.objects.all()
    serializer_class = ExperienceCategorySerializer


class ExperienceListCreate(ListCreateAPIView):
    model = Experience
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class MyExperienceList(ListAPIView):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)


class ExperienceDetail(RetrieveAPIView):
    model = Experience
    queryset = Experience.objects.all()
    serializer_class = ExperienceDetailSerializer


class ExperienceComments(ListCreateAPIView):
    serializer_class = ExperienceCommentSerializer

    def get_queryset(self):
        return ExperienceComment.objects.filter(experience_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        serializer.save(experience_id=self.kwargs["pk"])
