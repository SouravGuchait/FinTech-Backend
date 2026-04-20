"""Admin registration for CCPs."""

from django.contrib import admin

from ccp.models import CCP


@admin.register(CCP)
class CCPAdmin(admin.ModelAdmin):
    """CCP admin."""

    list_display = ("name", "entity")
    search_fields = ("name", "entity__name")
