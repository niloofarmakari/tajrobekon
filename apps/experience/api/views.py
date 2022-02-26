from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from ..models import Experience, ExperienceCategory, ExperienceComment
from .serializers import (
    ExperienceCategorySerializer,
    ExperienceCommentSerializer,
    ExperienceDetailSerializer,
    ExperienceSerializer,
)


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20


class ExperienceCategoryList(ListAPIView):
    """Get List of Experience Categories"""

    queryset = ExperienceCategory.objects.all()
    serializer_class = ExperienceCategorySerializer
    permission_classes = [AllowAny]


class ExperienceListCreate(ListCreateAPIView):
    """Get all experiences or create a new one"""

    queryset = Experience.objects.all().select_related("user", "category")
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPageNumberPagination


class MyExperienceList(ListAPIView):
    """Experiences created by the current user"""

    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user).select_related("category")


class ExperienceDetail(RetrieveAPIView):
    """Get experience detail by id"""

    queryset = Experience.objects.all().select_related("user", "category").prefetch_related("comments__user")
    serializer_class = ExperienceDetailSerializer
    permission_classes = [AllowAny]


class ExperienceComments(ListCreateAPIView):
    """Get comments for an experience or create a new comment for it"""

    serializer_class = ExperienceCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ExperienceComment.objects.filter(experience_id=self.kwargs["pk"]).select_related("user")

    def perform_create(self, serializer):
        serializer.save(experience_id=self.kwargs["pk"])
