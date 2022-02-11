from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .graphql.view import CustomGraphQLView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", CustomGraphQLView.as_view(graphiql=True)),
    path("experiences/", include("apps.experience.urls")),
    path("auth/", include("apps.authentication.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", include("rest_framework.urls")),
    path("", include("apps.index.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
