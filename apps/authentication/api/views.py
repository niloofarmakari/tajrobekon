from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    """Register New User"""

    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
