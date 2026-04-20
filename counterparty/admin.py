"""Admin registration for counterparties."""

from django.contrib import admin

from counterparty.models import Counterparty


@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    """Counterparty admin."""

    list_display = ("name", "counterparty_code")
    search_fields = ("name", "counterparty_code")
