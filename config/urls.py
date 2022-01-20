from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .graphql.view import CustomGraphQLView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.authentication.urls")),
    path("graphql/", CustomGraphQLView.as_view(graphiql=True)),
    path("", include("apps.experience.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
