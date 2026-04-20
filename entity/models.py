"""Entity model."""

from django.conf import settings
from django.db import models


class EntityType(models.TextChoices):
    """Supported entity classifications."""

    ENTITY = "entity", "Entity"
    ROLLUP = "rollup", "Rollup"
    TRADE = "trade", "Trade"


class Entity(models.Model):
    """Business entity used by portfolio, CCP, FCM, and agreements."""

    name = models.CharField(max_length=255)
    entity_type = models.CharField(
        max_length=16,
        choices=EntityType.choices,
        default=EntityType.ENTITY,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="created_entities",
    )

    objects = models.Manager()

    class Meta:
        """Model metadata."""

        ordering = ("name",)

    def __str__(self) -> str:
        """Return the entity name."""
        return str(self.name)
