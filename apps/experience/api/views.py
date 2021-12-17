from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .serializers import ExperienceCategoryModelSerializer, ExperienceModelSerializer
from ..models import Experience, ExperienceCategory


class ExperienceCategoryList(ListCreateAPIView):
    model = ExperienceCategory
    queryset = ExperienceCategory.objects.all()
    serializer_class = ExperienceCategoryModelSerializer


class ExperienceListCreate(ListCreateAPIView):
    model = Experience
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer


class ExperienceDetail(RetrieveAPIView):
    model = Experience
    queryset = Experience.objects.all()
    serializer_class = ExperienceModelSerializer
