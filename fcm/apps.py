"""Application configuration for FCM."""

from django.apps import AppConfig


class FcmConfig(AppConfig):
    """FCM application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fcm"
