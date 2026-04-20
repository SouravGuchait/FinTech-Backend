"""Authentication backends for the user app."""

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailOrUsernameBackend(ModelBackend):
    """Authenticate users by either unique email or username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        """Return a user when the identifier and password are valid."""
        identifier = username or kwargs.get("email") or kwargs.get("username")
        if identifier is None or password is None:
            return None

        user_model = get_user_model()
        try:
            user = user_model.objects.get(
                Q(email__iexact=identifier) | Q(username__iexact=identifier)
            )
        except user_model.DoesNotExist:
            user_model().set_password(password)
            return None
        except user_model.MultipleObjectsReturned:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
