"""Admin registration for portfolios."""

from django.contrib import admin

from portfolio.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """Portfolio admin."""

    list_display = ("name", "entity", "base_currency")
    list_filter = ("base_currency",)
    search_fields = ("name", "entity__name")
