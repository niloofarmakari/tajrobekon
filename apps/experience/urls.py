from django.urls import path

from .api.views import (
    ExperienceCategoryList,
    ExperienceComments,
    ExperienceDetail,
    ExperienceListCreate,
    MyExperienceList,
)

urlpatterns = [
    path("categories/", ExperienceCategoryList.as_view(), name="experience_category_list"),
    path("<int:pk>/", ExperienceDetail.as_view(), name="experience_detail"),
    path("<int:pk>/comments", ExperienceComments.as_view(), name="experience_comments"),
    path("me/", MyExperienceList.as_view(), name="my_experience_list"),
    path("", ExperienceListCreate.as_view(), name="experience_list_create"),
]
