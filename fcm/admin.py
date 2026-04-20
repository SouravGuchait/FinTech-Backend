"""Admin registration for FCMs."""

from django.contrib import admin

from fcm.models import FCM


@admin.register(FCM)
class FCMAdmin(admin.ModelAdmin):
    """FCM admin."""

    list_display = ("name", "entity")
    search_fields = ("name", "entity__name")
