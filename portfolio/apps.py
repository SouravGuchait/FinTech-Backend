"""Application configuration for portfolio."""

from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """Portfolio application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
