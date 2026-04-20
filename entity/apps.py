"""Application configuration for entity."""

from django.apps import AppConfig


class EntityConfig(AppConfig):
    """Entity application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "entity"
