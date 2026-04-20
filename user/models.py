"""User models."""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Application user authenticated by email or username."""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True, db_column="firstname")
    last_name = models.CharField(max_length=150, blank=True, db_column="lastname")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        """Model metadata."""

        ordering = ("email",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        """Return a readable representation."""
        return self.email

    @property
    def firstname(self) -> str:
        """Compatibility alias for API clients using firstname."""
        return self.first_name

    @property
    def lastname(self) -> str:
        """Compatibility alias for API clients using lastname."""
        return self.last_name
