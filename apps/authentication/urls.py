from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
