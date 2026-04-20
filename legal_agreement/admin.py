"""Admin registration for legal agreements."""

from django.contrib import admin

from legal_agreement.models import LegalAgreement


@admin.register(LegalAgreement)
class LegalAgreementAdmin(admin.ModelAdmin):
    """Legal agreement admin."""

    list_display = (
        "agreement_name",
        "entity",
        "counterparty",
        "ccp",
        "fcm",
        "agreement_type",
        "is_active",
    )
    list_filter = ("agreement_type", "is_active", "start_date", "end_date")
    search_fields = (
        "agreement_name",
        "entity__name",
        "counterparty__name",
        "ccp__name",
        "fcm__name",
    )
