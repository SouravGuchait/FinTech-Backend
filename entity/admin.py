"""Admin registration for entity models."""

from django.contrib import admin

from entity.models import Entity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    """Entity admin."""

    list_display = ("name", "entity_type", "created_by")
    list_filter = ("entity_type",)
    search_fields = ("name", "created_by__email")
