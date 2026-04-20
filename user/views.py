"""Session-based authentication views."""

from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import RegisterSerializer, UserSerializer


@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(APIView):
    """Register a user for local development and API clients."""

    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        """Create a user and return the public representation."""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    """Authenticate a user and persist the session cookie."""

    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        """Log a user in by email or username."""
        identifier = request.data.get("email") or request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=identifier, password=password)
        if user is None:
            return Response({"message": "invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)
        return Response({"message": "logged in"})


@method_decorator(csrf_exempt, name="dispatch")
class LogoutView(APIView):
    """End the active session."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Log out the current user."""
        logout(request)
        return Response({"message": "logged out"})


@method_decorator(csrf_exempt, name="dispatch")
class MeView(APIView):
    """Return the current session user."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return authenticated user details."""
        return Response(UserSerializer(request.user).data)
