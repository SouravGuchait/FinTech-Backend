"""Counterparty model."""

from django.db import models


class Counterparty(models.Model):
    """Agreement counterparty."""

    name = models.CharField(max_length=255)
    counterparty_code = models.CharField(max_length=64, unique=True)

    objects = models.Manager()

    class Meta:
        """Model metadata."""

        ordering = ("name",)
        verbose_name_plural = "counterparties"

    def __str__(self) -> str:
        """Return the counterparty name."""
        return str(self.name)
