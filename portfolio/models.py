"""Portfolio model."""

from django.db import models

from entity.models import Entity


class Portfolio(models.Model):
    """Portfolio tied to an entity."""

    name = models.CharField(max_length=255)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="portfolios")
    base_currency = models.CharField(max_length=8)

    objects = models.Manager()

    class Meta:
        """Model metadata."""

        ordering = ("name",)

    def __str__(self) -> str:
        """Return the portfolio name."""
        return str(self.name)
