"""Application configuration for CCP."""

from django.apps import AppConfig


class CcpConfig(AppConfig):
    """CCP application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "ccp"
