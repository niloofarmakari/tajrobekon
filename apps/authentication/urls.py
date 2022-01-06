from django.urls import path
from django.contrib.auth import views as auth_views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="authentication/login.html", redirect_authenticated_user=True),
        name="auth_login",
    ),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
