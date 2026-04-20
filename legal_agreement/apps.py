"""Application configuration for legal agreements."""

from django.apps import AppConfig


class LegalAgreementConfig(AppConfig):
    """Legal agreement application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "legal_agreement"
