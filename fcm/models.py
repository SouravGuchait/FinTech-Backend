"""FCM model."""

from django.db import models

from entity.models import Entity


class FCM(models.Model):
    """Futures commission merchant tied to an entity."""

    name = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="fcms")

    objects = models.Manager()

    class Meta:
        """Model metadata."""

        ordering = ("name",)
        verbose_name = "FCM"
        verbose_name_plural = "FCMs"

    def __str__(self) -> str:
        """Return the FCM name."""
        return str(self.name)
