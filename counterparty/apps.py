"""Application configuration for counterparty."""

from django.apps import AppConfig


class CounterpartyConfig(AppConfig):
    """Counterparty application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "counterparty"
