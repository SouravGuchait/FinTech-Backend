"""CCP model."""

from django.db import models

from entity.models import Entity


class CCP(models.Model):
    """Central counterparty tied to an entity."""

    name = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="ccps")

    objects = models.Manager()

    class Meta:
        """Model metadata."""

        ordering = ("name",)
        verbose_name = "CCP"
        verbose_name_plural = "CCPs"

    def __str__(self) -> str:
        """Return the CCP name."""
        return str(self.name)
