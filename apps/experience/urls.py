from django.urls import path
from .api.views import ExperienceCategoryList, ExperienceListCreate, ExperienceDetail


urlpatterns = [
    path("categories/", ExperienceCategoryList.as_view(), name="experience_category_list"),
    path("", ExperienceListCreate.as_view(), name="experience_list_create"),
    path("<int:pk>/", ExperienceDetail.as_view(), name="experience_detail"),
]
