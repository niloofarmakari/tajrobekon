from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.pagination import PageNumberPagination

from .serializers import (
    ExperienceCategorySerializer,
    ExperienceDetailSerializer,
    ExperienceSerializer,
    ExperienceCommentSerializer,
)
from ..models import Experience, ExperienceCategory, ExperienceComment


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20


class ExperienceCategoryList(ListCreateAPIView):
    model = ExperienceCategory
    queryset = ExperienceCategory.objects.all()
    serializer_class = ExperienceCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ExperienceListCreate(ListCreateAPIView):
    model = Experience
    queryset = Experience.objects.all().select_related("user").prefetch_related("tags", "comments__user")
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination


class MyExperienceList(ListAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user).select_related("category").prefetch_related("tags")


class ExperienceDetail(RetrieveAPIView):
    model = Experience
    queryset = Experience.objects.all().select_related("user", "category").prefetch_related("comments__user")
    serializer_class = ExperienceDetailSerializer
    permission_classes = [AllowAny]


class ExperienceComments(ListCreateAPIView):
    serializer_class = ExperienceCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ExperienceComment.objects.filter(experience_id=self.kwargs["pk"]).select_related("user")

    def perform_create(self, serializer):
        serializer.save(experience_id=self.kwargs["pk"])
